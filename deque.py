import doctest
import os

   
    
class Deque(object):
    """
    Implements a Deque using a Python list internally.
    >>> d = Deque()
    >>> d.enqueue_front('a')
    >>> d.dequeue_front()
    'a'
    >>> d.enqueue_front('a')
    >>> d.enqueue_rear('b')
    >>> len(d)
    2
    >>> d.dequeue_rear()
    'b'
    >>> len(d)
    1
    """
    def __init__(self):
        self._items = []
        
    def enqueue_front(self, item):
        """Add an item onto the front of the queue."""
        self._items.insert(0,item)
    
    def enqueue_rear(self, item):
        """Add an item onto the rear of the queue."""
        self._items.append(item)
        
    def dequeue_front(self):
        """Remove an item from the front of the queue and return it."""
        if not self.is_empty():
            return self._items.pop(0)
        else:
            raise IndexError('Can\'t dequeue_front from an empty deque!')

    def dequeue_rear(self):
        """Remove an item from the rear of the queue and return it."""
        if not self.is_empty():
            return self._items.pop()
        else:
            raise IndexError('Can\'t dequeue_rear from an empty deque!')
    
    def is_empty(self):
        """ Returns True if the deque is empty."""
        return len(self) == 0

    def __len__(self):
        """ Returns the number of items in the deque."""
        return len(self._items)
    
    def __repr__(self):
        """ Returns a string representing the deque."""
        return "Front -> " + repr(self._items) + " <- Rear"
    
    
   
    
if __name__ == '__main__':
    # uncomment the following line if you have problems with strange characters
    # os.environ['TERM'] = 'linux' # Suppress ^[[?1034h
    
    # failed doctests will show you what you need to fix/write
    # If everything works then the doctests will output nothing...
    doctest.testmod()
