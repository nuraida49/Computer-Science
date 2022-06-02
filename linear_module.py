""" Linear/sequential searching """
import tools
# uncomment the next line if you want to make some Name objects
from classes import Name


def linear_result_finder(tested_list, quarantined):
    """ The tested list contains (nhi, Name, result) tuples
        and isn't guaranteed to be in any order
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
    """
    comparisons = 0
    results = []
    # ---start student section---
    len_of_tested_list = len(tested_list) 
    i = 0
    while i < len(quarantined):
        tested = 0
        names = quarantined[i]
        found_name = False
        
        while tested < len_of_tested_list and not found_name:
            nhi, name, result = tested_list[tested]
            if names == name:
                tuples = (names, nhi, result)
                results.append(tuples)
                found_name = True          
            tested += 1
            comparisons += 1
            
        if  tested == len_of_tested_list:
            tuples = (names, None, None)
            results.append(tuples)
            
        i += 1
    # ===end student section===
    return results, comparisons


# Don't submit your code below or pylint will get annoyed :)
if __name__ == '__main__':
    # write your own simple tests here
    # eg
    tested = [(3, Name("Arthur"), True), (1, Name("Bingle"), True), (2, Name('Bob'), True), (4, Name('Faba'), True), (5, Name('Zabba'), True)]
    quarantined = [Name("Bob"), Name("Abba"), Name("Faba")]
    print(linear_result_finder(tested, quarantined))
