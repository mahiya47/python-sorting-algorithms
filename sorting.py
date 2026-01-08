import bubble_sort
import insertion_sort
import merge_sort
import quick_sort
import selection_sort

class Sorting():
    def __init__(self, data):
        self.data = data

    def run_bubble(self):
        return bubble_sort.bubble_sort(self.data.copy())

    def run_insertion(self):
        return insertion_sort.insertion_sort(self.data.copy())

    def run_merge(self):
        return merge_sort.merge_sort(self.data.copy())

    def run_quick(self):
        temp = self.data.copy()
        return quick_sort.quick_sort(temp, 0, len(temp) - 1)

    def run_selection(self):
        return selection_sort.selection_sort(self.data.copy())

nums = [64, 34, 25, 12, 22, 11, 90]
sorter = Sorting(nums)

print("Original List:", nums)
print("Bubble Sort:   ", sorter.run_bubble())
print("Insertion Sort:", sorter.run_insertion())
print("Merge Sort:    ", sorter.run_merge())
print("Quick Sort:    ", sorter.run_quick())
print("Selection Sort:", sorter.run_selection())