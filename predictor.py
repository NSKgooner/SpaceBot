import pickle


class Predictor():
    def __init__(self, vectorizer_path, model_path):
        self.vectorizer = self.load_vectorizer(vectorizer_path)
        self.model = self.load_model(model_path)

    @staticmethod
    def load_vectorizer(path):
        return pickle.load(open(path, 'r'))

    @staticmethod
    def load_model(path):
        return pickle.load(open(path, 'r'))

    def preprocessing(self, post):
        pass

    def vectorize(self, post):
        return self.vectorizer.transform(post)

    def predict(self, vector):
        return self.model.predict(vector)

    def chainer(self, post):
        post_vectorizer = self.vectorize(self.preprocessing(post))
        return self.predict(post_vectorizer)
