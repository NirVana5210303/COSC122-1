"""COSC122 2014, Assignment Part 2, Task 2.
Couper Robert York 24245144
"""
from classes_1 import CounterNode, CounterList
# import word counter bin if you want to use it
from word_counter_binary_search import word_counter_bin


def quick_sort_by_count_last_pivot(counter_list):
    """Sorts a counter list into decreasing order according to the counts.
    The pivot value used is always the last value in the sublist"""
    
    copy_of_list = counter_list
    
    #if the list is empty or contains one item, it doesn't need to be sorted
    if len(copy_of_list) <= 1:
        return copy_of_list
    else:
        qsort_last_pivot_helper(copy_of_list, 0, len(copy_of_list)-1)
        return copy_of_list



def qsort_last_pivot_helper(alist, first, last):
    """Recursive helper for the quicksort"""
    if first >= last:
        return 
    
    
    spliter = partition_last_pivot(alist,first,last)
    
    # recurse into the right hand part
    qsort_last_pivot_helper(alist, spliter + 1, last,)    
    
    
    #recurse into the lefthand part
    qsort_last_pivot_helper(alist, first, spliter - 1)
   
    
    


def partition_last_pivot(alist, first, last):
    """Partitions using the last value in the sublist.
    The index of the pivot location is returned.
    """
    #creating a pivot who is the last item in the list
    pivot = alist[last].count
    
    finished = False
    
    left_pointer = first
    
    #since we are using the end item of the list as our pivot our right pointer
    #needs to be the next point along
    right_pointer = last -1
 
    while finished != True:
        
        #move the leftpointer up untill a value is greater than the pivot
        while left_pointer <= right_pointer and \
              alist[left_pointer].count > pivot or \
              alist[left_pointer].count == pivot and\
              alist[left_pointer].word < alist[last].word:
            left_pointer +=1
            
        #decrement the rightpointer untill we find a value less than the pivot
        while left_pointer <= right_pointer and  \
              alist[right_pointer].count < pivot or \
              alist[right_pointer].count == pivot and\
              alist[right_pointer].word > alist[last].word:
            right_pointer -=1
            
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

def run_my_tests():
    """Run your tests here to keep them tidy"""
    # write your test code here to avoid it being run by the marking system
    # simple example

    # import word counter bin if you want to use this
    #words = ['a','b','c','d','e']
    ##words = ['in', 'mathematics', 'and', 'computer', 'science', 'an',
             #'algorithm', 'is', 'a', 'step', 'by', 'step', 'procedure', 'for',
             #'calculations', 'computer', 'science', 'is', 'the', 'scientific',
             #'and', 'practical', 'approach', 'to', 'computation', 'and', 'its',
             #'applications', 'in', 'computer', 'science', 'a', 'data',
             #'structure', 'is', 'a', 'particular', 'way', 'of', 'organizing',
             #'data', 'in', 'a', 'computer', 'so', 'that', 'it', 'can', 'be',
             #'used', 'efficiently']
    words = ['picture','yourself','in','a','boat','on','a','river','with','tangeringe','trees','and','marmalade','skies','somebody','calls','you','you','answer','quite','slowly','a','girl','with',
                 'kaleidoscope','eyes','cellophane','flowers','of','yellow','and','green','towering','over','your','head','look','for','the','girl','with','the','sun','in','her','eyes','and','shes','gone','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','ah','follow','her','down','to','a','bridge','by','a','fountain'
                 'where','rocking','horse','people','eat','marshmallow','pies','everyone','smiles','as','you','drift','pass','the','flowers','that','grow','so','incredibly','high','newspapwer','taxis','appear','on','the','shore','waiting','to','take','you','away','climb','in','the','back','with','your','head','in','the','clouds','and',"you're",'gone','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','ah','picture','yourself','on','a','train','in','a','station','with','plasticine','porters','with','looking','glass','ties','suddenly','someone','is','there','at','the','turnstile','the','girl','with','kaleidoscope','eyes','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','ah','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','ah','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds',]             
    
    counts , comparisons = word_counter_bin(words)

    quick_sort_by_count_last_pivot(counts)             
    #counts, _ = word_counter_bin(cactus)
    print("Input:")
    print(counts)

    print('\n'*3)
    quick_sort_by_count_last_pivot(counts)
    print("Sorted CounterList:")
    print(counts)




if __name__ == "__main__":
    # write your tests in run_my_tests
    # run_my_tests()
    pass
