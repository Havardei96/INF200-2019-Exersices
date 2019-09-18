def letter_freq(txt):
    dictionary = {}
    txt = txt.lower()
    for j in txt:
        if j in dictionary:
            dictionary[j] += 1
        else:
            dictionary[j] = 1
    return dictionary

if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))