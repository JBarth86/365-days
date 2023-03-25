Day 1 - March 23, 2023

I started my 365 days of code with a coding exercise on codewars.com I've provided a link to the exercise below along with the specification and the necessary command to install the codewars testing framework for python. My solution to the exercise as well as the sample tests are also included in this directory.

Most frequently used words in a text
4 kyu
https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python

Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
Examples:
top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")

# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")

# => ["e", "ddd", "aa"]

top_3_words(" //wont won't won't")

# => ["won't", "wont"]

codewars python test framework:
pip install git+https://github.com/codewars/python-test-framework.git#egg=codewars_test

I used Python for this one just because that's what I've been using lately. For me the thought process went something like this:

    step 1: get rid of the trash text i.e. white space, special characters, and apostrophys that weren't part of a word.
    step 2: reduce the list of words in the cleaned up text to a dictionary listing each unique word with its associated count.
    step 3a: sort that dictionary back into a list that is ordered list where list[0] is the word with the highest count
    step 3b: returning the sorted list as a slice i.e list[0:3] eliminated the need to account for lists with less than 3 words.

I got steps 1, 2, and 3b done pretty quickly but I wasn't happy with initial implementation ideas and decided to sleep on it. The next day I had several job interviews but after having stepped away from the problem for a bit, once I sat back down to finish it up step 3a came along to my satisfaction pretty quickly.

Of course after I submitted my solution on Codewars I saw some other people had come up with a more clever (perhaps more pythonic) solution using the collections.Counter class that I didn't know about at the time. However, I'm still pretty satisfied with my solution, especially my use of regular expressions and reducer functions and I learned something new along the way.
