def search(docs: list, target_string: str):
    result = []
    for doc in docs:
        if target_string in doc['text'].split():
            result.append(doc['id'])
    return result


# Текст документов
doc1 = "I can't shoot straight unless I've had a pint!"
doc2 = "Don't shoot shoot shoot that thing at me."
doc3 = "I'm your shooter."

# создание документа
# документ имеет два атрибута "id" и "text"
docs = [
    {'id': 'doc1', 'text': doc1},
    {'id': 'doc2', 'text': doc2},
    {'id': 'doc3', 'text': doc3},
]

# поисковый движок проводит поиск
result = search(docs, 'shoot')

print(result)  # => ['doc1', 'doc2']

# Документы пусты
print(search([], 'shoot'))  # []
