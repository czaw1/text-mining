 <h3>1. Project Overview</h3>
For this assignment, I used a Wikipedia article and 3 newspaper articles. I computed summary statistics to find the top 10 words used in the data. Before doing that, I cleaned the data by stripping punctuation, and prepositions from the text to obtain words that are integral to the main topic. I also conducted a sentiment analysis to see if the articles had a more negative tone or positive tone. What I hoped to learn from this was to see the difference in word choice and tone between a Wikipedia article and a news article. In addition, I wanted to compare the attributes mentioned previously among different media outlets such as the LA Times, BBC, and Times.


<h3>2. Implementation</h3>
<p>
In my text mining code, there are 4 main functions. All these functions work quite similarly. To break down the first function analyze_coupwiki, I summarized the article since it was longer than the news articles to understand the focus of the article. Then I cleaned the data so that only words that contribute to the main idea of the article remain. This was done through the code I received from Machine Learning Mastery. I decided to clean the data because, initially when I analyzed the article for its top 10 words used, most of the words were prepositions. I found that for the analysis to be more effective, I would need to process words that were integral to the article. Therefore, I went through the processes of cleaning the data. After cleaning the data, I used the clean data to count the top 10 words used in the article. Thus, I combined the technique to clean the data then to count the data into one function. This is so that I get a more accurate list of top 10 words. To count the top 10 words of the data, I used code from Geeks for Geeks. I used their code because it was very straightforward and efficient. It used pre-existing functions to carry out this analysis. 

In addition, I also ran a sentiment analysis on all of my data. I thought that this analysis was better than a text comparison analysis because I thought that comparing the sentiment analysis would be more insightful than just comparing the similarity of text. The tone gives more insight into how the article aims to pain the coup. A text similarity would be more fitting for testing plagirism so I did not use that analysis.
</p>

<h3> 3. Results </h3>
<h4>Top 10 Words and its Frequency</h4>
<p>
These are the top 10 words used in the Wiki: [('myanmar', 78), ('military', 78), ('february', 56), ('coup', 55), ('aung', 34), ('also', 31), ('government', 26), ('including', 20), ('country', 18), ('state', 18)]

These are the top 10 words used in the LA Times article: [('military', 11), ('country', 6), ('rights', 6), ('suu', 5), ('kyi', 5), ('human', 5), ('us', 4), ('myanmar', 4), ('democracy', 4), ('detained', 4)]

These are the top 10 words used in the BBC article: [('myanmar', 14), ('military', 13), ('coup', 10), ('suu', 10), ('kyi', 10), ('country', 7), ('image', 6), ('aung', 6), ('ms', 6), ('including', 5)]

These are the top 10 words used in the Times article: [('military', 35), ('myanmar', 21), ('country', 14), ('said', 14), ('coup', 13), ('aung', 12), ('suu', 12), ('kyi', 12), ('democratic', 11), ('us', 9)]
</p>
<p>
It is interesting that out of all the data sources, only two have the word ‘democracy’ in their top 10 words used. I would have assumed that all sources’ top 10 words would include democracy since the coup’s main aim is to destroy the democracy in the country. Common words from all data sources are the main people involved who are the military and Aung Sann Suu Kyi which is expected. Another interesting point is that ‘February’ is very high in the list of words for the Wikipedia article and it is not part of any of the other lists. It is interesting to note that Wikipedia focused on the time of the coup. Some errors I see in the lists are, words such as ‘also’, ‘us’, and ‘ms’ were not stripped during the data cleaning.</br>
</p>

<h4>Sentiment Report</h4>
<table>
  <tr>
    <th>Data</th>
    <th>Negative</th>
    <th>Positive</th>
    <th>Neutral</th>
    <th>Compound</th>
  </tr>
  <tr>
    <td>Wikipedia</td>
    <td>0.104</td>
    <td>0.826</td>
    <td>0.07</td>
    <td>-0.9997</td>
  </tr>
  <tr>
    <td>LA Times</td>
    <td>0.158</td>
    <td>0.784</td>
    <td>0.058</td>
    <td>-0.9953</td>
  </tr>
  <tr>
    <td>BBC</td>
    <td>0.123</td>
    <td>0.797</td>
    <td>0.08</td>
    <td>-0.9921</td>
  </tr>
  <tr>
    <td>Times</td>
    <td>0.062</td>
    <td>0.834</td>
    <td>0.104</td>
    <td>0.9976</td>
  </tr>
</table>

 
It is quite interesting to see that the Times article was the most neutral out of all data sources. I would imagine that the Wikipedia article would be the most neutral because it is supposed to be a purely factual page while newspaper articles are usually more opinionated based on the political party that makes up the newspaper company’s audience. The LA times seems to be the article with the most negative words. Though this analysis shows the number of negative words, and etc, I cannot assume that LA times paints a more negative view of the situation than the other sources. There is no relationship between the number of negative words used in an article and how the newspaper article views the situation. However, it does imply that LA times used more words that would provoke a more negative tone. The analysis surprised me in the sense that Wikipedia used more negative words than LA times. Although, the difference is not much.</br>


<h3> 4. Reflection</h3>
As for my process while doing this project, how I went about analyzing the texts is first, I would think of how I’d normally analyze the data manually, and then think of how I could automate it. I also thought of what results and what type of analysis I wanted. I had in mind that I wanted to analyze the differences in reporting the coup among different websites. The coup is quite a controversial topic, and personal, so I was more interested in getting results. From a process point of view, I think that cleaning the data went fairly well. The top 10 words list that resulted after cleaning the data was much more insightful than the one without data cleaning. Though there are some words that could have been stripped, as mentioned in the results section, overall all the top 10 words were important words of the text. There are many ways I could improve the project. Next time I do it, I would find a way to take the sentiment analysis data and put it into a table instead of having to do it manually. In addition, I would like to run an analysis that compares the top 10 words list to see which words overlap and which words do not exist in any of the other lists.
 

