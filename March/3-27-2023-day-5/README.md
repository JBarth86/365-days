# Day 5 - March 27, 2023

Aaaaand it's Monday.

I started a new job today but still managed to carve out some code. It took me a less than an hour, but then I spent at least an hour getting the comments just right and also getting my python linter straightened out in vscode. >.<

---

### [Nesting Structure Comparison](https://www.codewars.com/kata/520446778469526ec0000001/train/python)

**4 kyu**

> Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.
>
> **For example:**
>
> ```python
> # should return True
> same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
> same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )
>
> # should return False
> same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
> same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )
>
> # should return True
> same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )
>
> # should return False
> same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
> ```

I won't go through a long drawn out monologue about my thought process on this one. The solution is thoroughly commented if you're interested.

Rediscovered map() and zip() when looking at some of the more clever solutions.
