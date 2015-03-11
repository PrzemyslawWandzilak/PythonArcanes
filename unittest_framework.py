import collections
import numbers
import unittest

# This program unit tests a function "get_combinations_of_target_sum" 
# The function itself takes an input list and target sum and returns a list of tuples being combinations of source list elements, 
# whose elements sum up to the target sum.
    

# Warm your brain up with Combination with no repetitions
#===============================================================================
# e.g. all combinations of 4 element list 
# comb([1, 2, 3, 4]) = 4 + 6 + 4 + 1 = 15
# 
# 1 element 
# [1] [2] [3] [4]
# 
# 2 element 
# (iterate over 1 element list, skip last "column", only append elements with larger index than current element's column)
# 11 12 13 14 => XX 12 13 14
# 21 22 23 24 => XX XX 23 24
# 31 32 33 34 => XX XX XX 34
# 41 42 43 44 => XX XX XX XX
# 
# 3 element 
# (iterate over 2 element list, skip last "column", only append elements with larger index than current element's column)
# [12]1 [12]2 [12]3 [12]4 => XXX XXX [12]3 [12]4
# [13]1 [13]2 [13]3 [13]4 => XXX XXX XXX   [13]4
# [14]1 [14]2 [14]3 [14]4 => XXX XXX XXX   XXX
# 
# [23]1 [23]2 [23]3 [23]4 => XXX XXX XXX  [23]4
# [24]1 [24]2 [24]3 [24]4 => XXX XXX XXX  XXX
# 
# [34]1 [34]2 [34]3 [34]4 => XXX XXX XXX  XXX
# 
# 4 element
# (iterate over 3 element list, skip last "column", only append elements with larger index than current element's column)
# [1,2,3]1 [1,2,3]2 [1,2,3]3 [1,2,3]4 => XXXX XXXX XXXX [1,2,3,]4
# [1,2,4]1 [1,2,4]2 [1,2,4]3 [1,2,4]4 => XXXX XXXX XXXX XXXX
# 
# [1,3,4]1 [1,3,4]2 [1,3,4]3 [1,3,4]4 => XXXX XXXX XXXX XXXX
# 
# [2,3,4]1 [2,3,4]2 [2,3,4]3 [2,3,4]4 => XXXX XXXX XXXX XXXX
# 
# (iterate over 4 element list, skip last "column") => BREAK, no more elements
# 
#===============================================================================

#https://docs.python.org/2/library/itertools.html#itertools.combinations
def combinations_docs_py(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def get_all_combinations(iterable):
    n = len(iterable)
    all_combinations = []
    for i in range(1,n+1):
        for x in combinations_docs_py(iterable,i):
            all_combinations.append(x)
            
    return all_combinations

def get_all_combinations_improved(iterable):
    n = len(iterable)
    for i in range(1,n+1):
        for x in combinations_docs_py(iterable,i):
            yield x
    
def filter_by_sum(iterable, insum):
    result   = []
    for x in iterable:
        if sum(x) == insum:
            result.append(x)
    
    return result

def get_combinations_of_target_sum(inlist, insum):
    if isinstance(inlist, collections.Iterable) and inlist and\
       all([isinstance(e,numbers.Number) for e in inlist]) and \
       isinstance(insum, numbers.Number):

        # Input arguments OK
        #comblist = get_all_combinations(inlist)
        comblist = get_all_combinations_improved(inlist)
        outlist = filter_by_sum(comblist, insum)
        return outlist
    
    else:
        
        # Input arguments wrong
        raise ValueError("Both input list and sum must be numeric")

class TestGetCombinationsOfTargetSum(unittest.TestCase):
 
    def setUp(self):
        self.mylist = [1, 2, 3, 4, 5]
        self.mysum = 6
        self.emptylist = []
        self.mynotanumericlist = "list"
        self.mynotanumericlist2 = [3, 2, [4]]
        self.mynotanumericsum = "sum"
       
    
    def test_invalid_argument0(self):
        self.assertRaises(ValueError, get_combinations_of_target_sum, self.emptylist, self.mysum)
        
    def test_invalid_argument1(self):
        self.assertRaises(ValueError, get_combinations_of_target_sum, self.mynotanumericlist, self.mysum)

    def test_invalid_argument2(self):
        self.assertRaises(ValueError, get_combinations_of_target_sum, self.mynotanumericlist2, self.mysum)
    
    def test_invalid_argument3(self):
        self.assertRaises(ValueError, get_combinations_of_target_sum, self.mylist, self.mynotanumericsum)
    
    def test_invalid_argument4(self):
        self.assertRaises(ValueError, get_combinations_of_target_sum, self.mylist, self.emptylist)        
    
    def test_invalid_argument5(self):
        self.assertRaises(ValueError, get_combinations_of_target_sum, self.mynotanumericlist, self.mynotanumericsum)
    
    def test_check_sum(self):
        self.assertTrue(all([sum(x) == self.mysum for x in get_combinations_of_target_sum(self.mylist, self.mysum)]))
    
    def test_two_element_list(self):
        self.assertEqual(get_combinations_of_target_sum([1, 2], 2), [(2,)])

    def test_551015(self):
        self.assertEqual(get_combinations_of_target_sum([5,5,10,15], 15), [(15,), (5,10), (5,10)])
    
    def test_12348(self):
        self.assertEqual(get_combinations_of_target_sum([1, 2, 3, 4, 8], 6), [(2,4), (1, 2, 3)])
        
    def test_negative(self):
        self.assertEqual(get_combinations_of_target_sum([-1, -2, -3, -4, -8], -6), [(-2,-4), (-1, -2, -3)])
        

if __name__ == '__main__':
    unittest.main()
    
