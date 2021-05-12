########################
# Recommender Function #
########################

import pickle
import time
import numpy as np
from itertools import chain, product
from difflib import get_close_matches, SequenceMatcher
from gensim.models import Word2Vec

def recommend_product(product_count, cluster_number, current_basket):
    """
    Parameters: 
    -------------------
    product_count: int
      The number of products to be recommended
    cluster_number: int
      The cluster number the user belongs to
    current_basket: list
      A list of basket items

    Returns:
    -------------------
    recommendations: list
      A list of product recommendations based on the input
    """

    # Load models
    cluster_item_models = [Word2Vec.load(f"./cluster_models/model_cluster_{id}.model") for id in range(0, 13)]
    model = cluster_item_models[cluster_number-1]

    # Load Product name lookup from disk
    with open('product_lookup.pkl', 'rb') as file:
        product_lookup = pickle.load(file)

    product_id_lookup = dict(map(reversed, product_lookup.items()))

    items = [item for item in current_basket]

    matches = list(chain.from_iterable([get_close_matches(item, product_lookup.values()) for item in current_basket]))

    product_ids_matches = [product_id_lookup[item] for item in matches]

    def filter_matches(cluster_model, product_ids_matches):
        return [product_id for product_id in product_ids_matches if cluster_model.wv.__contains__(product_id)]

    filtered_matches = filter_matches(model, product_ids_matches)

    product_names = [product_lookup[product] for product in filtered_matches]

    cross_product_names = [product for product in list(product(product_names, product_names)) if product[0] != product[1]]

    if np.mean([SequenceMatcher(None, cross[0], cross[1]).ratio() for cross in cross_product_names]) > 0.5:
        filtered_matches_cleared = [filtered_matches[0]]
    else:
        filtered_matches_cleared = filtered_matches

    def average_item_vectors(cluster_model, product_ids_matches):
        if len(product_ids_matches) == 1:
            return cluster_model.wv[product_ids_matches[0]]
        else:    
            embeddings = [cluster_model.wv[product_id] for product_id in product_ids_matches]
            
            def softmax_weights(embeddings):
                raw_weights = [np.exp(i) for i in range(1, len(embeddings)+1)]
                softmax_weights = np.array([raw_weight/sum(raw_weights) for raw_weight in raw_weights])
                return softmax_weights
            sm_weights = softmax_weights(embeddings)

            return np.average(embeddings, axis=0, weights=sm_weights)

    basket_vector = average_item_vectors(model, filtered_matches_cleared)

    def retrieve_most_similar_products(cluster_model, product_lookup, basket_vector, n_matches):
        similar_products = cluster_model.wv.similar_by_vector(basket_vector, topn=n_matches)[1:n_matches+1]
        similar_products_id = [similar[0] for similar in similar_products]
        recommendations = [product_lookup[item_number] for item_number in similar_products_id]
            
        return recommendations   

    recommendations = retrieve_most_similar_products(model, product_lookup, basket_vector, n_matches=5)
    
    filtered_recommendations = [recommendation for recommendation in recommendations if recommendation not in matches][0:product_count]

    return {'recommendations': filtered_recommendations}



