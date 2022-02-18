class reverse_iter:
    def __init__(self, iterable):
        self.reversed_iterable = iterable[::-1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.reversed_iterable:
            return self.reversed_iterable.pop(0)
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for i in reversed_list:
    print(i)

