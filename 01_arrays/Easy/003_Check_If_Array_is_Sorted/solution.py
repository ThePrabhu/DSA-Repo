def check_is_sorted(arr):
    is_sorted = True
    
    if len(arr) <= 1:
        return True
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            is_sorted = False
            break

    return is_sorted