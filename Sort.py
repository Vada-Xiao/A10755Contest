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

        
def heapSort(h):
    i=len(h)
    ans=[]
    while i>0:
        j=0
        for j in range(len(h)//2):
            c1=2*j+1
            c2=2*j+2
            Max=j
            if(c1<len(h))and(h[c1]>h[Max]):
                Max=c1
            if(c2<len(h))and(h[c2]>h[Max]):
                Max=c2
            h[Max],h[j]=h[j],h[Max]
            j+=1
        ans.append(h[0])
        del h[0]
        i-=1
    print(ans)


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

