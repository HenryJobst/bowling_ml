import pandas as pd
from bowling_rolls_transformations.transformations import convert


def load_data(path):
    df = pd.read_csv(path, header=0, names=['rolls', 'scores'])
    rolls = df['rolls'].apply(convert).values
    scores = df['scores'].values
    return rolls, scores