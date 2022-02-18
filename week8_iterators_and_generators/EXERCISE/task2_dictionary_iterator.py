class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary

    def __iter__(self):
        return self

    def __next__(self):
        if not self.dictionary:
            raise StopIteration
        for key, value in self.dictionary.items():
            del self.dictionary[key]
            return key, value


ricky = dictionary_iter({1: '1', 2: '2'})
for x in ricky:
    print(x)

