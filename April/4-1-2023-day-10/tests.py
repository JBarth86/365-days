import codewars_test as test
from solution import give_change

@test.describe("Basic Tests")
def test_group():
    @test.it("basic test cases")
    def test_case():
        test.assert_equals(give_change(365), (0,1,1,0,1,3))
        test.assert_equals(give_change(217), (2,1,1,0,0,2))
