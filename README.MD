# ChatBot Application
## About Project

This is M.Tech project for Chatbot using Banking Dataset
Chatbot project is uses a Multi-Label Classification model where we have 3 parts of the project UI, Backend, Chatbot Engine (Multi Classification and NER). 

Dataset is https://huggingface.co/datasets/banking77
Classification Model is NN based model along with BERT. InDepth code can be found in file multi_label_classification.ipynb.
UI is developed using ReactJS (https://reactjs.org/)
Backend API is developed using https://flask.palletsprojects.com/en/2.1.x/

#### Developer Tools
Download and install latest version of NodeJS (https://nodejs.org/en/)
Download and install latest version of Python (https://www.python.org/downloads/)
Download CoreNLP NER from https://nlp.stanford.edu/software/stanford-ner-4.2.0.zip
Download CoreNLP NER Postagger https://nlp.stanford.edu/software/stanford-tagger-4.2.0.zip

Install ReactJS via npm,
Install Tensorflow, Pandas, Transformers, SkLearn, MatplotLib via pip
Install Flask via pip

Once all installations are done go into chatbot-app and run npm i to install all dependencies

#### How to run this Project

Step 1: Run multi_label_classification.ipynb file. It will save the model weights
Step 2: Run app.py if the project run succesfully you will see a message stating the project has been started on port no: 105
Step 3: Go into the chatbot-app and run npm i. Open chrome and type url http://localhost:3000
