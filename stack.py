import doctest
import os
    
    
class Stack(object):
    """Provides a stack with associated stack opertations.
    Internally the stack is stored as plain Python list.
    The top of the stack is at _items[n] and the bottom is at _items[0]
    _items is a private variable inside each stack instance and shouldn't 
    be accessed from outside the stack (eg, don't do s._items.pop(), you should
    be using s.pop()

    >>> s = Stack()
    >>> s.push('a')
    >>> s.peek()
    'a'
    >>> s.pop()
    'a'
    >>> s.push('a')
    >>> s.push('b')
    >>> s.peek()
    'b'
    >>> len(s)
    2
    >>> s.pop()
    'b'
    >>> len(s)
    1
    >>> s.pop()
    'a'
    >>> s.pop()
    Traceback (most recent call last):
    ...
    IndexError: Can't pop from empty stack!
    """
    
    def __init__(self):
        self._items = []
        
    def push(self, item):
        """Push a new item onto the stack."""
        # ---start student section---
        self._items.append(item)
        pass
        # ===end student section===
    
    def pop(self):
        """Pop an item off the top of the stack and return it.
        Raise IndexError if empty - see comments below."""
        # ---start student section---
        if len(self._items) > 0:
            dog = self._items.pop()
            return dog
        else:
    
        # ===end student section===
        # Raise IndexError if empty, eg,
            raise IndexError('Can\'t pop from empty stack!')
    
    def peek(self):
        """Return the item on the top of the stack, but don't remove it.
        Returns None if the list is empty"""
        # ---start student section---
        return self._items[-1]
        # ===end student section===
    
    def is_empty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return "Bottom -> " + repr(self._items) + " <- Top"

   
    
if __name__ == '__main__':
    # uncomment the following line if you have problems with strange characters
    # os.environ['TERM'] = 'linux' # Suppress ^[[?1034h
    
    # failed doctests will show you what you need to fix/write
    # If everything works then the doctests will output nothing...
    doctest.testmod()
    
