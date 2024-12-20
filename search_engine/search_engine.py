import re
from collections import Counter, defaultdict


def tokenize(text: str):
    """return list of split and lower text and digits and apostrophes"""
    return re.findall(r"[a-zA-Z0-9']+", text.lower())


def calculate_relevance_score(doc: dict, query: str):
    doc_tokens = tokenize(doc['text'])
    query_tokens = tokenize(query)
    doc_counter = Counter(doc_tokens)
    query_counter = Counter(query_tokens)
    intersections = set(doc_counter) & set(query_counter)
    intersections_score = sum(doc_counter[word] * query_counter[word] for word in intersections)
    return intersections_score


def index_inverter(docs_list: list):
    """index_inverter return inverted words index like {'Hello':[doc2, doc3], 'world': [doc1, doc2]}"""
    inverted_index = dict()
    for doc in docs_list:
        doc_id = doc["id"]
        text_tokens = tokenize(doc["text"])
        for token in text_tokens:
            if token not in inverted_index:
                inverted_index[token] = []
            inverted_index[token].append(doc_id)
    return inverted_index


def search(docs: list, query: str):
    found_docs = []
    for doc in docs:
        score = calculate_relevance_score(doc, query)
        found_docs.append((doc['id'], score))
    found_docs.sort(key=lambda item: item[1], reverse=True)
    result = [doc_id for doc_id, score in found_docs if score > 0]
    return result
