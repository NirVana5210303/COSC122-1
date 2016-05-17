def load_file(file_name):
    data_list = []
    v = 0
    f = open(file_name)
    line = f.readline()
    while line != "":
        line.strip()
        line = int(line)
        data_list = data_list + [line]
        line = f.readline()
    return data_list

    
        
def selection_sort(file_name):
    alist = load_file(file_name)
    n_comps = 0
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax  = 0
        for location in range(1, fillslot+1):
            n_comps +=1
            if alist[location] < alist[positionOfMax]:
                positionOfMax = location

            n_comps+=1    
        alist[fillslot], alist[positionOfMax]  = alist[positionOfMax], alist[fillslot]
        n_comps +=1
    # Note: you will need to count the comparisons
    print("Selection sort on {0}, {1:d} items, used {2:d} comparisons".
          format(file_name,len(alist),n_comps))
    return alist




def insertion_sort(file_name):
    n_comps = 0
    alist = load_file(file_name)
    for index in range(1, len(alist)):
        stop = False
        currentvalue = alist[index]
        position = index
        while position > 0 and not(stop):
            n_comps +=1
            if alist[position-1] > currentvalue:
                alist[position] = alist[position-1]
                position = position - 1
            else:
                stop = True
            
        alist[position] = currentvalue
    # Note: you will need to count the comparisons
    print("Insertion sort on {0}, {1:d} items, used {2:d} comparisons".format(file_name, len(alist), n_comps))
    return alist



        
def gap_insertion_sort(alist, start, gap):
    """In-place insertion sort on alist with given start and gap."""
    for i in range (start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        stop = False
        while position >= gap and not(stop):
            if alist[position-gap] < currentvalue:
                alist[position] = alist[position - gap]
                position = position - gap
            else:
                stop = True
        alist[position] = currentvalue




def shell_sort(file_name):
    """ Runs shell sort with gap starting at n//2 and then gap = gap //2 etc """
    alist = load_file(file_name)
    sublistcount = len(alist) // 2
    n_comps = 0
    gaplist = []
    while sublistcount > 0 :
        for startposition in range(sublistcount):
            gap_insertion_sort(alist, startposition, sublistcount)
        # build a list of gaps used as we go
        gaplist.append(sublistcount)
        sublistcount = sublistcount // 2        
    # Note: you will need to count the comparisons
    print("Shell sort on {0}, {1:d} items, used {2:d} comparisons. Gaps were {3}".format(file_name,len(alist),n_comps, str(gaplist)))
    return alist
    



def shell_sort2(file_name, gaplist):
    """ Receives a list of gaps and runs shell sort with those gaps 
    If a gap is greater than the number of items then ignore and move to next """
    # ---start student section---
    pass
    # ===end student section===



