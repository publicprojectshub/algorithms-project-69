import re


def string_cleaner(input_string):
    pattern = r'[!\"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~]'
    cleaned_string = re.sub(pattern, '', input_string, flags=re.IGNORECASE)
    return cleaned_string


def search(docs: list, target_string: str):
    result = []
    for doc in docs:
        doc_cleaned_text = string_cleaner(doc['text']).lower().split()
        if target_string.lower() in doc_cleaned_text:
            result.append(doc['id'])
    return result
