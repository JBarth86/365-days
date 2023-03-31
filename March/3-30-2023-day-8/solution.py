def all_non_consecutive(arr):
    
    output = []

    for index, number in enumerate(arr):

        next_index = index + 1
        next_number = number + 1

        if next_index < len(arr) and arr[next_index] != next_number:
            output.append({'i': next_index , 'n': arr[next_index]})

    return output
