class CounterLinkedList:
    __n_comparisons__ = 0

    def __init__(self, head=None):
        self.head = head
        self.__n_accesses__ = 0

    def __repr__(self):
        node = self.head
        string = str(node)
        while node.next_node:
            string += " -> " + str(node.next_node)
            node = node.next_node
        string = "[" + string + "]"
        return string

    def __contains__(self, item):
        raise TypeError("You can't use the 'in' keyword with a CounterLinkedList")

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
            CounterLinkedList.__n_comparisons__ += 1
        return self.i == j

    def __le__(self, j):
        if type(j) != MyString:
            CounterLinkedList.__n_comparisons__ += 1
        return self.i <= j

    def __ne__(self, j):
        if type(j) != MyString:
            CounterLinkedList.__n_comparisons__ += 1
        return self.i != j

    def __lt__(self, j):
        if type(j) != MyString:
            CounterLinkedList.__n_comparisons__ += 1
        return self.i < j

    def __gt__(self, j):
        if type(j) != MyString:
            CounterLinkedList.__n_comparisons__ += 1
        return self.i > j

    def __ge__(self, j):
        if type(j) != MyString:
            CounterLinkedList.__n_comparisons__ += 1
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
        self.next_node = None

    def __repr__(self):
        return str(self.word) + ": " + str(self.count)


def _c_mul(a, b):
    """Substitute for c multiply function"""
    return ((int(a) * int(b)) & 0xFFFFFFFF)


def nice_hash(input_string):
    """Takes a string name and returns a hash for the string. This hash value
    will be os independent, unlike the default Python hash function."""
    if input_string is None:
        return 0  # empty
    value = ord(input_string[0]) << 7
    for char in input_string:
        value = _c_mul(1000003, value) ^ ord(char)
    value = value ^ len(input_string)
    if value == -1:
        value = -2
    return value


def hash_word(item, slots):
    return nice_hash(item) % slots