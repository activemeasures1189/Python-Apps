import json
import difflib
from difflib import get_close_matches

data = json.load(open('C:/Users/Peter/Desktop/Webdev/Python Apps/English Dictionary/data.json', 'r'))

def dictionary(w):
    w = w.lower()
    if w in data:
       return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        print(get_close_matches(w, data.keys()))
        yn = input('Did you mean {0}? Press Y for yes, N for no.'.format(get_close_matches(w, data.keys()) [0]))
        if yn == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N':
            return "Record not found"
        else:
            return "Word was not understood"
    else:
        print('not found')
word = input('Enter word: ')
print(dictionary(word))




