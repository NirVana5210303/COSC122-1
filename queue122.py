""" Note we have called this module queue122.py so as to avoid a clash with the 
inbuilt module called queue. 
"""
import doctest
import os
   
    
class Queue(object):
    """Implements a Queue using a Python list.
    Internally the queue is stored as plain Python list.
    The front of the queue is at list[0] and rear is at list[n]
    _items is a private variable inside each queue instance and shouldn't 
    be accessed from outside the queue (eg, don't do q._items.dequeue(), you should
    be using q.dequeue()
    >>> q = Queue()
    >>> q.enqueue('a')
    >>> q.dequeue()
    'a'
    >>> q.enqueue('a')
    >>> q.enqueue('b')
    >>> len(q)
    2
    >>> q.dequeue()
    'a'
    >>> len(q)
    1
    >>> q.dequeue()
    'b'
    >>> q.dequeue()
    Traceback (most recent call last):
    ...
    IndexError: Can't dequeue from an empty queue!
    """
    
    def __init__(self):
        self._items = []
        
    def enqueue(self, item):
        """Add an item onto the rear of the queue."""
        # ---start student section---
        self._items.append(item)
        pass
        # ===end student section===
    
    def dequeue(self):
        """Remove an item from the front of the queue and return it.
        Raise IndexError if empty, see comment below."""
        # ---start student section---
        if len(self._items) > 0:
            item = self._items.pop(0)
            return item
        else:
        # ===end student section===
        # raise an index error if list is empty, eg,
            raise IndexError('Can\'t dequeue from an empty queue!')
    
    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return "Front -> " + repr(self._items) + " <- Rear"
    

   
    
if __name__ == '__main__':
    # uncomment the following line if you have problems with strange characters
    # os.environ['TERM'] = 'linux' # Suppress ^[[?1034h
    
    # failed doctests will show you what you need to fix/write
    # If everything works then the doctests will output nothing...
    doctest.testmod()
    
