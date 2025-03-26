def min_swaps_to_beautiful(arr):
    n = len(arr)

    
    def count_swaps(arr, target_order):
        swaps = 0
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if (target_order == 'ascending' and arr[j] < arr[min_index]) or \
                   (target_order == 'descending' and arr[j] > arr[min_index]):
                    min_index = j

            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]
                swaps += 1

        return s
    swaps_ascending = count_swaps(arr.copy(), 'ascending')
    swaps_descending = count_swaps(arr.copy(), 'descending')

    # Minimum number of swaps is the minimum of swaps for ascending and descending orders
    min_swaps = min(swaps_ascending, swaps_descending)

    return min_swaps
# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
result = min_swaps_to_beautiful(arr)
print(result)



