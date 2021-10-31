def main():
    """
    This function analyzes a Wikipedia page and multiple news articles on the coup d'etat that occured in Myanmar.
    It analyzes the word choice and sentiment of these data sources.
    It shows the results from the analysis of these data sources.
    """
    from coup_wiki import analyze_coupwiki
    analyze_coupwiki()
    from latimes_article import analyze_latimes
    analyze_latimes()
    from bbc_article import analyze_bbc
    analyze_bbc()
    from times_article import analyze_times
    analyze_times()


if __name__ == "__main__":
    main()