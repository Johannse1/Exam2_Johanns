# Exam 2
# Evan Johanns
# sorting
import random
from Search_Methods import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, quick_sort_recursion


def sorting():
    x = True
    y = 0
    while x is True:
        y = int(input("""Please type the number of the sort method you want to use: 
        1. Bubble sort (not that good)
        2. Selection sort
        3. Insertion sort
        4. Merge sort
        5. Quick sort
        6. Exit
        >> """))
        num_of_sort = int(input("How many numbers would you like to sort: "))
        my_list = []
        for num in range(num_of_sort):
            my_list.append((random.randint(1,100000)))

        if y == 1:
            method = bubble_sort(my_list)
            print(" Your list sorted using bubble sort.")
            print(method)
            sorting()
        elif y == 2:
            method = selection_sort(my_list)
            print(" Your list sorted using selection sort.")
            print(method)
            sorting()
        elif y == 3:
            method = insertion_sort(my_list)
            print(" Your list sorted using insertion sort.")
            print(method)
            sorting()
        elif y == 4:
            method = merge_sort(my_list)
            print(" Your list printed using merge sort")
            print(method)
            sorting()
        elif y == 5:
            method = quick_sort(my_list)
            print(" Your list printed using quick sort")
            print(method)
            sorting()
        elif y == 6:
            x = False


sorting()

