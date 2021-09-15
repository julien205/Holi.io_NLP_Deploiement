'''The file to launch our applications'''

'''---------The imports-----------------'''
from flask import Flask, request, render_template, Markup, jsonify
import joblib

#We import the functions we have build, they have as parameters the input text and sometimes the model
from functions.find_keywords import find_keywords
from functions.preprocessing_text import preprocess_text
from functions.topic_text import topic_text
from functions.color_text import color_text
from functions.color_text import mycolors

'''---------name of the app-----------------'''
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

'''-------Load model-----------------'''
model = joblib.load("models/lda_model.joblib")


'''---------The different pages-----------------'''
'''Our home page'''
@app.route("/")
def index():
     return render_template('index.html')

'''Our model plot with the help of the pyLDAvis library'''
@app.route("/model")
def goto_model():
     return render_template('lda.html')

'''Our documentation for the api'''
@app.route("/api_doc")
def goto_api():
     return render_template('api_doc.html')


'''Our live application'''
@app.route("/live_app")
def goto_live_app():
     return render_template('live_app.html')
 
 
'''Our result page for the input'''
@app.route("/result_live", methods=['POST'])
def result_live():
     text = request.form['input_text']
     l_keywords = int(request.form['l_keywords'][0])
     n_keywords = int(request.form['n_keywords'][0])
     n_topics = int(request.form['n_topics'][0])
     
     #We use the function to preprocess the text
     processed_text = preprocess_text(text)
     
     #We use the function that extract keywords
     try:
          keywords = find_keywords(processed_text, l_keywords, n_keywords)
     except:
          keywords=["No keyword found"]
          
     #We use the function that make the topic modeling, and we color the text according to the topics
     try:
          topics = topic_text(model,processed_text, n_topics)
          topics_colored = ["<font color=\"" + mycolors[i] + "\">" + topics[i] + ' ' + "</font>" for i in range(len(topics))]
     except:
          topics = ["No topic found"]
          
     #We use the function that colorize the text
     try:
          colored_text = color_text(model,processed_text,n_topics)
     except:
          colored_text = ["Impossible to colorize this text"]
     
     #We return the results 
     return render_template('live_app.html', topics=[Markup(x) for x in topics_colored], keywords=keywords, colored_text = Markup(colored_text))


'''Our API page'''
@app.route("/api", methods=["POST"])
def api():
     # Get the data
     req = request.get_json()
     # Check mandatory key
     if "text" in req.keys():
          text = req["text"]
     if "l_keywords" in req.keys():
          l_keywords = int(req["l_keywords"])
     if "n_keywords" in req.keys():
          n_keywords = int(req["n_keywords"])
     if "n_topics" in req.keys():
          n_topics = int(req["n_topics"])
     # preprocessing du text
     processed_text = preprocess_text(text)
     print('preprocessing done')
     #We use the function that extract keywords
     try:
        keywords = find_keywords(processed_text, l_keywords, n_keywords)
     except:
        keywords=["No keyword found"]
     print('preprocessing done')
     
     #We use the function that make the topic modeling
     try:
          topics = topic_text(model,processed_text, n_topics)
     except:
          topics = ["No topic found"]   
     print('Topcs modeling done')

     return jsonify({"keywords": keywords, "topics":topics}), 200


'''---------bottom activator-----------------'''
if __name__ == "__main__":
    app.run(debug=True)