"""FrequencyList classes and testing routines.
Work through the lab handout to find out what you are doing..."""


import time
import re
from unicodedata import category
import doctest
import os

#-------------------------------------------------------------------------
class FreqNode(object):

    """
    Stores an item, frequency pair.

    Basically a FreqNode object is a node in the frequency list.
    Each FreqNode holds an item, the frequency for the item,
    and a pointer to the next FreqNode object (or None).

    >>> f = FreqNode('c', 2)
    >>> f.item
    'c'
    >>> f.frequency
    2
    >>> print(f)
    'c' = 2
    """

    def __init__(self, item, frequency=1):
        self.item = item
        self.frequency = frequency
        self.next_node = None

    def increment(self):
        self.frequency += 1

    def __str__(self):
        return "\'{0}\' = {1:d}".format(self.item, self.frequency)


#-------------------------------------------------------------------------
class FreqList(object):

    """Stores a linked list of FreqNode objects.
    NOTE: This is a parent class for Unsorted, NicerUnSorted & Sorted FreqLists
    """

    def __init__(self):
        self.head = None

    def add(self, item):
        """Will be implemented by child classes. Don't write anything here.
        There is will add an item with frequency=1 if item not in list,
        otherwise it will increment the frequency count for the item.
        """
        pass

    def get_item_frequency(self, item):
        """Returns Frequency of item, if found else returns 0.
        NOTE: Don't use this when writing your add methods.
        That is, you should scan through the list directly when adding.
        Using this method to check for existence of an item will be
        very inefficient... think about why.
        """

        # ---start student section---
        count = 0
        for i in range(0,item):
            if i == item:
                count+=1
             else:   
            
        # ===end student section===

    def get_xy_for_plot(self):
        x = []
        y = []
        curr_item = self.head
        while not curr_item is None:
            x.append(curr_item.item)
            y.append(curr_item.frequency)
            curr_item = curr_item.next_node
        return x, y

    def _get_index_width(self):
        length = self.__len__()
        max_power_of_ten = 1
        divisor = 10
        while length // divisor > 0:
            divisor *= 10
            max_power_of_ten += 1
        return max_power_of_ten + 2
        

    def __str__(self):
        """Returns the items together with their letter frequencies."""
        item_strs = []
        current = self.head
        node_num = 1
        index_width = self._get_index_width()
        while not current is None:
            line_str = '{:>{width}}:  {}'.format(node_num, 
                                                 str(current),
                                                 width=index_width)
            item_strs.append(line_str)
            current = current.next_node
            node_num += 1
        return '\n'.join(item_strs)

    def __len__(self):
        """Returns the number of nodes in the freq. list. Zero if empty."""
        current = self.head
        length = 0
        while not current is None:
            length += 1
            current = current.next_node
        return length


#-------------------------------------------------------------------------
class UnsortedFreqList(FreqList):

    """FreqList that adds new items to the front of the list"""

    def add(self, new_item):
        """
        Adds the given `letter` with a frequency of 1 as a FreqNode object
        to the list. If the given `letter` is already in the list, the frequency
        is incremented by 1. If not in the list then the item is added at start

        >>> f = UnsortedFreqList()
        >>> f.add('a')
        >>> print(f)
          1:  'a' = 1
        >>> f.add('b')
        >>> print(f)
          1:  'b' = 1
          2:  'a' = 1
        >>> f.add('a')
        >>> print(f)
          1:  'b' = 1
          2:  'a' = 2
        """
        # ---start student section---
        pass
        # ===end student section===


#-------------------------------------------------------------------------
class NicerUnsortedFreqList(FreqList):

    """FreqList that adds new items at the end of the list"""

    def add(self, new_item):
        """
        If the given `letter` is already in the list, the frequency is
        incremented by 1.  If not in list, the item is added to the end of the
        list with a frequency of 1.

        >>> f = NicerUnsortedFreqList()
        >>> f.add('a')
        >>> print(f)
          1:  'a' = 1
        >>> f.add('b')
        >>> print(f)
          1:  'a' = 1
          2:  'b' = 1
        >>> f.add('a')
        >>> print(f)
          1:  'a' = 2
          2:  'b' = 1
        """
        # ---start student section---
        pass
        # ===end student section===


