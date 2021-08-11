def binarysearch(list, value):
    left_edge, right_edge = 0, len(list)-1
    while left_edge <= right_edge:
        middle = left_edge + (right_edge - 1) // 2
        if list[middle] == value:
            return middle
        elif list[middle] < value:
            left_edge = middle + 1
        else:
            right_edge = middle -1
    return -1

def binarysearchrecursive(list, value, left_edge, right_edge):
    left_edge, right_edge = 0, len(list)-1
    if left_edge <= right_edge:
        middle = left_edge + (right_edge - 1) // 2
        if list[middle] == value:
            return middle
        elif list[middle] < value:
            return binarysearchrecursive(list, value, middle + 1, right_edge)
        else:
            return binarysearchrecursive(list, value, left_edge, middle -1)
    return -1

def main():
    list = [4, 3, 1, 5, 2]
    print(list)
    print(binarysearch(list, 5))

if __name__ == '__main__':
    main()