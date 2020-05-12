from collections import Counter
from re import sub
from sys import exit



while True:
    try:
        path_to_file = input("Input path to file and press 'Enter': ")
        if path_to_file in 'Nn':
            exit(0)
        file = open(path_to_file)
    except (FileNotFoundError):
        print("\nThis path is wrong.\n"
              "Please input another path or press 'N' for exit.\n")
    else:
        break

text = file.read()
text = sub('[.,?!:;-]','',text)
text = text.lower()
words = text.split()

words_dict = Counter(words)

print("\nThere are {} words\n".format(sum(words_dict.values())))
for word, count in sorted(words_dict.items()):
    print("{0} - {1} time(s)".format(word, count))



