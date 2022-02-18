class take_skip:
    def __init__(self, step: int, count: int):
        self.number = 0
        self.step = step
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        self.count -= 1
        curr_num = self.number
        self.number += self.step
        return curr_num


k = take_skip(10, 5)
for el in k:
    print(el)
