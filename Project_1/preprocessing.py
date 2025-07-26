import os
import re
import nltk
from sklearn.datasets import load_files

nltk.download('stopwords')
from nltk.corpus import stopwords

def load_dataset(path):
    dataset = load_files(path, encoding='latin1', decode_error='ignore')
    return dataset.data, dataset.target, dataset.target_names

def clean_text(text):
    text = re.sub(r'\W', ' ', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)

def preprocess_corpus(corpus):
    return [clean_text(doc) for doc in corpus]
