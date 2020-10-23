import pickle


class LoadModel:
    def __init__(self, path: str):
        self.path = path
        self.model = None

    def load(self):
        try:
            with open(self.path, 'rb') as file:
                self.model = pickle.load(file)
        except FileNotFoundError:
            raise FileNotFoundError('File not found')

        return self.model
