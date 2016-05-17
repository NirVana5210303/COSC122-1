"""This docstring is so that pylint doesn't fail"""
from classes_1 import CounterNode, CounterList

def word_counter_freq(words_list):
    """This function takes a list of strings and
    returns a CounterList, containing each of the
    strings and the number of times it occurred in
    the list, and an integer, the number of
    of string comparisons the function made.
    The CounterList is ordered by the number of
    times a string occurred in the list"""
    
#makes a new list in preperation for de-puncuated words to be added
    complete_list = []
   #for every word in the given word list make it a string, make it lowercase
   #and check for puncuation
   
    for word in words_list:
        word = str(word)
        word = word.lower()
        word = "".join(i for i in word if i not in \
                       ('!','.',',',"'",'"',':',';'))
        complete_list.append(word)
   
   #setup our comparisons
    comparisons = 0
   
    #make a new counter list
    counter_list = CounterList()
    #set a default value to automatically so we can always add a value to
    #the counter list
    counter_list.append(CounterNode(''))
   
        # for every word in the given words_list
    for words in complete_list:
        #set a variable to the length of the CounterList
        length = len(counter_list)
        #set an counting index
        index = 0
            
        #here is where we force it to compare and add our first value
        if counter_list[0].word == '':
            current_node = CounterNode(words,1)
            counter_list[0].word = current_node.word
            
        else:
            #while the length of the list is greater than the index
            while length > index:
                #always increment a comparison as this is were we do comparisons
                comparisons +=1
                #if the word is the same as the current indexed word
                if words == counter_list[index].word:
                    #increase the current indexed words count
                    counter_list[index].count += 1
                    #creating another place holding index that will be used
                    #for comparing our two words count vales
                    loop_counter = index
                    #Making a trigger that will be used for swapping items
                    item_comparing = True
                    
                    #while the current words count is greater than the word
                    #next to its count AND the loop_counter is > 0 so it doesn't
                    #go out of range
                    while counter_list[index].count > \
                        counter_list[loop_counter-1].count and loop_counter > 0:
                        #finish looping here with the trigger
                        item_comparing = False
                        #Decrement our loop_counter
                        loop_counter -=1
                       
                    #now if the trigger is False     
                    if item_comparing == False:
                        #switch the two items that need switching
                        counter_list[loop_counter], counter_list[index] = \
                        counter_list[index], counter_list[loop_counter]
                    
                    break
                #increase the main index to keep going through words
                index +=1
                
                #if the main index is the same length of the list,
                #e.g you'rve gone through the list and no 2 words are the same
                if index == length:
                    #then make a new node according to the current word
                    current_node = CounterNode(words,1)
                    #add it to the counter_list
                    counter_list.append(current_node)
                    
    #return our final list and number of comparisons
    return counter_list, comparisons    