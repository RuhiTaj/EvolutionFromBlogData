#https://medium.com/@acrosson/extract-subject-matter-of-documents-using-nlp-e284c1c61824

#download article

import requests

url = 'http://techcrunch.com/2016/05/26/snapchat-series-f/'
r = requests.get(url)


# pass the document to BeautifulSoup to parse out the body and title

from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, 'html.parser')
title = soup.find('title').get_text()
document = ' '.join([p.get_text() for p in soup.find_all('p')])

# (pre-processing)-remove any characters which weren’t alpha numeric but kept few punctuation marks

document = re.sub(‘[^A-Za-z .-]+’, ‘ ‘, document)
document = ‘ ‘.join(document.split())
document = ‘ ‘.join([i for i in document.split() if i not in stop])

#tokenise and extract most frequent words

words = nltk.tokenize.word_tokenize(document)
words = [word.lower() for word in words if word not in stop]
fdist = nltk.FreqDist(words)
most_freq_nouns = [w for w, c in fdist.most_common(10)
                   if nltk.pos_tag([w])[0][1] in NOUNS]

#the most related ones by taking the intersection of named entities and the most frequently mentioned nouns

subject_nouns = [entity for entity in top_10_entities
                 if entity.split()[0] in most_freq_nouns]

#take our tokenized sentences and run them through a n-gram tagging model

train_sents = nltk.corpus.brown.tagged_sents()
train_sents += nltk.corpus.conll2000.tagged_sents()
train_sents += nltk.corpus.treebank.tagged_sents()

# Create instance of SubjectTrigramTagger
trigram_tagger = SubjectTrigramTagger(train_sents)







