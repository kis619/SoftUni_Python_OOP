class sequence_repeat:
    def __init__(self, sequence, number: int):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # def check_index(index, end_index):
        #     if index > end_index:
        #         self.index = 0
        #         return 0
        #     return index
        #
        # if self.number == 0:
        #     raise StopIteration
        # i = check_index(self.index, len(self.sequence) - 1)
        # self.index += 1
        # self.number -= 1
        # return self.sequence[i]
        if self.index < self.number:
            i = self.index
            self.index += 1
            return self.sequence[i % len(self.sequence)]

        raise StopIteration
res = sequence_repeat('abc', 7)
for el in res:
    print(el, end='')