import math


def letter_freq(txt):
    dictionary = {}
    txt = txt.lower()
    for j in txt:
        if j in dictionary:
            dictionary[j] += 1
        else:
            dictionary[j] = 1
    return dictionary


def entropy(message):
    char_freq = letter_freq(message)
    tot_char = 0
    for _ in message:
        tot_char += 1
    freq_letter = {}
    for key, value in char_freq.items():
        freq_letter[ord(key)] = value/tot_char
    entropy = 0
    for value in freq_letter.values():
        entropy += value * math.log2(value)
    return entropy


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
