def push_zeroes(arr, n): 
    count = 0 
    for i in range(n): 
        if arr[i] != 0:               
            arr[count] = arr[i] 
            count+=1

    while count < n: 
        arr[count] = 0
        count += 1
if __name__ == '__main__':
    num = [1, 0, 7, 2, 0, 3, 9, 0, 4]

    items = len(num)
    push_zeroes(num, items)
    print(num)
# Time Complexity: O(n) where n is number of elements in input array.