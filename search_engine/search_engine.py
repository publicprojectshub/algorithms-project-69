import re
from collections import Counter


def tokenize(text):
    # return list of split and lower text and digits
    return re.findall(r'[a-zA-Z0-9]+', text.lower())


def calculate_relevance_score(doc_tokens, query_tokens):
    doc_counter = Counter(doc_tokens)
    query_counter = Counter(query_tokens)

    intersections = set(doc_counter) & set(query_counter)
    intersections_score = sum(doc_counter[word] * query_counter[word] for word in intersections)

    return intersections_score


def search(docs: list, query: str):
    query_tokens = tokenize(query)

    # (doc id: score)
    found_docs = []

    for doc in docs:
        doc_tokens = tokenize(doc['text'])
        score = calculate_relevance_score(doc_tokens, query_tokens)

        found_docs.append((doc['id'], score))
    found_docs.sort(key=lambda item: item[1], reverse=True)
    result = [doc_id for doc_id, score in found_docs if score > 0]

    return result

