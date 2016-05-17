"""COSC122 2014, Assignment Part 2, Task 1.
Your name etc should go here...
Couper Robert York
"""

from classes_1 import CounterList, CounterNode
#from word_counter_binary_search import word_counter_bin


def find_unique_words_in_list1(list1, list2):
    """This function takes in two counter lists of words and counts
    , and returns
    a counter list containing all the words that are unique to the first list
    and the number of word comparisons that were used.
    The two lists are assumed to be 
    in alphabetical order and this function takes
    advantage of this to improve its efficiency.
    """
    CounterList.reset_comparisons()
    
    #Declaring new Counterlists counters & pointers
    new_counter_list = CounterList()
    comparisons = 0
    list1_pointer = 0
    list2_pointer = 0 
    
    #A main loop that will run untill the pointers are less then the length
    #of both given lists
    while list1_pointer < len(list1) and list2_pointer < len(list2):
        #Well our list1 word is greater than our list2 word so potentially
        #it could still be in the list2 so check the next element in list2
        if list1[list1_pointer].word > list2[list2_pointer].word:
            comparisons +=1
            list2_pointer +=1
            
        #List1 current word is less than list2's therefore it must be unique
        # as these are alphabetically ordered so can't exist later in list2 
        elif list1[list1_pointer].word < list2[list2_pointer].word:
            comparisons +=1
            new_counter_list.append(list1[list1_pointer])
            list1_pointer +=1
        
        #Then the words are the same so it can't be unique so check the next
        #words in each list (aslong as we arn't at the end of list1) <-indexing
        else:
            comparisons +=1
            if list1_pointer != len(list1):
                comparisons +=1
                list1_pointer +=1
                list2_pointer +=1
            
    #This is if we hit the end of list2 but still have remaining words in list1
    #these will be unique so are all added :)
    while list1_pointer != len(list1):
        new_counter_list.append(list1[list1_pointer])
        list1_pointer +=1 
    
    return new_counter_list, comparisons