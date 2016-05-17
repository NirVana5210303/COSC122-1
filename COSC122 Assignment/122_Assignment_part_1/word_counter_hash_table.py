from classes_2 import CounterNode, CounterLinkedList, hash_word


def word_counter_hash(words_list, slots):
    """This function takes a list of strings and
    returns a hash table (represented by a list,)
    were an empty slot contains None and a non
    empty slot contains a CounterLinkedList, and
    an integer, the number of string comparisons
    the function made.
    Each CounterLinkedList contains one or more
    CounterNodes, which contain a string and the
    number of times that string occurred in the
    given list."""
    
    complete_list = []
    #for every word in the given word list make it a string, make it lowercase
    #and check for puncuation
    
    for word in words_list:
        word = str(word)
        word = word.lower()
        word = "".join(i for i in word if i not in ('!','.',',',"'",'"'
                                                    ,':',';'))
        complete_list.append(word)
    comparisons = 0
    
    
    linked_list = CounterLinkedList()
    linked_list.head = (CounterNode(''))
    
    for word in complete_list:
        hash_word(word,slots)
        counter_list = [None]*slots
        
        if hash_word == None:
            linked_list.head = counter_list
            current_node = CounterNode(words,1)
            current_node.next_node = linked_list.head
        else:
            for item in linked_list:
                if item == word:
                    word.count +=1
                else:
                    linked_list.head = word
    
            
    return linked_list,comparisons


#check whether there is a value already stored at that hash_value by checking for None. If None add a new CounterLinkedList there. If not then you have to go through each item in the linked list at that particular slot and check for the word. If its there, add one to the count, if not, add it to the start of the linked list at that slot. #Because if it isn't None, then there is something already there (and it could be the same word or a different word that hashes to the same value)