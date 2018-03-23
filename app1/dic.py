import json

with open('data.json') as mydata:
    data = json.load(mydata)

def mydictionary(keyword):#keyword is local variable
    if str(keyword).lower in data: # useful built-in function
        return data[keyword]
    else:
        return 'There is no such word in English'

keyword = input('Enter keyword: ') #keyword is global variable

print(mydictionary(keyword))