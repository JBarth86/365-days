# Day 11 - April 2, 2023

So I did write some code today but my solution didn't pass all the tests so I won't post it here just yet. I've got a few challenges set back in working directories that I haven't solved yet. The one I worked on today involves recieving a list of number ranges, or _intervals_ as input and outputing the total range covered by those intervals.

**example:**

```python
# this should return 2 as [0, 1] covers a range of 1
# as does [2, 3]
sum_of_intervals([0, 1], [2, 3])
```

the kicker here is that they can overlap and it becomes challenging to catch all the corner cases when they do

```python
# this should return 10 as [3, 7] bridges the gap
# between [0, 5] and [6, 10]
sum_of_intervals([[0, 5], [6, 10], [3, 7]])
```

I'll figure it out eventually. For now I'm just satisfied that I'm sticking to it.
