import unittest
import textwrap
from unique_words_in_list import find_unique_words_in_list1
from classes_1 import CounterList, CounterNode
from timeout import timeout
import os


# import your word_counter_bin with the next line
# word_counter_binary_search import word_counter_bin

from _for_part2_testing_only_word_counter_binary_search import word_counter_bin

DEFAULT_TIMEOUT = 5
OUTPUT_MARK_FILE = "mark_unq.txt"



def reset_mark():
    if os.path.isfile(OUTPUT_MARK_FILE):
        with open(OUTPUT_MARK_FILE,'w') as f:
            f.write('')



def change_get_comparisons():
    CounterList.get_comparisons = lambda: -1



change_get_comparisons()



class TestUnique(unittest.TestCase):

    def setUp(self):
        """This runs before each test case"""
        CounterList.reset_comparisons()

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

    @timeout(5)
    def test_01_two_word_lists(self):
        l1, temp = word_counter_bin(["list", "one"])
        l2, temp = word_counter_bin(["list", "two"])
        unique, comparisons = find_unique_words_in_list1(l1, l2)
        expected_uniques = "['one': 1]"
        expected_comparisons = 3
        self.assertEqual(str(unique), expected_uniques)
        self.assertEqual(comparisons, expected_comparisons)
        self.add_mark(2)

    @timeout(5)
    def test_02_two_word_lists_real_comparisons(self):
        l1, temp = word_counter_bin(["list", "one"])
        l2, temp = word_counter_bin(["list", "two"])
        unique, comparisons = find_unique_words_in_list1(l1, l2)
        expected_uniques = "['one': 1]"
        expected_comparisons = 3
        self.assertEqual(comparisons, CounterList.__n_comparisons__)
        self.add_mark(2)
        

    @timeout(5)
    def test_03_identical_lists(self):
        l1, temp = word_counter_bin(["nothing", "unique", "in",
                                     "this", "sentence"])
        l2, temp = word_counter_bin(["nothing", "unique", "in",
                                     "this", "sentence"])
        uniques, comparisons = find_unique_words_in_list1(l1, l2)
        expected_uniques = "[]"
        expected_comparisons_upper_limit = 10
        expected_comparisons_lower_limit = 5
        self.assertEqual(str(uniques), expected_uniques)
        self.assertGreaterEqual(comparisons, expected_comparisons_lower_limit)
        self.assertLessEqual(comparisons, expected_comparisons_upper_limit)
        self.add_mark(2)

    @timeout(5)
    def test_04_unique_lists(self):
        l1, temp = word_counter_bin(["everything", "is", "unique",
                                     "in", "this", "sentence"])
        l2, temp = word_counter_bin(["oranges", "apples", "pears",
                                     "strawberries", "pie"])
        unique, comparisons = find_unique_words_in_list1(l1, l2)
        expected_uniques = textwrap.dedent("""\
                                              ['everything': 1
                                              'in': 1
                                              'is': 1
                                              'sentence': 1
                                              'this': 1
                                              'unique': 1]""")
        expected_comparisons_upper_limit = 18
        expected_comparisons_lower_limit = 14
        self.assertEqual(str(unique), expected_uniques)
        self.assertGreaterEqual(comparisons, expected_comparisons_lower_limit)
        self.assertLessEqual(comparisons, expected_comparisons_upper_limit)
        self.add_mark(2)

    @timeout(5)
    def test_05_cross_over_lists(self):
        l1, temp = word_counter_bin(["a","b","c","d","e","f"])
        l2, temp = word_counter_bin(["d", "e", "f", "g", "h"])
        unique, comparisons = find_unique_words_in_list1(l1, l2)
        expected_uniques = textwrap.dedent("""\
                                              ['a': 1
                                              'b': 1
                                              'c': 1]""")
        expected_comparisons_upper_limit = 13
        expected_comparisons_lower_limit = 5
        self.assertEqual(str(unique), expected_uniques)
        self.assertGreaterEqual(comparisons, expected_comparisons_lower_limit)
        self.assertLessEqual(comparisons, expected_comparisons_upper_limit)
        self.add_mark(2)


    @timeout(5)
    def test_06_cross_over_lists_2(self):
        l1, temp = word_counter_bin(["d","e","f", "g", "h", "i", "j"])
        l2, temp = word_counter_bin(["a", "b", "c", "g", "h"])
        unique, comparisons = find_unique_words_in_list1(l1, l2)
        expected_uniques = textwrap.dedent("""\
                                              ['d': 1
                                              'e': 1
                                              'f': 1
                                              'i': 1
                                              'j': 1]""")
        expected_comparisons_upper_limit = 17
        expected_comparisons_lower_limit = 9
        self.assertEqual(str(unique), expected_uniques)
        self.assertGreaterEqual(comparisons, expected_comparisons_lower_limit)
        self.assertLessEqual(comparisons, expected_comparisons_upper_limit)
        self.add_mark(2)


    @timeout(5)
    def test_07_empty_list_one(self):
        l1, temp = word_counter_bin([])
        l2, temp = word_counter_bin(["oranges", "apples", "pears",
                                     "strawberries", "pie"])
        unique, comparisons = find_unique_words_in_list1(l1, l2)
        expected_uniques = "[]"
        expected_comparisons = 0
        self.assertEqual(str(unique), expected_uniques)
        self.assertEqual(comparisons, expected_comparisons)
        self.add_mark(1)

    @timeout(5)
    def test_08_empty_list_two(self):
        l1, temp = word_counter_bin(["everything", "is", "unique",
                                     "in", "this", "sentence"])
        l2, temp = word_counter_bin([])
        unique, comparisons = find_unique_words_in_list1(l1, l2)
        expected_uniques = textwrap.dedent("""\
                                              ['everything': 1
                                              'in': 1
                                              'is': 1
                                              'sentence': 1
                                              'this': 1
                                              'unique': 1]""")
        expected_comparisons = 0
        self.assertEqual(str(unique), expected_uniques)
        self.assertEqual(comparisons, expected_comparisons)
        self.add_mark(1)

    @timeout(30)
    def test_07_longer_lists(self):
        with open("text_alice.txt") as f:
            words1 = f.read().split()
        with open("text_looking_glass.txt") as f:
            words2 = f.read().split()
        l1, temp = word_counter_bin(words1)
        l2, temp = word_counter_bin(words2)
        unique, comparisons = find_unique_words_in_list1(l1, l2)
        expected_words_file = open("test_uniques_longer_lists_result.txt")
        expected_uniques = expected_words_file.read()
        expected_words_file.close()
        expected_comparisons_upper_limit = 8462
        expected_comparisons_lower_limit = 7084
        self.assertEqual(str(unique), expected_uniques)
        self.assertGreaterEqual(comparisons, expected_comparisons_lower_limit)
        self.assertLessEqual(comparisons, expected_comparisons_upper_limit)
        self.add_mark(2)


    @timeout(30)
    def test_08_longer_lists_real_comparisons(self):
        with open("text_alice.txt") as f:
            words1 = f.read().split()
        with open("text_looking_glass.txt") as f:
            words2 = f.read().split()
        l1, temp = word_counter_bin(words1)
        l2, temp = word_counter_bin(words2)
        unique, comparisons = find_unique_words_in_list1(l1, l2)
        expected_words_file = open("test_uniques_longer_lists_result.txt")
        expected_uniques = expected_words_file.read()
        expected_words_file.close()
        self.assertEqual(comparisons, CounterList.__n_comparisons__)
        self.add_mark(2)



if __name__ == "__main__":
    reset_mark()
    unittest.main(exit=False, verbosity=0)

