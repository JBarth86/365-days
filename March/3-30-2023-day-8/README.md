# Day 8 - March 30, 2023

### It's my birthday!

It has also been quite a long day. I traded in my 2016 Camaro 2SS convertible for a 2018 Honda Civic. I'm not _entirely_ unhappy with my decision.

I got home hella late from the dealership, so I picked an easy challenge for today and I won't go into great detail on my thinking on this one. Point being, I stayed on target and coded _something_ today, and that's something to be proud of.

---

[Find all non-consecutive numbers
](https://www.codewars.com/kata/58f8b35fda19c0c79400020f/train/python)

**7 kyu**

> Your task is to find all the elements of an array that are non consecutive.
>
> A number is non consecutive if it is not exactly one larger than the previous element in the array. The first element gets a pass and is never considered non consecutive.
>
> Create a function name all_non_consecutive
>
> E.g., if we have an array
>
> ```python
> [1,2,3,4,6,7,8,15,16]
> ```
>
> then 6 and 15 are non-consecutive.
>
> You should return the results as an array of objects with two values
>
> **i**: _the index of the non-consecutive number_
>
> and **n**: _the non-consecutive number_
>
> E.g., for the above array the result should be:
>
> ```python
> [
>  {'i': 4, 'n': 6},
>  {'i': 7, 'n': 15}
> ]
> ```
>
> If the whole array is consecutive or has one element then return an empty array.
>
> The array elements will all be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive and/or negetive and the gap could be larger than one.
>
> f you like this kata, maybe try this one next: https://www.codewars.com/kata/represent-array-of-numbers-as-ranges
