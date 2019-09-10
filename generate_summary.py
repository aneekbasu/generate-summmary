from nltk.corpus import stopwords
import networkx as nx
import read_article as ra
import similarity_matrix as sm

def generate_summary(file_name, top_n):
    stop_words = stopwords.words('english')
    summarize_text = []

    sentences =  ra.read_article(file_name)

    sentence_similarity_martix = sm.build_similarity_matrix(sentences, stop_words)

    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
    if(top_n>len(ranked_sentence)):
        print("Entered number of sentences is greater than the actual summary")
        return


    for i in range(top_n):
      summarize_text.append(" ".join(ranked_sentence[i][1]))

    print("Summarize Text: \n", ". ".join(summarize_text))
