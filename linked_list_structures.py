'''Data structures implemented with linked lists.'''
import doctest
import os

class Node:
    '''A node for a linked list.'''
    def __init__(self, initdata):
        self.data = initdata
        self.next_node = None

class Stack (object):
    """ Implements a Stack using a Linked List"
    >>> s = Stack()
    >>> print(s)
    List for stack is: None
    >>> result = s.pop()
    Traceback (most recent call last):
    ...
    IndexError: Can't pop from empty stack.
    >>> s.push('a')
    >>> print(s)
    List for stack is: a -> None
    >>> len(s)
    1
    >>> s.pop()
    'a'
    >>> print(s)
    List for stack is: None
    >>> s.push('b')
    >>> print(s)
    List for stack is: b -> None
    >>> s.push('c')
    >>> print(s)
    List for stack is: c -> b -> None
    >>> len(s)
    2
    >>> s.peek()
    'c'
    >>> print(s)
    List for stack is: c -> b -> None
    >>> s.pop()
    'c'
    >>> print(s)
    List for stack is: b -> None
    """

    def __init__(self):
        self.head = None
        self.data = []
        self.tail = None

    def push(self, item):
        """push a new item on to the stack"""
        # ---start student section---
        self.data.append(item)
        # ===end student section===

    def pop(self):
        """pop an item off the top of the stack, and return it
        If stack is empty you should raise an IndexError as per
        the comment below."""
        # use the following line to raise error when stack is empty
        # raise IndexError("Can't pop from empty stack.")
        # ---start student section---
        if len(self.data) > 0:
            item = self.data.pop()
            return item
        else:
        # ===end student section===
        # raise an index error if list is empty, eg,
            raise IndexError('Can\'t pop from empty stack.')
        

    def peek(self):
        """pop an item on the top of the top of the stack, but don't remove it"""
        # ---start student section---
        return self.data[-1]
        # ===end student section===

    def isEmpty(self):
        return self.head is None

    def __len__(self):
        """ Returns the length --- calling len(s) will invoke this method """
        # ---start student section---
        return len(self.data)
        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the stack starting 
        from the beginning of the list. Items are separated by -> 
        and ending with -> None
        See doctests in class docstring
        """
        # ---start student section---
        string = ''
    

        # ===end student section===




class Queue (object):
    """ Implements a Queue using a Linked List"
    >>> q = Queue()
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
    >>> len(q)
    1
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
        self.data = []
        self.tail = None

    def enqueue(self, item):
        """Add an item onto the tail of the queue."""
        # ---start student section---
        self.data.append(item)
        # ===end student section===

    def dequeue(self):
        """Remove an item from the head of the queue and return it.
        If queue is empty you should raise an IndexError as per
        the comment below."""        
        # use the following line to raise error when queue is empty
        # raise IndexError("Can't dequeue from empty queue.")        
        # ---start student section---
        if len(self.data) > 0:
            item = self.data.pop(0)
            return item
        else:
        # ===end student section===
        # raise an index error if list is empty, eg,
            raise IndexError('Can\'t dequeue from empty queue.')
        # ===end student section===

    def isEmpty(self):
        # ---start student section---
        return len(self) == 0
        # ===end student section===

    def __len__(self):
        """ Returns the length --- calling len(q) will invoke this method """
        # ---start student section---
        return len(self.data)
        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the queue starting 
        from the beginning of the list. Items are separated by -> 
        and ending with -> None
        See doctests in class docstring
        """
        # ---start student section---
        string = ''
        while self.head != None:
            self.getnext(item)
            print("List for queue is: {} -> {} -> None".format(item))

        # ===end student section===


if __name__ == '__main__':
    os.environ['TERM'] = 'linux'  # Suppress ^[[?1034h
    # Uncomment the testmod() line to run the tests
    # Can enter an infinite loop if your Stack isn't implemented correctly
    doctest.testmod() 