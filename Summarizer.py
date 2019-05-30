import bs4 as bs  
import urllib.request  
import re
import heapq 
import nltk
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('stopwords')
from nltk.corpus import stopwords  # for removeStopWords(text)

class TextSummarizer():
    def __init__(self,content):
        self.setSentenceList(content)
        self.setStopwords()
        self.cleanseText(content)
        self.calcWordFreq(self.getCleansedText())
        self.calcSentFreq(self.getSentenceList())
    
    def setSentenceList(self, article_text):
        self.sentence_list = nltk.sent_tokenize(article_text)
        
    def getSentenceList(self):
        return self.sentence_list
    
    def setStopwords(self):
        self.stopwords = nltk.corpus.stopwords.words('english')
        
    def getStopwords(self):
        return self.stopwords
    
    def cleanseText(self, article_text):
        # Removing Square Brackets and Extra Spaces
        self.article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
        self.article_text = re.sub(r'\s+', ' ', article_text)
        # Removing special characters and digits
        self.formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
        self.formatted_article_text = re.sub(r'\s+', ' ', self.formatted_article_text)
    
    def getCleansedText(self):
        return self.formatted_article_text
    
    def calcWordFreq(self, formatted_article_text):
        try:
            self.word_frequencies = {}
            for word in nltk.word_tokenize(formatted_article_text):  
                if word not in self.getStopwords():
                    if word not in self.word_frequencies.keys():
                        self.word_frequencies[word] = 1
                    else:
                        self.word_frequencies[word] += 1
            self.maximum_frequncy = max(self.word_frequencies.values())
            for word in self.word_frequencies.keys():  
                self.word_frequencies[word] = (self.word_frequencies[word]/self.maximum_frequncy)
        except ValueError:
            pass
            
    def getWordFreq(self):
        return self.word_frequencies
            
    def calcSentFreq(self, sentence_list):
        self.sentence_scores = {}
        for sent in sentence_list:  
            for word in nltk.word_tokenize(sent.lower()):
                if word in self.getWordFreq().keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in self.sentence_scores.keys():
                            self.sentence_scores[sent] = self.getWordFreq()[word]
                        else:
                            self.sentence_scores[sent] += self.getWordFreq()[word]
                            
    def getSentFreq(self):
        return self.sentence_scores
                            
    def getSummary(self, num_of_sent):
        self.summary_sentences = heapq.nlargest(num_of_sent, self.getSentFreq(), key=self.getSentFreq().get)
        #self.summary = '\n'.join(self.summary_sentences)  
        return self.summary_sentences
    
#a = TextSummarizer('https://www.ontario.ca/laws/about-e-laws#ccl')

#print (a.getSummary(5))