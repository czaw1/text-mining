from newspaper import Article

url = 'https://www.bbc.com/news/world-asia-55902070'
article = Article(url)
article.download()
article.parse()

def analyze_bbc():
    """
    This function analyzes a BBC article on the coup d'etat that occured in Myanmar.
    It analyzes the word choice and sentiment of these data sources.
    """
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

    from collections import Counter
    Counter = Counter(words)
    most_occur_bbc = Counter.most_common(10)
    print(f'These are the top 10 words used in the Wiki: {most_occur_bbc}')
    print(f'')

    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    paragraph = article.text
    score = SentimentIntensityAnalyzer().polarity_scores(paragraph)
    print(f'This is the sentiment report of the Wiki: {score}')