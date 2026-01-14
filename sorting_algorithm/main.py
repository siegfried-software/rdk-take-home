def sortAndFindMedian(numbers):
    insertion_sort(numbers)
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1]+numbers[n // 2]) /2
    else:
        return numbers[n//2]


# Insertion sort is a very fast sorting algorithm when specifically dealing with small data sets (despite Big-O best/worst/avg)
# Given that the unit tests I did are small, I implemented it over merge sort or quick sort
# Big-O of O(n^2) on average and worst (reversed order) while a Big-O of O(n) at best (sorted order)
# Easier to implement due to no recursion and saves memory
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        j = i
        while j > 0 and numbers[j - 1] > numbers[j]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1
    return numbers
