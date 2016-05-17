def partition_median_of_three(alist, first, last):
    """Partitions accoring to the median of three and
    returns the index of pivot location
    """
    # ---start student section---
    leftbound = first
    rightbound = last -1
    if len(alist) > 2:
        mid = (first + last)//2
        
        if alist[mid].count > alist[first].count:
            
            if alist[last].count > alist[mid].count:
                pivot = alist[mid]
                alist[mid], alist[last] = alist[last], alist[mid]
            elif alist[mid].count > alist[last].count:
 
                if alist[first].count > alist[last].count:
                    pivot = alist[first]
                    alist[first], alist[last] = alist[last], alist[first]
                elif alist[last].count > alist[first].count:
                    pivot = alist[last]
                else:
                    if alist[first].word > alist[last].word:
                        pivot = alist[first]
                        alist[first], alist[last] = alist[last], alist[first]
                    else:
                        pivot = alist[last]
            else:
                if alist[mid].word > alist[last].word:
                    pivot = alist[last]
                else:
                    pivot = alist[mid]
                    alist[mid], alist[last] = alist[last], alist[mid]
        elif alist[first].count > alist[mid].count:

            if alist[last].count > alist[first].count:
                pivot = alist[first]
                alist[first], alist[last] = alist[last], alist[first]
            elif alist[first].count > alist[last].count:

                if alist[mid].count > alist[last].count:
                    pivot = alist[mid]
                    alist[mid], alist[last] = alist[last], alist[mid]
                elif alist[last].count > alist[mid].count:
                    pivot = alist[last]
                else:
                    if alist[mid].word > alist[last].word:
                        pivot = alist[mid]
                        alist[mid], alist[last] = alist[last], alist[mid]
                    else:
                        pivot = alist[last]
            else:
                if alist[first].word > alist[last].word:
                    pivot = alist[last]
                else:
                    pivot = alist[first]
                    alist[first], alist[last] = alist[last], alist[first]
        else:
            if alist[mid].word > alist[first].word:
                if alist[first].count > alist[last].count:
                    pivot = alist[first]
                    alist[first], alist[last] = alist[last], alist[first]
                elif alist[last].count > alist[mid].count:
                    pivot = alist[mid]
                    alist[mid], alist[last] = alist[last], alist[mid]
                else:
                    if alist[first].word > alist[last].word:
                        pivot = alist[first]
                        alist[first], alist[last] = alist[last], alist[first]
                    elif alist[mid].word > alist[last].word:
                        pivot = alist[last]
                    else:
                        pivot = alist[mid]
                        alist[mid], alist[last] = alist[last], alist[mid]
        pivot = alist[last]
    else:
        pivot = first