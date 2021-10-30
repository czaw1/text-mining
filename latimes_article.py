from newspaper import Article

url = 'https://www.latimes.com/opinion/story/2021-01-31/opinion-myanmar-military-coup-outrage'
article = Article(url)
article.download()
article.parse()

# print(article.text)

from nltk.sentiment.vader import SentimentIntensityAnalyzer

paragraph = article.text
score = SentimentIntensityAnalyzer().polarity_scores(paragraph)
# print(score)


# print(stop_words)

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
print(words[:30])