#-------------------------------------------------------------------------
class SortedFreqList(FreqList):

    """FreqList that keeps items in order, sorted by their frequencies"""

    def _insert_in_order(self, freq_node):
        """ Takes a FreqNode and inserts in to the list so that
        items are sorted from largest to smallest 
        """
        # so we don't have to lookup each time
        freq_of_item = freq_node.frequency

        # check to see if larger than first freq in list
        if freq_of_item > self.head.frequency:
            freq_node.next_node = self.head
            self.head = freq_node
        else:
            curr_freq = self.head
            inserted = False
            while (curr_freq.next_node is not None) and not(inserted):
                if freq_of_item > curr_freq.next_node.frequency:
                    # insert here
                    freq_node.next_node = curr_freq.next_node
                    curr_freq.next_node = freq_node
                    inserted = True
                else:
                    curr_freq = curr_freq.next_node
            # got to end and didn't find
            if not inserted:
                freq_node.next_node = None  # as now at end of list
                curr_freq.next_node = freq_node

    def add(self, new_item):
        """
        If the list is empty then make a new FreqNode and insert it at head.
        If the given `letter` is already in the list, the frequency
        is incremented by 1. 
        If needed, the node is removed and then inserted 
        in to its sorted position - using _insert_in_order.
        If not already in freq list then adds the given `letter` with a 
        frequency of 1 as a FreqNode object to the end of the list.

        >>> f = SortedFreqList()
        >>> f.add('a')
        >>> print(f)
          1:  'a' = 1
        >>> f.add('b')
        >>> print(f)
          1:  'a' = 1
          2:  'b' = 1
        >>> f.add('b')
        >>> print(f)
          1:  'b' = 2
          2:  'a' = 1
        >>> f.add('a')
        >>> print(f)
          1:  'b' = 2
          2:  'a' = 2
        >>> f.add('a')
        >>> print(f)
          1:  'a' = 3
          2:  'b' = 2
        """
        # ---start student section---
        pass
        # ===end student section===

#-------------------------------------------------------------------------
# End of Class definitions
#=========================================================================


def time_freq_build(freq_list_class, doc, n_chars):
    """Calculate the letter frequencies using the supplied freq_list_class and
    document (in the form of a sting called doc).
    Returns a freq_list and the time_taken in seconds.
    """
    # create a new freq_list instance of the given class
    freq_list = freq_list_class()
    if n_chars == 1:
        # do a simple scan for single characters
        start = time.perf_counter()
        for char in doc:
            freq_list.add(char)
        end = time.perf_counter()
    elif n_chars > 1:
        # do a scan for given multiples of characters
        start = time.perf_counter()
        for i in range(0, len(doc) - n_chars):
            chars = doc[i:i + n_chars]
            freq_list.add(chars) 
        end = time.perf_counter()
    else:
        raise ValueError("Number of characters must be a positive integer")
    time_taken = end - start
    return freq_list, time_taken


def plot_freq_list(freq_list):
    """ Plots a bar chart showing item frequency.
    Will take any of the various freq_list classes, eg, unsorted, sorted etc
    """
    from matplotlib import pyplot
    (x, y) = freq_list.get_xy_for_plot()
    item_list_nums = list(range(len(x)))
    width = 0.8
    pyplot.bar(item_list_nums, y, width)
    pyplot.title("Frequency Distribution")
    pyplot.xlabel('Item')
    tick_positions = [i + width / 2 for i in item_list_nums]
    pyplot.xticks(tick_positions, x)
    pyplot.ylabel('Frequencies')
    pyplot.draw()
    pyplot.show()


