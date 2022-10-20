def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # sLet's swap the element to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
arr = [-50, 6001, 1290,77,-99,100]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting :')
print(arr)
