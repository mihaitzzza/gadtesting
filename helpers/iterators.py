class MyIterator:
    def __init__(self, n, init_value):
        self.n = n
        self.init_value = init_value

    @property
    def numbers(self):
        return self.n

    @property
    def first_value(self):
        return self.init_value

    def __iter__(self):
        self.value = self.init_value
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.n:
            current_value = self.value
            self.value **= 2
            self.i += 1

            return current_value

        raise StopIteration
