## NLP 
We use RASA platform for building our NLP service  for some reasons: RASA is an open-source natural language processing tool, it can run locally and has the advantage of self-hosted open source such as adaptability, data control, etc.

spaCy is a popular open-source library for natural language processing in Python. It provides easy-to-use interfaces to perform tasks such as tokenization, part-of-speech tagging, dependency parsing, and named entity recognition.

spaCy provides a number of pre-trained models that can be used out-of-the-box for various NLP tasks. These models are trained on large datasets and provide excellent performance for a variety of languages.

In this project, we are using the `en_core_web_md model`, which is a large English model that includes vectors for words in the model vocabulary. This model is well-suited for tasks such as named entity recognition and part-of-speech tagging.

## Installation 
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
You will need to install the following dependencies:
- Python 3.6 or later
- Rasa
- spaCy

You can install these dependencies using pip:
```sh
pip install -r requirements.txt
```
You will also need to download the necessary spaCy models. You can do this by running the following command:
```sh
python -m spacy download en_core_web_md
```
## Rasa Train & Run
First let us use the cmd to train then test. 
```sh
rasa train
rasa shell
``` 
Enabling the HTTP API
```diff
rasa run --enable-api -p $port
```