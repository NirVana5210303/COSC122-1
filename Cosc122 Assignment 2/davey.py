"""COSC122 2014, Assignment Part 2, Task 3.
Author: David Mackay
Date: 15/10/14
"""
from classes_1 import CounterNode, CounterList
from word_counter_binary_search import word_counter_bin




def qsort_by_count_mo3(alist):
    """Sorts a counter list into decreasing order according to the counts.
    The pivot value used is selected using the median of three technique"""
    if len(alist) == 1:
        return alist
    else:
        qsort_by_count_mo3_helper(alist, 0, len(alist)-1)
            
        
    return alist

def qsort_by_count_mo3_helper(alist, first, last):
    """Recursive helper for median of three quicksort"""
    if first>=last:
        return

    split = partition_median_of_three(alist, first, last)

    qsort_by_count_mo3_helper(alist, first, split - 1)
    qsort_by_count_mo3_helper(alist, split + 1, last)

def partition_median_of_three(alist, first, last):
    """Partitions accoring to the median of three and
    returns the index of pivot location
    """
    middle = (first + last) // 2
    
    if last == first + 1:
        alist[first], alist[last] = alist[last], alist[first]
        
    elif alist[first].count == alist[middle].count and \
         alist[first].count == alist[last].count:
        
        if alist[middle].word <= alist[first].word <= alist[last].word or \
             alist[last].word <= alist[first].word <= alist[middle].word:
            alist[first], alist[last] = alist[last], alist[first]           
                
        elif alist[first].word <= alist[middle].word <= alist[last].word or \
        alist[last].word <= alist[middle].word <= alist[first].word:
            alist[middle], alist[last] = alist[last], alist[middle]
           
        else:
            pivot = alist[last].count        
    
    elif alist[first].count == alist[middle].count or \
         alist[first].count == alist[last].count or \
         alist[middle].count == alist[last].count:
        partition_helper(alist, first, middle, last)
    
    elif alist[middle].count <= alist[first].count <= alist[last].count or \
        alist[last].count <= alist[first].count <= alist[middle].count:
        alist[first], alist[last] = alist[last], alist[first]       
            
    elif alist[first].count <= alist[middle].count <= alist[last].count or \
    alist[last].count <= alist[middle].count <= alist[first].count:
        alist[middle], alist[last] = alist[last], alist[middle]
       
    else:
        pivot = alist[last].count
        
        
    done = False
    pivot = alist[last].count
    left_index = first
    right_index = last-1
    
    while done is False:

        while left_index<=right_index and alist[left_index].count>pivot or \
              alist[left_index].count == pivot and \
              alist[left_index].word<alist[last].word:
            left_index+=1
        
        while left_index<=right_index and alist[right_index].count<pivot\
              or alist[right_index].count == pivot and \
              alist[right_index].word>alist[last].word:
            right_index-=1
            
        if left_index>right_index:
            done = True
            
        else:
            alist[left_index], alist[right_index] = \
                alist[right_index], alist[left_index]
            
    
    alist[last], alist[left_index] = alist[left_index], alist[last]
        
    return left_index



def partition_helper(alist, first, middle, last):
    """helper function for the partition_median_of_three"""
    if alist[first].count == alist[middle].count:
        
        if alist[first].count > alist[last].count and \
           alist[first].word <= alist[middle].word:
            alist[middle], alist[last] = alist[last], alist[middle]
            
        elif alist[first].count > alist[last].count:
            alist[first], alist[last] = alist[last], alist[first]
            
        elif alist[first].word >= alist[middle].word:
            alist[middle], alist[last] = alist[last], alist[middle]
        
        else:
            alist[first], alist[last] = alist[last], alist[first]            

    elif alist[first].count == alist[last].count:
        
        if alist[first].count > alist[middle].count and \
           alist[first].word <= alist[last].word:
            pass
        
        elif alist[first].count > alist[middle].count:
            alist[first], alist[last] = alist[last], alist[first]

        elif alist[first].word >= alist[last].word:
            pass
        
        else:
            alist[first], alist[last] = alist[last], alist[first]


    elif alist[middle].count == alist[last].count:
        
        if alist[middle].count > alist[first].count and \
           alist[middle].word <= alist[last].word:
            pass
        
        elif alist[middle].count > alist[first].count:
            alist[middle], alist[last] = alist[last], alist[middle]
        
        elif alist[middle].word >= alist[last].word:
            pass
        
        else:
            alist[middle], alist[last] = alist[last], alist[middle]
    
    
    
    
def run_my_tests():
    """Run your tests here to keep them tidy"""
    # write your test code here to avoid it being run by the marking system
    # simple example

    # import word counter bin if you want to use this
    words = ['in', 'mathematics', 'and', 'computer', 'science', 'an',
             'algorithm', 'is', 'a', 'step', 'by', 'step', 'procedure', 'for',
             'calculations', 'computer', 'science', 'is', 'the', 'scientific',
             'and', 'practical', 'approach', 'to', 'computation', 'and', 'its',
             'applications', 'in', 'computer', 'science', 'a', 'data',
             'structure', 'is', 'a', 'particular', 'way', 'of', 'organizing',
             'data', 'in', 'a', 'computer', 'so', 'that', 'it', 'can', 'be',
             'used', 'efficiently']

    counts, _ = word_counter_bin(words)
    #print("Input:")
    #print(counts)

    #print('\n'*3)
    qsort_by_count_mo3(counts)
    print("Sorted CounterList:")
    print(counts)




if __name__ == "__main__":
    # write your tests in run_my_tests
    # run_my_tests()
    pass
