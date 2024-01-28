import csv
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer


def load_data(fpath):
    # map ham -> 0, spam -> 1
    cat_map = {"ham": 0, "spam": 1}
    tfidf = TfidfVectorizer()
    msgs, y = [], []
    filein = open(fpath, "r")
    reader = csv.reader(filein)
    for i, line in enumerate(reader):
        if i == 0:
            # skip over the header
            continue
        cat, msg = line
        y.append(cat_map[cat])
        msg = msg.strip()  # remove newlines
        msgs.append(msg)
    X = tfidf.fit_transform(msgs)
    return X, y, tfidf


def featurize(text, tfidf):
    features = tfidf.transform(text)
    return features


def train(X, y, model):
    model.fit(X, y)
    return model


def predict(X, model):
    return model.predict(X)


clf = LogisticRegression()
X, y, tfidf = load_data("spamorham.csv")
train(X, y, clf)
