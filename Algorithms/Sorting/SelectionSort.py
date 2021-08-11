def selectionsort(unsorted_list):
    
    print(unsorted_list)
    
    # iterating the whole unsorted list
    for i in range(len(unsorted_list)):
        
        # keep track of the index of minimum value, so that we can move it to sorted size
        smallest_index = i
        
        for j in range(i+1, len(unsorted_list)):
            
            # if found element with smaller value than the current smallest value
            # set new index to the index of the smaller value
            if unsorted_list[j] < unsorted_list[smallest_index]:
                smallest_index = j
        
        # then swap the smallest element with the first element
        unsorted_list[smallest_index], unsorted_list[i] = unsorted_list[i], unsorted_list[smallest_index]
        
        print(unsorted_list)
    
    print(unsorted_list)

def main():
    list = [4, 3, 1, 5, 2]
    selectionsort(list)

if __name__ == '__main__':
    main()