def move_zeros(lst):

    results = []
    zeros = []

    for number in lst:

        if number == 0:
            zeros.append(number)
        
        else:
            results.append(number)

    return [*results, *zeros]
