Project Overview: Python Sorting Algorithm Library
This project is a modular Python-based library that implements five of the most fundamental sorting algorithms. It is designed with a Controller-Service architecture, where a central Sorting class manages the data and provides a unified interface to call various algorithms stored in separate modules.

Algorithms Implemented
Bubble Sort: A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

Selection Sort: Improves on bubble sort by making only one exchange for every pass through the list, looking for the smallest element and moving it to the front.

Insertion Sort: Builds the final sorted array one item at a time, much like how you might sort playing cards in your hands.

Merge Sort: A Divide and Conquer algorithm that splits the list into halves, sorts them recursively, and then merges them back together.

Quick Sort: A highly efficient sorting algorithm that picks a 'pivot' element and partitions the array into sub-arrays of smaller and larger elements.

Technical Features
Modular Design: Each algorithm lives in its own .py file (e.g., bubble_sort.py), making the code clean, organized, and easy to maintain.

Data Integrity: The main class uses .copy() when passing data to algorithms. This ensures the original unsorted list remains unchanged so multiple algorithms can be tested on the same dataset.

Unified Interface: Users only need to interact with the Sorting class in sorting.py to run any of the five algorithms.
