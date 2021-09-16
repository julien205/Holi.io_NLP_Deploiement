# Holi.io_NLP_Deploiement

  Ce projet, proposé par Clément Sirvente, a été fait en coopération avec Florian Guillot.
  
La demande de holi.io est détaillée dans le fichier project_initialisation.pdf, fourni par Clément Sirvente

Nous avions choisi de présenter ce projet sous la forme d'une réunion client qui décrirait notre démarche, celle ci est résumée dans le document de Projet_ginal_presentation.pdf

Le principe du projet est d'extraire de l'information de documents sous la forme de topics et de mots clés.
Nous avons dans un premier temps preprocessé les données fournies par Clément (articles de presses réunis dans le Mind Dataset de Microsoft).
Cette étape est décrite dans le notebook step1_import_data.ipynb.

Pour ce qui est de l'extraction d'information, nous avons utilisé deux méthodes: 
    - le topic modeling par LDA dont l'entrainement et l'optimisation du paramètrage sont décrit dans le notebook  
Step2_LDA_model_training.ipynb
    - l'extraction de keywords grace à un model de réseau de neurone préentrainé basé sur BERT
    SentenceTransformer: 'distilbert-base-nli-mean-tokens'
    
Enfin nous avons souhaité présenter nos résultats dans une application disponible à l'adresse https://jedha-holi-text-analyzer.herokuapp.com (Nous avons utilisé la version gratuite de Heroku, notre site manque donc de stabilité en ligne mais est performant en local via flask.
