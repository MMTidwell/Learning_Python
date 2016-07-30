lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction'
}
"""
    'direction': 'north south east west down up left right back',
    'verbs': 'go stop kill eat',
    'stop': 'the in of from at it',
    'noun': 'door bear princess cabinet'
"""


def scan(sentence):
    words = sentence.split()
    result = []

    for word in words:
        pair = (lexicon[word], word)
        result.append(pair)

    return result


