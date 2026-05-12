# Reverse An Array

## Problem Understanding
Reverse all elements in the array.

Example:

Input:
[1, 2, 3, 4]

Output:
[4, 3, 2, 1]

---

## My Initial Approach

- Initialized an empty array
- Traversed through the original array
- Added each element to the front of the new array using `+`
- Returned the reversed array

---

## Approach 1: Using List Concatenation

### Time Complexity
O(n²)

### Reason
Every iteration creates a new list and copies previous elements.

---

### Space Complexity
O(n)

### Reason
A new reversed array is created.

---

## Better Approaches

### Approach 2: Backward Traversal


### Time Complexity
O(n)

### Space Complexity
O(n)

---

### Approach 3: Two Pointer In-Place Reversal

```python
def reverse_an_arr(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr
```

### Time Complexity
O(n)

### Space Complexity
O(1)

---

## Pattern
- Array Traversal
- Two Pointers
- Swapping

---

## Edge Cases

- Empty array
- Single element array
- Negative numbers
- Duplicate elements

---

## Mistakes I Made

- Initially thought my solution was O(n)
- Did not realize list concatenation creates new arrays
- Forgot hidden cost of copying elements

---

## Key Learnings

- Learned array traversal
- Learned hidden complexity of list concatenation
- Understood difference between O(n) and O(n²)
- Learned swapping using two pointers
- Learned in-place reversal
- Understood why O(1) space optimization is important

---

## Important Observation

Operations like:
- list concatenation
- insert at beginning
- repeated string concatenation

can increase time complexity due to internal copying.