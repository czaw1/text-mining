from mediawiki import MediaWiki
"""
This function analyzes a Wikipedia page and multiple news articles on the coup d'etat that occured in Myanmar.
It analyzes the word choice and sentiment of these data sources.
"""
wikipedia = MediaWiki()
coup = wikipedia.page('2021_Myanmar_coup_d%27état')
print(coup.summary)

#Code from Lines 11 to 30 was botained from the link mentoned below.
#https://machinelearningmastery.com/clean-text-machine-learning-python/
def analyze_coupwiki():

    import nltk
    nltk.download('punkt')
    from nltk.tokenize import word_tokenize 
    tokens = word_tokenize(coup.content)
    # splits words based on white space and punctuation
    # each word is a 'token'
    tokens = [w.lower() for w in tokens]
    #changes all words to lower case
    import string
    #Lines 20 and 21 stips all punctuation
    table = str.maketrans("","", string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    #Line 23 takes away all words that is a nonalphabet word
    words = [word for word in stripped if word.isalpha()]
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    #Line 28 takes away words that do not contribute deeper meaning to the phrase.
    stop_words = stopwords.words('english')
    words = [w for w in words if not w in stop_words]

    from collections import Counter
    Counter = Counter(words)
    most_occur_coupwiki = Counter.most_common(10)
    print(most_occur_coupwiki)

if __name__ == "__main__":
    analyze_coupwiki()