import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from sklearn.metrics import accuracy_score
import pickle

stopWords = set(nltk.corpus.stopwords.words('nepali'))
# vect = TfidfVectorizer(tokenizer= lambda x: x.split(" "),
#                                   sublinear_tf=True, encoding='utf-8',
#                                   decode_error='ignore',
#                                   max_df=0.5,
#                                   min_df=10,
#                                   stop_words=stopWords)

vect = TfidfVectorizer(sublinear_tf=True, encoding='utf-8',
                                 decode_error='ignore',stop_words=stopWords)

output_dict = {
    0:"auto",
    1:"bank",
    2:"blog",
    3:"business",
    4:"economy",
    5:"education",
    6:"employment",
    7:"entertainment",
    8:"interview",
    9:"literature",
    10:"national_news",
    11: "opinion",
    12:"sports",
    13: "technology",
    14: "tourism",
    15: "world"
}


trainNews = pd.read_csv("./data/train.csv")
testNews = pd.read_csv("./data/test.csv")
xTrain = trainNews['text']
yTrain = trainNews['label']

tfidf = vect.fit(xTrain.values.astype('U'))
xTrainvect = vect.fit_transform(xTrain)
yTrainvect = yTrain
xTestvect = vect.transform(testNews['text'])
yTestvect = testNews['label']

model = MultinomialNB(alpha=0.01, fit_prior=True)
model.fit(xTrainvect, yTrainvect)

ypred = model.predict(xTestvect)
score = accuracy_score(yTestvect, ypred)
print ("Accuracy: ",score)
pickle.dump(model, open("/Nepali-NLP/Nepali-News-Classification/models/news_classifier_model.pickle", 'wb'))
pickle.dump(tfidf, open("/Nepali-NLP/Nepali-News-Classification/models/news_vectorizer.pickle", "wb"))
####TEST#####
test = "नेपालको छवि विगतको तुलनामा उच्च : मन्त्री ज्ञवाली"
yPred = model.predict(vect.transform([test]))
print ("OUTPUT: ", output_dict[int(yPred)])