def plot_truncated_freq_list(freq_list, n=26):
    """Plots a bar chart showing item frequency for the top n items.
    Will take any of the various freq_list classes, eg, unsorted, sorted etc
    """
    from matplotlib import pyplot
    (raw_x, raw_y) = freq_list.get_xy_for_plot()
    # only use the first n items
    x = raw_x[:n]
    y = raw_y[:n]

    # show with ' marks so spaces can be seen
    if len(x[0]) > 1:
        x = [repr(item) for item in x]

    item_list_nums = list(range(len(x)))
    width = 0.8
    pyplot.bar(item_list_nums, y, width)
    pyplot.title("Frequency Distribution (top " + str(n) + " items)")
    pyplot.xlabel('Item')
    tick_positions = [i + width / 2 for i in item_list_nums]
    pyplot.xticks(tick_positions, x)
    pyplot.ylabel('Frequencies')
    pyplot.draw()
    pyplot.show()



def print_test_header(filename, doc):
    """Does what it says."""
    print('\n' * 2)
    print('-' * 60)
    print('Tests for: ' + filename)
    print('Doc size:  {} chars'.format(len(doc)))
    print('-' * 60)





def run_a_test(doc, freq_class, n_chars, verbose=True):
    """Calls the freq_list builder for the given doc and n_chars.
    Times how long it takes and prints the time taken.
    If verbose == True then prints out the resulting freq list.
    """

    freq_list, total_time = time_freq_build(freq_class, doc, n_chars)

    n_items = len(freq_list)
    class_name = re.compile(r"<class '__main__\.(?P<id>.*)'>")
    ans = class_name.search(str(type(freq_list)))
    class_type = ans.group('id')
    print('  {}, {} char(s) -> t = {:>.4f}s  ({} items)'.format(class_type,
                                                                n_chars,
                                                                total_time,
                                                                n_items))
    if verbose:
        print()
        print(freq_list)

    # use something like the following for showing graphs
    # you will need matplotlib installed...
    # plot_truncated_freq_list(freq_list, 10)
    # plot_freq_list(freq_list)



def run_tests(filename, verbose=True):
    """Runs sorted/unsorted * n char tests
    If verbose == True then prints out the resulting freq list."""
    # to save reloading the corpus for each test simply pre load and send
    # it off to be analysed
    f = open(filename, 'r', encoding='utf-8')
    doc = format_document(f.read())
    # feel free to print doc here to see what it looks like
    # maybe only for the smallest file:)
    # print(doc)
    f.close()

    print_test_header(filename, doc)
    run_settings = []

    # Uncomment lines for tests that you want to run
    # you can run one after the other if you like...
    # run_settings.append((UnsortedFreqList, 1, verbose))
    # run_settings.append((NicerUnsortedFreqList, 1, verbose))
    # run_settings.append((SortedFreqList, 1, verbose))
    # run_settings.append((UnsortedFreqList, 2, verbose))
    # run_settings.append((NicerUnsortedFreqList, 2, verbose))
    # run_settings.append((SortedFreqList, 2, verbose))

    for settings in run_settings:
        run_a_test(doc, *settings)
    print('=' * 60)




################################################################################
# DO NOT MODIFY ANYTHING in this area 
#-------------------------------------------------------------------------------
def format_document(input_doc):
    """ Re-formats `input_doc` by collapsing all whitespace characters into a
    space and stripping all characters that aren't letters or punctuation.
    Converts all uppercase characters in the file to lower case.
    """
    # Collapse whitespace
    reduced_doc = re.compile(r'\s+', re.UNICODE).sub(' ', input_doc)
    # http://www.unicode.org/reports/tr44/#General_Category_Values
    allowed_categories = ('Lu', 'Ll', 'Lo', 'Po', 'Zs')
    d = ''.join([c.lower() for c in reduced_doc
                 if category(c) in allowed_categories])
    return d
################################################################################
################################################################################

if __name__ == '__main__':

    os.environ['TERM'] = 'linux'  # Suppress ^[[?1034h

    # Uncomment the next line to run the doctests
    doctest.testmod()  
    # Can enter an infinite loop if something isn't implemented correctly
    # So test on small data file first

    # Uncomment the files you want to test
    # ------------------------------------
    # run_tests("le_rire.txt", verbose=True)         # smallest corpus
    # run_tests("ulysses.txt", verbose=True)         # medium corpus
    # run_tests("war_and_peace.txt", verbose=True)   # one of the longest
    # books in english

