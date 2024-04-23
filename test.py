import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

file = open("random_paragraphs.txt", "r")
text=file.read()

tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

word_freq = Counter(filtered_tokens)
for word, count in word_freq.most_common():
    print(word, count)