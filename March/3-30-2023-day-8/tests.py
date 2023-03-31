from solution import all_non_consecutive
import codewars_test as test

@test.describe('A simple example')
def _():
    test.assert_equals(all_non_consecutive([1,2,3,4,6,7,8,10]), [{'i': 4, 'n': 6}, {'i': 7, 'n': 10}])
