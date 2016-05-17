import unittest
import os
import sys
from classes_1 import CounterList, CounterNode
from quicksort_median_of_three_pivot import qsort_by_count_mo3
from quicksort_median_of_three_pivot import partition_median_of_three
from timeout import timeout
from _for_part2_testing_only_word_counter_binary_search import word_counter_bin
# import word_counter_bin from your binary counter module here
# word_counter_binary_search import word_counter_bin

OUTPUT_MARK_FILE = "mark_mo3.txt"


sys.setrecursionlimit(3200)

def reset_mark():
    if os.path.isfile(OUTPUT_MARK_FILE):
        with open(OUTPUT_MARK_FILE,'w') as f:
            f.write('')


def load_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return words



def to_left_or_equal(node1, node2):
    """ Returns True if node1 has greater count or same count and <= word """
    if node1.count > node2.count:
        ans = True
    else:
        if node1.count < node2.count:
            ans = False
        else:
            # counts equal
            ans = node1.word <= node2.word
    return ans



def to_right_or_equal(node1, node2):
    """ Returns True if node1 has lower count or same count and >= word """
    if node1.count < node2.count:
        ans = True
    else:
        if node1.count > node2.count:
            ans = False
        else:
            # counts equal
            ans = node1.word >= node2.word
    return ans



def in_order(c_list):
    if len(c_list) == 0:
        result = True
    else:
        prev_node = c_list[0]
        for node in c_list[1:]:
            if not to_right_or_equal(node, prev_node):
                return False
            else:
                prev_node = node
        result = True
    return result


class TestQSMedian(unittest.TestCase):
    
    
    def add_mark(self, mark):
        """ Reads mark from file, adds to it and writes to file after each test
        so that partial mark is recorded if infinite loop is encountered.
        """
        total = 0
        if os.path.isfile(OUTPUT_MARK_FILE):
            with open(OUTPUT_MARK_FILE,'r') as f:
                raw_input = f.read().strip()
                if raw_input == '':
                    total = 0
                else:
                    total = int(raw_input)
        total += mark
        with open(OUTPUT_MARK_FILE,'w') as f:
            f.write(str(total)+'\n')
    
    def setUp(self):
        """This runs before each test case"""
        CounterList.reset_comparisons()

    @timeout(5)
    def test_all_counts_same(self):
        words = ['apples', 'oranges', 'pears', 'pie', 'strawberries']
        c_list, _ = word_counter_bin(words)
        qsort_by_count_mo3(c_list)
        self.assertTrue(in_order(c_list))
        self.add_mark(2)

    @timeout(5)
    def test_short_list(self):
        words = ['apples', 'apples', 'oranges', 'apples', 'pears', 'pie',
                 'strawberries', 'strawberries', 'strawberries', 'strawberries',
                 'strawberries']
        c_list, _ = word_counter_bin(words)
        qsort_by_count_mo3(c_list)
        self.assertTrue(in_order(c_list))
        self.add_mark(2)

    @timeout(5)
    def test_short_in_order_list(self):
        words = ['apples', 'apples', 'apples',
                 'oranges', 'oranges',
                 'pears']
        c_list, comparisons = word_counter_bin(words)
        qsort_by_count_mo3(c_list)
        self.assertTrue(in_order(c_list))
        self.add_mark(2)
        
    @timeout(5)
    def test_short_reverse_order_list(self):
        words = ['apples', 'oranges', 'oranges', 'pears', 'pears', 'pears', 'pie',
                 'pie', 'pie', 'pie', 'pie', 'strawberries', 'strawberries',
                 'strawberries', 'strawberries', 'strawberries', 'strawberries',
                 'strawberries', 'strawberries', 'strawberries']
        c_list, _ = word_counter_bin(words)
        qsort_by_count_mo3(c_list)
        self.assertTrue(in_order(c_list))
        self.add_mark(2)

    @timeout(5)
    def test_pivot_counts_same(self):
        c_list = CounterList()
        c_list.append(CounterNode('b', 20))
        c_list.append(CounterNode('d', 20))
        c_list.append(CounterNode('a', 20))
        c_list.append(CounterNode('e', 20))
        c_list.append(CounterNode('c', 20))
        pivot_index = partition_median_of_three(c_list, 0, 4)
        for i in range(pivot_index):
            self.assertLessEqual(c_list[i].word, c_list[pivot_index].word)
        for i in range(pivot_index+1, len(c_list)):
            self.assertGreaterEqual(c_list[i].word, c_list[pivot_index].word)
        self.add_mark(2)

    @timeout(5)
    def test_pivot_unique_counts(self):
        c_list = CounterList()
        c_list.append(CounterNode('b', 10))
        c_list.append(CounterNode('d', 20))
        c_list.append(CounterNode('a', 30))
        c_list.append(CounterNode('e', 40))
        c_list.append(CounterNode('c', 50))
        pivot_index = partition_median_of_three(c_list, 0, 4)
        for i in range(pivot_index+1, len(c_list)):
            self.assertLessEqual(c_list[i].count, c_list[pivot_index].count)
        for i in range(pivot_index):
            self.assertGreaterEqual(c_list[i].count, c_list[pivot_index].count)
        self.add_mark(2)

    @timeout(30)
    def test_with_alice(self):
        words = load_words("text_alice.txt")
        c_list, _ = word_counter_bin(words)
        qsort_by_count_mo3(c_list)
        self.assertTrue(in_order(c_list))
        self.add_mark(2)

    @timeout(30)
    def test_with_sherlock(self):
        words = load_words("text_sherlock.txt")
        c_list, _ = word_counter_bin(words)
        qsort_by_count_mo3(c_list)
        self.assertTrue(in_order(c_list))
        self.add_mark(2)



if __name__ == "__main__":
    reset_mark()
    unittest.main(exit=False, verbosity=0)
