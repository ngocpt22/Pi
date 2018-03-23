import json
from difflib import get_close_matches

with open('data.json') as mydata:
    data = json.load(mydata)


def mydictionary(word):  #keyword is local variable
    word = str(word).lower()
    if word in data:  # useful built-in function
        return formatOutput(data[word])
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        yn = input('Did you mean %s instead? Enter Y if yes, or N if no: ' %
                   get_close_matches(word, data.keys())[0])
        if yn == 'Y':
            return formatOutput(result = data[get_close_matches(word, data.keys(), cutoff=0.8)[0]])
        elif yn == 'N':
            return 'There is no such word in English. Please double check it.'
        else:
            return 'We didn\'t understand your entry'
    else:
        return 'There is no such word in English'

def formatOutput(result):
    if len(result) == 1:
        return result[0]
    else:
        mul_result = ''
        for i in result:
            mul_result = mul_result + i + '\n'
        return mul_result
keyword = input('Enter keyword: ')  #keyword is global variable

print(mydictionary(keyword))