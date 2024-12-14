from search_engine import search_engine

doc1 = "I can't shoot straight unless I've had a pint!"
doc2 = "Don't shoot shoot shoot that thing at me."
doc3 = "I'm your shooter."

docs = [
    {'id': 'doc1', 'text': doc1},
    {'id': 'doc2', 'text': doc2},
    {'id': 'doc3', 'text': doc3},
]


def test_search():
    assert search_engine.search(docs, 'shoot') == ['doc1', 'doc2']
    assert search_engine.search(docs, 'money') == []
    assert search_engine.search([], 'shoot') == []
