# Check If Array Is Sorted

## Problem Understanding
Check whether the given array is sorted in non-decreasing order.

Example:

Input:
[1, 2, 3, 4]

Output:
True

---

## Approach

- Create a flag variable
- Traverse through the array
- Compare current element with next element
- If current element is greater than next element:
  - array is not sorted
  - stop traversal

---

## Pattern
- Array Traversal
- Adjacent Comparison

---

## Time Complexity
O(n)

### Reason
In worst case, the entire array is traversed once.

---

## Space Complexity
O(1)

### Reason
No extra data structures are used.

---

## Edge Cases

- Empty array
- Single element array
- Duplicate elements
- Negative numbers

---

## Better Optimization

### Cleaner Approach

```python
def check_is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False

    return True
```

### Why Better?
- Removes unnecessary flag variable
- Cleaner and more readable
- Uses early return

---

## Mistakes I Made

- Initially thought space complexity was O(n)
- Forgot that single variables do not affect space complexity significantly

---

## Key Learnings

- Learned adjacent element comparison
- Understood early termination using break/return
- Learned difference between O(1) and O(n) space
- Improved understanding of traversal patterns