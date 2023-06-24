import argparse
import random
import string

def xkcdpwgen(num_words, num_caps, num_nums, num_symbols):
    "make a password generator using the XKCD method"
    words = []
    with open('words.txt', 'r') as file:
        for line in file:
            words.append(line.strip())

    # shuffle words from 'words.txt'
    random.shuffle(words)
    selected_words = words[:num_words]

    # capitalize the first word if there are any caps
    if num_caps > 0:
        random.shuffle(selected_words)
        selected_words = [word.capitalize() for word in selected_words[:num_caps]] + selected_words[num_caps:]

    password = ''.join(selected_words)

    # add numbers to password
    if num_nums > 0:
        numbers = ''.join(random.choices(string.digits, k=num_nums))
        password += numbers

    # add symbols to the password
    if num_symbols > 0:
        symbols = ''.join(random.choices(string.punctuation, k=num_symbols))
        password += symbols

    return password

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a secure, memorable password using the XKCD method')
    parser.add_argument('-w', '--words', type=int, default=4, help='include WORDS words in the password (default=4)')
    parser.add_argument('-c', '--caps', type=int, default=0, help='capitalize the first letter of CAPS random words (default=0)')
    parser.add_argument('-n', '--numbers', type=int, default=0, help='insert NUMBERS random numbers in the password (default=0)')
    parser.add_argument('-s', '--symbols', type=int, default=0, help='insert SYMBOLS random symbols in the password (default=0)')
    args = parser.parse_args()

    password = xkcdpwgen(args.words, args.caps, args.numbers, args.symbols)
    print(password)