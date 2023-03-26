# Day 3 - March 25, 2023

It's Saturday. I slept in and it was kind of nice but also not the most productive thing I've ever done.

Link and spec below for the Codewars challenge I did today. I was already familiar with regex but I did have to spend a little time researching lookaheads but this solution ultimately came along pretty easily.

I continue to remember past coding project ideas so I don't suppose I'll be running out of stuff to work on any time soon.

---

> ### [Regex Password Validation](https://www.codewars.com/kata/52e1476c8147a7547a000811/train/python)
>
> 5 kyu
>
> You need to write regex that will validate a password to make sure it meets the following criteria:
>
> - At least six characters long
> - contains a lowercase letter
> - contains an uppercase letter
> - contains a digit
> - only contains alphanumeric characters (note that '\_' is not alphanumeric)

I'll save you the touble of opening _solution.py_

```python
regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])[a-zA-Z\d]{6,}$"
```

As I said before, the bulk of the problem for me here was to figure out the mechanism of checking that a match satisfied multiple constraints i.e at least one number, at least one capital letter etc.

Lookaheads seemed to be the ticket, so I spent about a half hour watching videos about regex lookaheads in python and then quickly knocked out my minimum 1 line of code for the day.
