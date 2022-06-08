
def bubble_sort(sorting_list):
    count=0
    swaps= 0
    while(True):
        loop_swap = 0
        for i in range(len(sorting_list)-1):
            count +=1
            print(f"{count} iterations")
            previous = sorting_list[i]
            current = sorting_list[i+1]
            if(previous>current):
                sorting_list[i+1] = previous
                sorting_list[i] = current
                swaps+=1
                loop_swap +=1
        if loop_swap == 0:
            break
    print(f"Final result: {sorting_list}")
    print(f"Swaps: {swaps}")
    

bubble_sort([4, 3, 5, 0, 1])

