import re
from nltk.tokenize import word_tokenize

# Run the following command to install nltk for the first time:
# import nltk
# nltk.download('punkt')


sentence = "i am sleepy. it's really cold"
words = word_tokenize(sentence)
print(words)

def spl_chars_removal(lst):
    lst1=list()
    for element in lst:
        str=""
        str = re.sub("[-9a-zA-Z]"," ",element)
        lst1.append(str)
    return lst1


def main():
    sentence = "i am sleepy. it's really cold"
    result = ''.join(e for e in sentence if e.isalnum())
    words = word_tokenize(result)
    print(words)

    # print(spl_chars_removal(words))
    # pass

if __name__=='__main__':
    main()