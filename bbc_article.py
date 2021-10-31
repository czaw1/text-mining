from newspaper import Article

url = 'https://www.bbc.com/news/world-asia-55902070'
article = Article(url)
article.download()
article.parse()
print(article.text)

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
tokens = word_tokenize(article.text)
# print(tokens)
tokens = [w.lower() for w in tokens]
import string
table = str.maketrans("","", string.punctuation)
stripped = [w.translate(table) for w in tokens]
words = [word for word in stripped if word.isalpha()]
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
words = [w for w in words if not w in stop_words]
# print(words[:30])
from collections import Counter
Counter = Counter(words)
most_occur = Counter.most_common(10)
print(most_occur)