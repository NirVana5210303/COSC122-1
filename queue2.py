"""Complete the Queue2 class so that it makes use of the head/tail pointers
Make sure you keep the new doctests given below.
"""
import doctest
import os


class Node:
    """A node for a linked list."""
    def __init__(self, initdata):
        self.data = initdata
        self.next_node = None


class Queue2(object):
    """ Implements a Queue using a Linked List with head and tail pointers
    You should be able to copy a lot of your code from your Queue class
    but you will be able to make efficiency gains via the use of a tail pointer
    >>> q = Queue2()
    >>> len(q)
    0
    >>> print(q)
    List for queue is: None
    >>> result = q.dequeue()
    Traceback (most recent call last):
    ...
    IndexError: Can't dequeue from empty queue.
    >>> q.enqueue('a')
    >>> print(q)
    List for queue is: a -> None
    >>> print(q.tail.data)
    a
    >>> print(q.head.data)
    a
    >>> len(q)
    1
    >>> q.dequeue()
    'a'
    >>> len(q)
    0
    >>> q.enqueue('a')
    >>> q.enqueue('b')
    >>> print(q)
    List for queue is: a -> b -> None
    >>> q.enqueue('c')
    >>> print(q)
    List for queue is: a -> b -> c -> None
    >>> len(q)
    3
    >>> q.dequeue()
    'a'
    >>> print(q)
    List for queue is: b -> c -> None
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        """Add an item onto the tail of the queue."""
        # ---start student section---
        self._items.append(item)
        
        pass
        # ===end student section===

    def dequeue(self):
        """Remove an item from the head of the queue and return it.
        If queue is empty you should raise an IndexError as per
        the comment below."""        
        # use the following line to raise error if stack is empty
        # raise IndexError("Can't dequeue from empty queue.")
        # ---start student section---
        if len(self._items) > 0:
            item = self._items.pop(0)
            return item
        else:
            raise IndexError('Can\'t dequeue from an empty queue!')
        # ===end student section===

    def is_empty(self):
        # ---start student section---
        return len(self) == 0
        # ===end student section===

    def __len__(self):
        """ Returns the length --- calling len(q) will invoke this method"""
        # ---start student section---
        return len(self._items)

        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the queue starting 
        from the beginning of the list. Items are separated by -> 
        and ending with -> None
        See doctests in class docstring
        """
        # ---start student section---
        string = ''
        for i, value in(self._items):
            string += 'List for queue is : {} --> \n'.format(i,value)
            return string
        # ===end student section===



if __name__ == '__main__':
    os.environ['TERM'] = 'linux'  # Suppress ^[[?1034h
    # Uncomment the testmod() line to run the tests
    # Can enter an infinite loop if your Stack isn't implemented correctly
    doctest.testmod() 