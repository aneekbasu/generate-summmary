from nltk.cluster.util import cosine_distance
import numpy as np
import sentence_similarity as ss

def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = ss.sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix
