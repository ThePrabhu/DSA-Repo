def finding_max(arr):
    max_element = arr[0]
    for num in arr:
        if max_element < num:
            max_element = num

    return max_element
print(finding_max([1,9,5,-3,67,89,-12,123,4,5,6]))