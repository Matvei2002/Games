def morse_code(phrase):
    result = ''
    morse = {'a': '.—', 'b': '—...', 'c': '—.—.', 
              'd': '—..', 'e': '.', 'f': '..—.',
              'g': '——.', 'h': '....', 'i': '..',
              'j': '.———', 'k': '—.—', 'l': '.—..',
              'm': '——', 'n': '—.', 'o': '———', 'p': '.——.',
              'q': '——.—', 'r': '.—.', 's': '...', 't': '—',
              'u': '..—', 'v': '...—', 'w': '.——', 'x': '—..—',
              'y': '—.——', 'z': '——..'}
    for i in phrase:
        if i in morse:  # проверяем наличие символа
            result += morse[i]
            result += ' '
    return(result)


def main():
    phrase = (input('Введите фразу: ')).lower()
    print(morse_code(phrase))

main()