"""COSC122 2014, Assignment Part 2, Task 2.
Couper Robert York 24245144
"""
from classes_1 import CounterNode, CounterList
# import word counter bin if you want to use it
#from word_counter_binary_search import word_counter_bin


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