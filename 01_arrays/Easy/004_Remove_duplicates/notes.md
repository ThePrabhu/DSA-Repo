# Remove Duplicates from Sorted Array

## Problem Understanding
Given a sorted array, remove duplicate elements in-place so that each unique element appears only once.

The relative order of the elements must remain the same.

Return the number of unique elements `k`.

Example:

Input:
[1, 1, 2]

Output:
2

Updated array:
[1, 2, _]

---

## My First Thought / Brute Force Idea
My first idea was to create a new array and store only unique elements.

That would work, but it would use extra space, which is not ideal for this problem because the question asks for an in-place solution.

---

## Final Approach
- Use two pointers
- One pointer reads the array
- One pointer writes the next unique element
- Since the array is sorted, duplicates are always next to each other
- When a new unique element is found, place it at the write position

---

## Pattern
- Two Pointers
- In-place Array Update
- Fast and Slow Pointer Style

---

## Time Complexity
O(n)

### Reason
The array is traversed only once.

---

## Space Complexity
O(1)

### Reason
No extra array or extra data structure is used.

---

## Why Two Pointers Work Here
Because the array is sorted, all duplicates are adjacent.

That means I only need to compare the current element with the previous element to detect whether it is a new unique value.

---

## Mistakes I Made
- First thought of using a brute force method with extra arrays
- Did not immediately think about in-place updating
- Needed to understand how the write pointer moves only when a new unique element is found

---

## Key Learnings
- Learned the two pointer technique
- Learned how to overwrite values in the same array
- Learned how sorted arrays make duplicate removal easier
- Learned how to analyze an array by reading and writing positions separately
- Understood why this problem is an in-place logic problem, not a brute force problem

---

## Similar Problems to Practice Later
- Move Zeroes
- Merge Sorted Array
- Remove Element
- Squares of a Sorted Array
- Partition Array
- Container With Most Water
- Two Sum