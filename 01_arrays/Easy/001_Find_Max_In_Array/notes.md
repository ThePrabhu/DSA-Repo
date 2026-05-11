# Max Element in Array

## Problem Understanding
Find the maximum element present in an array.

---

## Approach
- Initialize the first element as the maximum
- Traverse through the array
- Compare each element with the current maximum
- Update the maximum when a larger element is found

---

## Pattern
Array Traversal

---

## Time Complexity
O(n)

Reason:
The array is traversed only once.

---

## Space Complexity
O(1)

Reason:
No extra data structure is used.

---

## Mistakes I Made
- Initially thought sorting was required
- Forgot that sorting increases time complexity unnecessarily

---

## Better Optimization
### Sorting Approach
Time Complexity: O(n log n)

### Traversal Approach
Time Complexity: O(n)

Traversal is more efficient because only the maximum value is needed.

---

## Edge Cases
- Array with negative numbers
- Array with one element
- Array with duplicate maximum values

---

## Key Learnings
- Never sort an array when only max/min is required
- Learned basic array traversal
- Learned how to track a value while iterating
- Understood why traversal is more optimal than sorting