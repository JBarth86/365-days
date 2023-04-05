from solution import User
import codewars_test as test

user = User()

def do_test(rank, expected_rank, expected_progress):
    if rank: user.inc_progress(rank)
    test.assert_equals(user.rank, expected_rank, "After applying rank of " + str(rank))
    test.assert_equals(user.progress, expected_progress, "After applying rank of " + str(rank))

@test.it("Sample tests")
def _():

    global user
    do_test(-8, -8, 3)

    user = User()
    do_test(-7, -8, 10)

    user = User()
    do_test(-6, -8, 40)

    user = User()
    do_test(-5, -8, 90)

    user = User()
    do_test(-4, -7, 60)

    user = User()
    do_test(1, -2, 40)
    do_test(1, -2, 80)
    do_test(1, -1, 20)
    do_test(1, -1, 30)
    do_test(1, -1, 40)
    do_test(2, -1, 80)
    do_test(2, 1, 20)
    do_test(-1, 1, 21)
    do_test(3, 1, 61)
