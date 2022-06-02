""" Binary search is trickier than you think.
Remember your binary search should only use one comparison
per while loop, ie, one comparison per halving.
"""

import tools
# uncomment the next line if you want to make some Name objects
from classes import Name

# We recomment using a helper function that does a binary search
# for a Name in a given tested list. This will let you test your
# binary search by itself.




def binary_result_finder(tested, quarantined):
    """ The tested list contains (nhi, Name, result) tuples and
        will be sorted by Name
        quarantined is a list of Name objects
        and isn't guaranteed to be in any order
        This function should return a list of (Name, nhi, result)
        tuples and the number of comparisons made
        The result list must be in the same order
        as the  quarantined list.
        The nhi and result should both be set to None if
        the Name isn't found in tested_list
        You must keep track of all the comparisons
        made between Name objects.
        Your function must not alter the tested_list or
        the quarantined list in any way.
        Note: You shouldn't sort the tested_list, it is already sorted. Sorting it
        will use lots of extra comparisons!
    """
    total_comparisons = 0
    results = []
    # ---start student section---
    for names in quarantined:
        first = 0
        last = len(tested) - 1
        while first < last:
            midpoint = (first + last) // 2
            nhi, name, result = tested[midpoint]
            total_comparisons += 1
            if names <= name:
                last = midpoint - 1
            else:
                first = midpoint + 1
                
        midpoint = (first + last) // 2
        try:
            if names == name:
                tuples = (names, nhi, result)
                results.append(tuples)
            else:
                tuples = (names, None, None)
                results.append(tuples)
        except IndexError:
            pass
            
    # ===end student section===
    return results, total_comparisons


# Don't submit your code below or pylint will get annoyed :)
if __name__ == '__main__':
    # write your own simple tests here
    # eg
    tested = [(3, Name("Vallipuram"), True), (1, Name("Zorina"), True)]
    quarantined = [Name("Andrzej"), Name("Meris"), Name("Rheal"), Name("Vallipuram"), Name("Zorina")]
    print(binary_result_finder(tested, quarantined))
