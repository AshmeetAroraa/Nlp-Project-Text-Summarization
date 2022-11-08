


import bs4 as bs
import urllib.request
import re
import nltk





scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Economy_of_Ghana')
article = scraped_data.read()
parsed_article =  bs.BeautifulSoup(article, 'lxml')
paragraphs = parsed_article.find_all('p')
article_text = ""
for p in paragraphs:
    article_text += p.text





article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)
formatted_article = re.sub('[^a-zA-Z]', ' ', article_text)
formatted_article = re.sub(r'\s+', ' ', formatted_article)





tokenize_sentence = nltk.sent_tokenize(article_text)





stopwords = nltk.corpus.stopwords.words('english')
word_frequency = {}
for word in nltk.word_tokenize(formatted_article):
    if word not in stopwords:
        if word not in word_frequency.keys():
            word_frequency[word] = 1
        else: 
            word_frequency[word] += 1





maximum_frequncy = max(word_frequency.values())
for word in word_frequency.keys():
    word_frequency[word] = (word_frequency[word] / maximum_frequncy)





sentence_score = {}
for sent in tokenize_sentence:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequency.keys():
            if len(sent.split(' ')) < 50:
                if sent not in sentence_score.keys():
                    sentence_score[sent] = word_frequency[word]
                else:
                    sentence_score[sent] += word_frequency[word]





import heapq 
sentence_summary = heapq.nlargest(10, sentence_score, key = sentence_score.get)
summary = ' '.join(sentence_summary)
print(summary)






