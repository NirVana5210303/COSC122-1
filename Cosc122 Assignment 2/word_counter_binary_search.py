"""This docstring is so that pylint doesn't fail"""
from classes_1 import CounterNode, CounterList

def word_counter_bin(words_list):
    """This function takes a list of strings and
    returns a CounterList, containing each of the
    strings and the number of times it occurred in
    the list, and an integer, the number of
    of string comparisons the function made.
    The CounterList is alphabetically ordered"""
    complete_list = []
    #for every word in the given word list make it a string, make it lowercase
    #and check for puncuation
    
    for word in words_list:
        word = str(word)
        word = word.lower()
        word = "".join(i for i in word if i not in  ('!','.',',',"'",'"' \
                                                   ,':',';'))
        complete_list.append(word)
        
    comparisons = 0
    
    #make a new counter list
    counter_list = CounterList()
              
    #for every word in the given words_list
    for words in complete_list:
        #set up parameters for a binary search top and bottom
        top = len(counter_list)
        bottom = 0
        
        while top != bottom :
            #setup a mid_point
            mid_point = (bottom + top)//2
            comparisons +=1
            
            #check the middle point to see if its less than the current word
            #if so then the search continues manipluating the values
            if counter_list[mid_point].word < words :
                bottom = mid_point + 1
            else:               
                top = mid_point
        
        #if we're reched the top of the list then insert in the word at the top
        length = len(counter_list)
        if top == length:
            counter_node = CounterNode(words,1)
            counter_list.insert(top, counter_node)                  
            
        #if the bottom word is the same as the word then increase its count
        if counter_list[bottom].word == words:
            comparisons +=1
            counter_list[bottom].count +=1
        
        #any other case just insert the word at the bottom
        else:
            counter_node = CounterNode(words,1)
            comparisons +=1
            counter_list.insert(bottom , counter_node)       
    return counter_list, comparisons 

    
