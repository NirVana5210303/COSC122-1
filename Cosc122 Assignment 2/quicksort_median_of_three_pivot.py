"""COSC122 2014, Assignment Part 2, Task 3.
Couper Robert York 24245144,
"""
from classes_1 import CounterNode, CounterList

# import word counter bin if you want to use it
from word_counter_binary_search import word_counter_bin




def qsort_by_count_mo3(alist):
    """Sorts a counter list into decreasing order according to the counts.
    The pivot value used is selected using the median of three technique"""
    copy_of_list = alist
    
    #if the list is empty or contains one item, it doesn't need to be sorted
    #otherwise carry on :)
    if len(copy_of_list) == 1:
        return copy_of_list
    else:
        qsort_by_count_mo3_helper(copy_of_list, 0, len(copy_of_list)-1)
    return copy_of_list

def qsort_by_count_mo3_helper(alist, first, last):
    """Recursive helper for median of three quicksort"""
    if first >= last:
        return 
    
    
    spliter = partition_median_of_three(alist, first, last)
    
    # recurse into the left hand part
    qsort_by_count_mo3_helper(alist, first, spliter - 1)
    qsort_by_count_mo3_helper(alist, spliter + 1, last)  
    #recurse into the lefthand part



def partition_median_of_three(alist, first, last):
    """Partitions accoring to the median of three and
    returns the index of pivot location
    """ 
    #find a middle value, and compare the first, middle and last values.Counts
    #and words to make sure it is the correct one to be swapped
    #NOTE:that this is Last_pivot code reused so no matter what the median value
    #is it will be swapped to the end and will continue as before
    
    middle = (first + last) // 2
    
    if first == last + 1:
        alist[first], alist[last] =  alist[last], alist[first]
    
        
    elif alist[first].count == alist[middle].count and \
         alist[last].count == alist[middle].count:
        
        if alist[middle].word <= alist[first].word <= alist[last].word or \
             alist[last].word <= alist[first].word <= alist[middle].word:
            alist[first], alist[last] = alist[last], alist[first]           
                
        elif alist[first].word <= alist[middle].word <= alist[last].word or \
        alist[last].word <= alist[middle].word <= alist[first].word:
            alist[middle], alist[last] = alist[last], alist[middle]
           
        else:
            pivot = alist[last].count        
    
    elif alist[middle].count == alist[first].count or \
         alist[last].count == alist[first].count or \
         alist[middle].count == alist[last].count:
        my_partition(alist, first, middle, last)        
        
    elif alist[middle].count < alist[first].count < alist[last].count\
            or alist[last].count < alist[first].count < alist[middle].count:
        alist[first], alist[last] = alist[last], alist[first]           
        
    elif alist[first].count < alist[middle].count < alist[last].count\
         or alist[last].count < alist[middle].count < alist[first].count:
        alist[middle], alist[last] = alist[last], alist[middle]
      
    else:
        pivot = alist[last].count      
        
    left_pointer = first
    right_pointer = last -1    
    pivot = alist[last].count 
    finished = not True
   
     
    #since we are using the end item of the list as our pivot our right pointer
    #needs to be the next point along
    
    while finished != True:
        #move the leftpointer up untill a value is greater than the pivot
        while left_pointer <= right_pointer and\
              alist[left_pointer].count > pivot or\
              alist[left_pointer].count == pivot and\
              alist[left_pointer].word < alist[last].word:
            left_pointer = left_pointer + 1
            
        #decrement the rightpointer untill we find a value less than the pivot
        while left_pointer <= right_pointer and  \
              alist[right_pointer].count < pivot or \
              alist[right_pointer].count == pivot and\
              alist[right_pointer].word > alist[last].word:
            right_pointer = right_pointer - 1
            
        #if the pointers have surpassed then jump out the loop as we have found
        #our split point
        if right_pointer < left_pointer:
            finished = True
        else:
            #Swap our pointers because the left mark is now the split point
            alist[left_pointer], alist[right_pointer] = \
            alist[right_pointer], alist[left_pointer]
            
    #swap the pivot out for a new one
    alist[last], alist[left_pointer] = alist[left_pointer], alist[last]
 

    return left_pointer


def my_partition(alist, first, middle, last):
    """this function is called upon and helps check counts/words
    and cut down messiness of code and to make it pylint compatible"""
    
    #Here i am checking to make sure we are swapping the correct words if the
    #counts are the same
    
    if alist[first].count == alist[middle].count:
        
        if alist[first].count > alist[last].count and \
           alist[first].word <= alist[middle].word:
            alist[middle], alist[last] = alist[last], alist[middle]
            
        elif alist[last].count > alist[first].count:
            alist[first], alist[last] = alist[last], alist[first]
            
        elif alist[middle].word >= alist[first].word:
            alist[middle], alist[last] = alist[last], alist[middle]
        
        else:
            alist[first], alist[last] = alist[last], alist[first]            
    
    elif alist[first].count == alist[last].count:
        
        
        if alist[middle].count > alist[first].count:
            alist[first], alist[last] = alist[last], alist[first]

        else:
            alist[first], alist[last] = alist[last], alist[first]
    
    
    elif alist[middle].count == alist[last].count:
        
        if alist[first].count > alist[middle].count:
            alist[middle], alist[last] = alist[last], alist[middle]
        
        else:
            alist[middle], alist[last] = alist[last], alist[middle]


def run_my_tests():
    """Run your tests here to keep them tidy"""
    # write your test code here to avoid it being run by the marking system
    # simple example

    # import word counter bin if you want to use this
    #words = ['in', 'mathematics', 'and', 'computer', 'science', 'an',
             #'algorithm', 'is', 'a', 'step', 'by', 'step', 'procedure', 'for',
             #'calculations', 'computer', 'science', 'is', 'the', 'scientific',
             #'and', 'practical', 'approach', 'to', 'computation', 'and', 'its',
             #'applications', 'in', 'computer', 'science', 'a', 'data',
             #'structure', 'is', 'a', 'particular', 'way', 'of', 'organizing',
             #'data', 'in', 'a', 'computer', 'so', 'that', 'it', 'can', 'be',
             #'used', 'efficiently']
    #words = ['b', 'd', 'a','a', 'e', 'c','c']
    #words = ['b','a','a','c']
    words = ['picture','yourself','in','a','boat','on','a','river','with','tangeringe','trees','and','marmalade','skies','somebody','calls','you','you','answer','quite','slowly','a','girl','with',
                     'kaleidoscope','eyes','cellophane','flowers','of','yellow','and','green','towering','over','your','head','look','for','the','girl','with','the','sun','in','her','eyes','and','shes','gone','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','ah','follow','her','down','to','a','bridge','by','a','fountain'
                     'where','rocking','horse','people','eat','marshmallow','pies','everyone','smiles','as','you','drift','pass','the','flowers','that','grow','so','incredibly','high','newspapwer','taxis','appear','on','the','shore','waiting','to','take','you','away','climb','in','the','back','with','your','head','in','the','clouds','and',"you're",'gone','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','ah','picture','yourself','on','a','train','in','a','station','with','plasticine','porters','with','looking','glass','ties','suddenly','someone','is','there','at','the','turnstile','the','girl','with','kaleidoscope','eyes','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','ah','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','ah','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds',]       
    counts, _ = word_counter_bin(words)
    print("Input:")
    print(counts)

    print('\n'*3)
    qsort_by_count_mo3(counts)
    pivot_index = partition_median_of_three(counts, 0, 4)
    print("Sorted CounterList:")
    print(counts)
    
if __name__ == "__main__":
    # write your tests in run_my_tests
    run_my_tests()
    pass