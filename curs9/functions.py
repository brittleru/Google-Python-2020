class MyIterator:
    def __init__(self, max=3):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return self.n
        else:
            raise StopIteration


def iter_sum(data):
    current_sum = 0
    my_iterator = iter(data)

    for n in my_iterator:
        current_sum += n

    return current_sum


def iterators_sum(*args):
    sums = []

    for iter_item in args:
        try:
            sums.append(iter_sum(iter_item))
        except TypeError:
            sums.append(0)

    return sums

# print(iter_sum([1, 2, 3]))
# print(iter_sum((0, 2, 4)))
# print(iter_sum(("a", 2, 4)))

# print(iterators_sum('1', 3, None, False, 99))
# print(iterators_sum('1', 3, [1, 2, 3, 4], (3, 9, 7)))
