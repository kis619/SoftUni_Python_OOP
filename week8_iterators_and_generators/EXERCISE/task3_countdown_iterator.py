class countdown_iterator:
    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 0:
            raise StopIteration

        curr_number = self.count
        self.count -= 1
        return curr_number

iterator = countdown_iterator(10)
for num in iterator:
    print(num)