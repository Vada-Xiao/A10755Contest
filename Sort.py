def QuickSort(array, beginIndex, endIndex):
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
        QuickSort(array, beginIndex, right)
        QuickSort(array, right + 1, endIndex)
    return


# list is a keyword in python!! Everyone must prevent for using it.
def SelectionSort(list):
    for i in range(len(list)):
        min=i
        for j in range(i+1,len(list)):
            if(list[j]<list[min]):
                min=j
        list[i],list[min]=list[min],list[i]
    return

TestData = [0,99,11,22,44,52,3,6,48,2,10,15]

# QuickSort(TestData, 0, len(TestData))
# print(TestData)

SelectionSort(TestData)
print(TestData)