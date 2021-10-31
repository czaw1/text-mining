from mediawiki import MediaWiki
wikipedia = MediaWiki()
coup = wikipedia.page('2021_Myanmar_coup_d%27état')


"""
This function analyzes a Wikipedia page on the coup d'etat that occured in Myanmar.
It analyzes the word choice and sentiment of these data sources.
"""
wikipedia = MediaWiki()
coup = wikipedia.page('2021_Myanmar_coup_d%27état')


#Code from Lines 11 to 30 was botained from the link mentoned below.
#https://machinelearningmastery.com/clean-text-machine-learning-python/
def analyze_coupwiki():
    print(f'SUMMARY:{coup.summary}')
    print('')
    import nltk
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
    from nltk.corpus import stopwords
    #Line 28 takes away words that do not contribute deeper meaning to the phrase.
    stop_words = stopwords.words('english')
    words = [w for w in words if not w in stop_words]

    """
    Function counting top 10 words received from https://www.geeksforgeeks.org/find-k-frequent-words-data-set-python/
    """
    from collections import Counter
    Counter = Counter(words) #adds clean data into a counter to count top 10 words used
    most_occur_coupwiki = Counter.most_common(10)
    print(f'These are the top 10 words used in the Wiki: {most_occur_coupwiki}')
    print(f'')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    paragraph = coup.content
    score = SentimentIntensityAnalyzer().polarity_scores(paragraph)
    print(f'This is the sentiment report of the Wiki: {score}')