# Python DSA Problems Collection 🐍

A comprehensive collection of Data Structures and Algorithms implementations in Python. This repository contains fundamental sorting and searching algorithms with clear, educational implementations.

## 📚 Table of Contents

- [Sorting Algorithms](#sorting-algorithms)
- [Searching Algorithms](#searching-algorithms)
- [How to Run](#how-to-run)
- [Algorithm Complexity](#algorithm-complexity)

## 🔄 Sorting Algorithms

### 1. Bubble Sort
**File:** [bubble_sort.py](bubble_sort.py)

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Best for:** Small datasets, educational purposes

### 2. Insertion Sort
**File:** [insertion_sort.py](insertion_sort.py)

Insertion Sort builds the final sorted array one item at a time by inserting each element into its correct position.

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Best for:** Small datasets, nearly sorted data

### 3. Selection Sort
**File:** [selection_sort.py](selection_sort.py)

Selection Sort divides the input into sorted and unsorted regions, and repeatedly selects the smallest element from the unsorted region.

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Best for:** Small datasets, minimizing memory writes

## 🔍 Searching Algorithms

### 1. Linear Search
**File:** [lin_search.py](lin_search.py)

Linear Search sequentially checks each element in the list until a match is found or the whole list has been searched.

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Best for:** Unsorted data, small datasets

### 2. Binary Search
**File:** [bin_search.py](bin_search.py)

Binary Search is an efficient algorithm for finding an item in a sorted list by repeatedly dividing the search interval in half.

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Best for:** Sorted data, large datasets

### 3. First Occurrence (Recursive)
**File:** [first_occurence.py](first_occurence.py)

Recursive implementation to find the first occurrence of a value in an array.

- **Time Complexity:** O(n)
- **Space Complexity:** O(n) - recursive stack
- **Approach:** Recursion

### 4. Last Occurrence (Recursive)
**File:** [last_occurence.py](last_occurence.py)

Recursive implementation to find the last occurrence of a value in an array by searching from the end.

- **Time Complexity:** O(n)
- **Space Complexity:** O(n) - recursive stack
- **Approach:** Recursion

## 🚀 How to Run

Each file is a standalone Python script with interactive input. To run any algorithm:

```bash
python <filename>.py
```

**Example:**
```bash
python bubble_sort.py
```

Follow the prompts to:
1. Enter the array size
2. Input array elements
3. View the results

## 📊 Algorithm Complexity

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) |
| **Linear Search** | O(1) | O(n) | O(n) | O(1) |
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1) |

## 📝 Notes

- All sorting implementations are **in-place** algorithms
- Binary search requires a **sorted array** to function correctly
- Recursive search implementations demonstrate functional programming concepts
- Each file includes interactive input for hands-on learning

## 🎯 Future Enhancements

Potential additions to this collection:
- Merge Sort
- Quick Sort
- Heap Sort
- Depth First Search (DFS)
- Breadth First Search (BFS)
- Tree and Graph implementations

---

**Author:** Niraj  
**Last Updated:** December 29, 2025
