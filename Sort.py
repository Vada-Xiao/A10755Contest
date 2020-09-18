def quickSort(array, beginIndex, endIndex):
    if beginIndex < endIndex:
        left = beginIndex + 1
        right = endIndex - 1
        while left < right:
            while left < right and array[beginIndex] >= array[left]:
                left += 1
            while left < right and array[beginIndex] <= array[right]:
                right -= 1
            # Swapping two elements in python code.
            array[left], array[right] = array[right], array[left]
        while beginIndex < right and array[beginIndex] <= array[right]:
            right -= 1
        array[beginIndex], array[right] = array[right], array[beginIndex]
        quickSort(array, beginIndex, right)
        quickSort(array, right + 1, endIndex)
    return



TestData = [0,99,11,22,44,52,3,6,48,2,10,15]
quickSort(TestData, 0, len(TestData))
print(TestData)