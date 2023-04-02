# Day 10 - April 1, 2023

It's saturday. I picked my son back up from Alabama and generally enjoyed having the day off today. Yet again I reached for the low hanging fruit, but it's better than doing nothing at all.

---

[You Got Change?](https://www.codewars.com/kata/5966f6343c0702d1dc00004c/train/python)

**7 kyu**

> Create a function that will take any amount of money and break it down to the smallest number of bills as possible. Only integer amounts will be input, NO floats. This function should output a sequence, where each element in the array represents the amount of a certain bill type. The array will be set up in this manner:
>
> array[0] ---> represents $1 bills
>
> array[1] ---> represents $5 bills
>
> array[2] ---> represents $10 bills
>
> array[3] ---> represents $20 bills
>
> array[4] ---> represents $50 bills
>
> array[5] ---> represents $100 bills
>
> In the case below, we broke up $365 into 1 $5 bill, 1 $10 bill, 1 $50 bill, and 3 $100 bills:
>
> ```python
> 365 =>  [0,1,1,0,1,3]
> ```
>
> In this next case, we broke $217 into 2 $1 bills, 1 $5 bill, 1 $10 bill, and 2 $100 bills:
>
> ```python
> 217 => [2,1,1,0,0,2]
> ```

For whatever reason, even though the spec specifically calls for us to return an array, the tests expect us to return a tuple, so at the end I just cast the array as a tuple, but it is still pretty annoying.
