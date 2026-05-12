# Approach 1: List Concatenation
# Time: O(n²)
# Space: O(n)

def reverse_concat(arr):
    reversed_arr = []

    for num in arr:
        reversed_arr = [num] + reversed_arr

    return reversed_arr


# Approach 2: Backward Traversal
# Time: O(n)
# Space: O(n)

def reverse_backward(arr):
    reversed_arr = []

    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])

    return reversed_arr


# Approach 3: Two Pointer In-Place
# Time: O(n)
# Space: O(1)

def reverse_two_pointer(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left] # considet working with temp in other programmes

        left += 1
        right -= 1

    return arr