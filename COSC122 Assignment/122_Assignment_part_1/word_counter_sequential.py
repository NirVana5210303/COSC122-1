"""This docstring is so that pylint doesn't fail"""
from classes_1 import CounterNode, CounterList

def word_counter_seq(words_list):
    """This function takes a list of strings and
    returns a CounterList, containing each of the
    strings and the number of times it occurred in
    the list, and an integer, the number of
    of string comparisons the function made.
    The CounterList is un-ordered."""
    #makes a new list
    complete_list = []
    #for every word in the given word list make it a string, make it lowercase
    #and check for puncuation
    
    for word in words_list:
        word = str(word)
        word = word.lower()
        word = "".join(i for i in word if i not in \
                       ('!','.',',',"'",'"',':',';'))
        complete_list.append(word)
    
    comparisons = 0
    
    #make a new counter list
    counter_list = CounterList()
    counter_list.append(CounterNode(''))
    
    #for every word in the given words_list
    #set a variable to the length of the CounterList
    #set a counting index
    for words in complete_list:
        length = len(counter_list)
        index = 0 
        
        #if the word correspondng to the index 0 is the same
        if counter_list[0].word == '':
            current_node = CounterNode(words,1)
            counter_list[0].word = current_node.word
            
        #while the length of the list is greater than the index
        #always increment a comparison as this is were we do comparisons
        else:
            while length > index:
                
                comparisons +=1
                
                if words == counter_list[index].word:
                    counter_list[index].count += 1
                    break
                index +=1
                
                #if the main index is the same length of the list,
                #e.g you've gone through the list and no 2 words are the same                
                if index == length:
                    #then make a new node according to the current word
                    current_node = CounterNode(words,1)
                    #and add it to the counter_list
                    counter_list.append(current_node)            
    return counter_list, comparisons 