import re
import string

exclude = set(string.punctuation)

def pre_pro(text):
    """
    cleaning the text
    """
    text = text.lower()
    text = re.sub( '\s+', ' ', text ).strip()
    text = re.sub( '&\w*;', ' ', text ) #eg: &nbsp;
    text = re.sub( '#\d+;', ' ', text ) #eg: #1223;
    text = re.sub( '&#\d+;', ' ', text ) #eg: &#fffee;
    text = re.sub( '<\w.*>', ' ', text ) #eg: <html>
    text = ''.join(ch for ch in text if ch not in exclude)
    return text


def jaccard(set_a, set_b):
    """
    calculate the distance between two text
    Jaccard Similairty: J(a,b) = |A ∩ B|/|A ∪ B|.
    """
    intersection = set_a & set_b
    union = set_a | set_b
    if len(union) > 0:
        return len(intersection) / len(union)
    else:
        return 0

def text_similarity(text1,text2):
    text1_set = set([x for x in text1.lower().split()])
    text2_set = set([x for x in text2.lower().split()])
    jaccard_similarity = jaccard(text1_set, text2_set)
    return int(jaccard_similarity*100)

text1 = """ मलाई स्याउ खान मन छ । एप्पल स्वास्थ्य को लागी धेरै राम्रो छ"""
text2 = """मलाई धेरै नै स्याउ खान मन पर्छ । एप्पल स्वास्थ्य को लागी धेरै राम्रो छ"""

sim_score = text_similarity(text1,text2)
print ("The two documents are "+str(sim_score)+"% similar")
