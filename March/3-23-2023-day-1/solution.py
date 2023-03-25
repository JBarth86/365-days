from re import findall
from functools import reduce

# Main function


def top_3_words(text):

    # First we remove all the junk and put all the words in a list
    wordmap = findall(r"'?[a-z]+[a-z']*", text.lower())
    # Then we trade that list for a dictionary of unique words and their counts
    # Example {'Life': 42}
    wordmap = reduce(get_count, wordmap, {})

    # Finally we sort the dictionary by count into a list and return up to three of the largest values
    return sort_by_count(wordmap)[0:3]

# Reducer function


def get_count(result, word):

    # If the current word is already in the list increment the count else add it to the list with count == 1
    result[word] = result[word] + 1 if word in result else 1

    return result

# Sorting function


def sort_by_count(wordmap):

    results = []

    # For each word in the wordmap we compare it to each word already sorted in results
    for word, count in wordmap.items():

        index = 0

        # This loop runs if results is not empty and we haven't yet found the insertion point
        while len(results) > index:

            # If the result count at the current index is larger than the current word we move to the next index
            if wordmap[results[index]] > count:
                index += 1

            # If the count for the current word is larger we've found the proper insertion point
            else:
                break

        results.insert(index, word)

    return results
