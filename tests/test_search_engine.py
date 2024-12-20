from search_engine import search_engine

doc1 = "I can't shoot straight unless I've had a pint!"
doc2 = "Don't shoot_ shoot shoot that thing at me."
doc3 = "I'm your shooter."
doc4 = "You are _Shooter!."

docs = [
    {"id": "doc1", "text": doc1},
    {"id": "doc2", "text": doc2},
    {"id": "doc3", "text": doc3},
    {"id": "doc4", "text": doc4},
]

docs2 = [
    {"id": "doc1", "text": doc1}
]

input_str = "Hello, World! ;:>=-)_This is a test: @2025 #Python."


def test_search():
    assert search_engine.search(docs, 'money') == []
    assert search_engine.search([], 'shoot') == []
    assert search_engine.search(docs, 'pint') == ['doc1']
    assert search_engine.search(docs, 'shooter') == ['doc3', 'doc4']


def test_search_relevance():
    assert search_engine.search(docs, 'shoot') == ['doc2', 'doc1']


def test_search_few_words():
    assert search_engine.search(docs, 'shoot at me') == ['doc2', 'doc1']


def test_tokenize():
    assert search_engine.tokenize(input_str) == ['hello', 'world', 'this', 'is', 'a', 'test', '2025', 'python']


def test_index_inverter():
    assert search_engine.index_inverter(docs2) == {'i': ['doc1'], "can't": ['doc1'], 'shoot': ['doc1'],
                                                   'straight': ['doc1'], 'unless': ['doc1'], "i've": ['doc1'],
                                                   'had': ['doc1'], 'a': ['doc1'], 'pint': ['doc1']}
