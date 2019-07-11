import numpy as np


class Generator:
    def __init__(self, path='/home/alexkryu4kov/mysite/speeches.txt'):
        self.path = path
        self.text = self.load_text()
        self.corpus = self.make_corpus()

    def load_text(self):
        with open(self.path, 'r') as f:
            return f.read()

    def make_corpus(self):
        return self.text.split()

    def make_pairs(self):
        for i in range(len(self.corpus) - 1):
            yield (self.corpus[i], self.corpus[i+1])

    def generate_dict(self):
        self.word_dict = {}
        pairs = self.make_pairs()
        for word_1, word_2 in pairs:
            if word_1 in self.word_dict.keys():
                self.word_dict[word_1].append(word_2)
            else:
                self.word_dict[word_1] = [word_2]

    def make_chain(self):
        first_word = np.random.choice(self.corpus)
        chain = [first_word]
        n_words = 30
        self.generate_dict()
        for i in range(n_words):
            chain.append(np.random.choice(self.word_dict[chain[-1]]))
        return ' '.join(chain)
