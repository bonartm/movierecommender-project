"""
contains various implementations for recommending movies
"""

import pandas as pd
from utils import movies, ratings, nmf_model


def recommend_random(query, k=10):
    """
    Recommends a list of k random movie ids
    """
    return [1, 20, 34, 25]


def recommend_popular(query, k=10):
    """
    Recommend a list of k movie ids that are the most popular
    """
    return []


def recommend_nmf(query, k=10):
    """
    Recommend a list of k movie ids based on a trained NMF model
    """
    return []


def recommend_neighbors(query, k=10):
    """
    Recommend a list of k movie ids based on the most similar users
    """
    return []



# list of liked movies
query = [1, 34, 56, 21]
print(recommend_random(query))
