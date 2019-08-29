import nltk
import pickle

stopWords = set(nltk.corpus.stopwords.words('nepali'))


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

"""
Load the trained model and vectorizer pickle
"""

model = pickle.load(open("Nepali-NLP/Nepali-News-Classification/models/news_classifier_model.pickle", 'rb'))
vectorizer = pickle.load( open("+-*9-+-----+"
                               "+"
                               "Nepali-NLP/Nepali-News-Classification/models/news_vectorizer.pickle", "rb"))

"""
predict the classes for the text
"""
test = "नेपालको छवि विगतको तुलनामा उच्च : मन्त्री ज्ञवाली"
yPred = model.predict(vectorizer.transform([test]))
print ("OUTPUT: ", output_dict[int(yPred)])