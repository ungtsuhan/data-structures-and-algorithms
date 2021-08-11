# Sorting

## Selection Sort

Continue finding smallest value, and moving it to beginning of the list

### Performance

Slow. O(n ^ 2) Operation

```py
def selectionsort(unsorted_list):
    print(unsorted_list)
    for i in range(len(unsorted_list)):
        smallest_index = i
        for j in range(i+1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[smallest_index]:
                smallest_index = j
        unsorted_list[smallest_index], unsorted_list[i] = unsorted_list
    print(unsorted_list)
```