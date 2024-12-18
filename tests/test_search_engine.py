from search_engine import search_engine

doc1 = "I can't shoot straight unless I've had a pint!"
doc2 = "Don't shoot_ shoot shoot that thing at me."
doc3 = "I'm your shooter."
doc4 = "You are _Shooter!."

docs = [
    {'id': 'doc1', 'text': doc1},
    {'id': 'doc2', 'text': doc2},
    {'id': 'doc3', 'text': doc3},
    {'id': 'doc4', 'text': doc4},
]

input_str = "Hello, World! ;:>=-)_This is a test: @2023 #Python."


def test_search():
    assert search_engine.search(docs, 'money') == []
    assert search_engine.search([], 'shoot') == []
    assert search_engine.search(docs, 'pint') == ['doc1']
    assert search_engine.search(docs, 'shooter') == ['doc3', 'doc4']


def test_search_relevance():
    assert search_engine.search(docs, 'shoot') == ['doc2', 'doc1']


def test_string_cleaner():
    assert search_engine.string_cleaner(input_str) == 'Hello World This is a test 2023 Python'
