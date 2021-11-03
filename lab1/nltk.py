import nltk
nltk.download('popular')
from urllib import request
url='https://www.gutenberg.org/files/2554/2554-0.txt'
response=request.urlopen(url)
raw=response.read().decode('utf8')
type(raw)
print('Hello')
raw[1:74]
tokens = nltk.word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[1:10])