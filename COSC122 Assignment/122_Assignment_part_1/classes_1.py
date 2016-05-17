class CounterList:
    __n_comparisons__ = 0

    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = data
        self.__n_accesses__ = 0


    def __getitem__(self, i):
        self.__n_accesses__ += 1
        return self.data[i]

    def __setitem__(self, i, item):
        self.__n_accesses__ += 1
        if type(item) != CounterNode:
            raise ValueError("Only Counter objects can be placed in a CounterList")
        else:
            self.data[i] = item

    def __delitem__(self, key):
        self.__n_accesses__ += 1
        del(self.data[key])

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)

    def __contains__(self, item):
        raise TypeError("You can't use the 'in' keyword with a CounterList")

    def __eq__(self, other):
        self.__n_comparisons__ += 1
        return self.data == other

    def insert(self, index, item):
        if type(item) != CounterNode:
            raise ValueError("Only Counter objects can be added to a CounterList")
        else:
            self.data.insert(index, item)

    def index(self, a=None):
        raise TypeError("You can't do that with a CounterList")

    def append(self, item):
        if type(item) != CounterNode:
            raise ValueError("Only Counter objects can be added to a CounterList")
        else:
            self.data.append(item)

    def get_accesses(self):
        return self.__n_accesses__

    @classmethod
    def get_comparisons(cls):
        return cls.__n_comparisons__

    @classmethod
    def reset_comparisons(cls):
        cls.__n_comparisons__ = 0


class MyString:
    '''A wrapped string that counts comparisons of itself
   against strings and delegates all other operations to the
   string itself.'''
    def __init__(self, i):
        self.i = i

    def __eq__(self, j):
        if type(j) != MyString:
            CounterList.__n_comparisons__ += 1
        return self.i == j

    def __le__(self, j):
        if type(j) != MyString:
            CounterList.__n_comparisons__ += 1
        return self.i <= j

    def __ne__(self, j):
        if type(j) != MyString:
            CounterList.__n_comparisons__ += 1
        return self.i != j

    def __lt__(self, j):
        if type(j) != MyString:
            CounterList.__n_comparisons__ += 1
        return self.i < j

    def __gt__(self, j):
        if type(j) != MyString:
            CounterList.__n_comparisons__ += 1
        return self.i > j

    def __ge__(self, j):
        if type(j) != MyString:
            CounterList.__n_comparisons__ += 1
        return self.i >= j

    def __repr__(self):
        return repr(self.i)

    def __getattr__(self, attr):
        '''All other behaviours use self.i'''
        return self.i.__getattr__(attr)


class CounterNode:
    def __init__(self, word, count=1):
        self.word = MyString(word)
        self.count = count

    def __repr__(self):
        return str(self.word) + ": " + str(self.count)







