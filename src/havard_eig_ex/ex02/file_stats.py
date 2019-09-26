from collections import Counter


def char_counts(textfilename):
    with open(textfilename, encoding='UTF-8') as f:
        data = f.read()
        freq_of_char = Counter(data)
        list_char_freq = [0 for _ in range(256)]
        for key, value in freq_of_char.items():
            if ord(key) < 256:
                list_char_freq[ord(key)] = value
    return list_char_freq


if __name__ == '__main__':
    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
