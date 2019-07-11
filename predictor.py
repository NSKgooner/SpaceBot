import pickle


class Predictor:
    def __init__(self, vectorizer_path="/home/alexkryu4kov/mysite/data/tfidf_vec.pkl", model_path="/home/alexkryu4kov/mysite/data/model.pkl"):
        self.vectorizer = self.load_vectorizer(vectorizer_path)
        self.model = self.load_model(model_path)

    @staticmethod
    def load_vectorizer(path):
        return pickle.load(open(path, 'rb'))

    @staticmethod
    def load_model(path):
        return pickle.load(open(path, 'rb'))

    def preprocessing(self, post):
        return post

    def vectorize(self, post):
        return self.vectorizer.transform(post)

    def predict(self, vector):
        return self.model.predict(vector)

    def chainer(self, post):
        post_vectorizer = self.vectorize(self.preprocessing(post))
        return self.predict(post_vectorizer)
