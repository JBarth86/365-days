from solution import same_structure_as
import codewars_test as test

test.assert_equals(same_structure_as([1,[1,1]],[2,[2,2]]), True, "[1,[1,1]] same as [2,[2,2]]")
test.assert_equals(same_structure_as([1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")
test.assert_equals(same_structure_as(0, []), False, "0 is not valid input")
test.assert_equals(same_structure_as([[3, []]], [[3, []]]), True, "[[3, []]] same as [[3, []]]")
test.assert_equals(same_structure_as([[]], []), False, "[[]] not same as []")
