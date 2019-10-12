from random import shuffle

def anagramize(word):
    array_word = list(word)
    shuffle(array_word)
    return "".join(array_word)

print(list(map(anagramize, ['armpit', 'bear bear', 'hairs'])))
