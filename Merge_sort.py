'''
# Description:
This program implements Merge Sort, a divide-and-conquer sorting algorithm that recursively splits an array into smaller subarrays, sorts them, and merges them back into a sorted sequence.

# What It Does:

Divides the Array:
 - Recursively splits the array into two halves until each part contains a single element.
Sorts and Merges:
 - Compares elements from both halves and merges them in sorted order.
 - Continues merging until the entire array is sorted.
Efficient Sorting:
 - Works with a time complexity of O(n log n), making it efficient for large datasets.

Example Usage:

numbers = [4, 10, 6, 14, 2, 1, 8, 5]
print('Unsorted array:', numbers)
merge_sort(numbers)
print('Sorted array:', numbers)

Output:

Unsorted array: [4, 10, 6, 14, 2, 1, 8, 5]  
Sorted array: [1, 2, 4, 5, 6, 8, 10, 14]  

This program efficiently sorts any numerical list using Merge Sort, making it a great choice for large-scale sorting tasks! 🚀
'''

def merge_sort(array):
    if len(array) <= 1:
        return
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: '+ str(numbers))