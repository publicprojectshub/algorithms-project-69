import re


def string_cleaner(input_string):
    pattern = r'[!\"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~]'
    cleaned_string = re.sub(pattern, '', input_string, flags=re.IGNORECASE)
    return cleaned_string


def search(docs: list, target_string: str):
    searched_docs = dict()  # {doc_id_with_target_string: target_string_amount}
    for doc in docs:
        doc_cleaned_text = string_cleaner(doc['text']).lower().split()
        if target_string.lower() in doc_cleaned_text:
            searched_docs[doc['id']] = doc['text'].count(target_string)
    # sorted dict to list
    result = [doc[0] for doc in sorted(searched_docs.items(), key=lambda item: item[1], reverse=True)]
    return result
