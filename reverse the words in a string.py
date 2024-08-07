def rev_sent(sentence):
    words=sentence.split(' ')
    reverse_sentence=(' ').join(reversed(words))
    return reverse_sentence

x=input('Input is ')
print(rev_sent(x))