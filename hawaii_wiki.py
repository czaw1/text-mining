from mediawiki import MediaWiki

wikipedia = MediaWiki()
coup = wikipedia.page('2021_Myanmar_coup_d%27état')
# print(hawaii.title)
# print(hawaii.content)
print(coup.summary)

# print(f'these are the categories of the wiki page:{hawaii.categories}')

# word_bank = hawaii.content.split()
# d = {}
# for word in word_bank:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
# print(d)
"""
https://www.geeksforgeeks.org/find-k-frequent-words-data-set-python/
"""

from collections import Counter
# split() returns list of all the words in the string
split_it = coup.content.split()


# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)
  
# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(50)
  
# print(most_occur)

# Natural Language Processor
from nltk.sentiment.vader import SentimentIntensityAnalyzer

paragraph = coup.content
score = SentimentIntensityAnalyzer().polarity_scores(paragraph)
print(score)


# hawaii.content.split()
# hawaii.content.lower()
# print(hawaii.content)

# if __name__ == "__main__":
#     main() DO NOT FORGET TO DO THIS

# print(coup.content)

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
tokens = word_tokenize(coup.content)
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
print(words[:10])