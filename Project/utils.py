import pandas as pd

def load_csv(path):
    return pd.read_csv(path)

def save_model(model, path):
    import pickle
    with open(path, 'wb') as f:
        pickle.dump(model, f)
