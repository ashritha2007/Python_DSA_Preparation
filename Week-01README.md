# Week 01 — Python DSA Theory Notes

## Overview

This week focused on Python fundamentals and the basic concepts required to solve Data Structures and Algorithms (DSA) problems.

## Day 1 — Big O Notation and Array Basics

### 1. Big O Notation

Big O notation describes how the time or space required by an algorithm grows as the input size increases.

**Types of Time Complexity**

- **O(1) — Constant Time:** The operation takes approximately the same amount of time regardless of input size.
- **O(log n) — Logarithmic Time:** The problem size reduces significantly at each step. Binary search is a common example.
- **O(n) — Linear Time:** The work grows proportionally with the input size. Traversing an array is an example.
- **O(n log n) — Linearithmic Time:** Commonly seen in efficient sorting algorithms such as merge sort.
- **O(n²) — Quadratic Time:** Often occurs when two loops process pairs of elements.

**Important takeaway:** Choosing an efficient algorithm becomes increasingly important as the input size grows.

### 2. Arrays and Lists

An array stores elements in an ordered sequence. In Python, lists are commonly used to perform array-based DSA problems.

Important concepts:
- Indexing starts at zero.
- The last valid index is one less than the length of a non-empty list.
- Lists are mutable, so their elements can be changed.
- Traversal means visiting elements one by one.

### 3. Finding Maximum, Minimum and Sum

- **Maximum:** The largest element in a list.
- **Minimum:** The smallest element in a list.
- **Sum:** The total obtained by adding all elements.

A common approach is to traverse the list and update a running result.

**Time complexity:** O(n), because the list may need to be scanned completely.

### 4. Reversing an Array

Reversing means changing the order of elements so that the last element becomes the first.

The two-pointer technique uses:
- A left pointer starting at the beginning.
- A right pointer starting at the end.
- Swapping elements while moving both pointers toward the center.

**Time complexity:** O(n).

When reversing in place, the algorithm uses O(1) auxiliary space.

---

## Day 2 — Lists, Tuples and Array Rotation

### 1. List Operations

Python lists support operations such as:
- `append()` — adds an element to the end.
- `pop()` — removes and returns an element.
- `insert()` — inserts an element at a specified position.
- `len()` — returns the number of elements.
- Slicing — extracts a portion of a list or creates a reversed copy.

### 2. List Slicing

Slicing extracts elements using a start position, a stop position and an optional step.

Important points:
- The start index is included.
- The stop index is excluded.
- A negative step can traverse a sequence backward.
- Slicing generally creates a new list when applied to a list.

### 3. List Comprehension

List comprehension is a concise way to create a new list from an existing sequence by applying an expression to its elements.

It can make simple transformations shorter and easier to read.

### 4. Tuples

A tuple is an ordered collection similar to a list, but it is immutable.

- Lists use square brackets.
- Tuples commonly use parentheses.
- A list can be modified after creation, whereas a tuple cannot have its elements reassigned.

### 5. Array Rotation

Array rotation moves elements from one end of an array to the other.

- **Right rotation:** Elements at the end move toward the beginning.
- **Left rotation:** Elements at the beginning move toward the end.
- Rotating by `k` positions means repeating the rotation `k` times.
- When `k` is greater than the array length, modulo can reduce the number of necessary rotations.

### 6. Palindrome Array

An array is a palindrome if it reads the same forward and backward.

The two-pointer approach compares the first and last elements, then moves inward. A mismatch means the array is not a palindrome.

**Time complexity:** O(n).

---

## Day 3 — String Fundamentals

### 1. Strings

A string is a sequence of characters. Python strings are immutable, meaning their individual characters cannot be changed directly after creation.

### 2. String Slicing

String slicing extracts part of a string using index positions.

Important concepts:
- Indexing starts at zero.
- The stop index is excluded.
- A negative step allows traversal in reverse.
- Reverse slicing is a concise way to obtain a reversed string.

### 3. Important String Methods

- **`find()`** — returns the index of the first occurrence of a substring, or `-1` when it is absent.
- **`split()`** — divides a string into a list of parts.
- **`join()`** — combines strings from an iterable using a separator.
- **`lower()`** — converts alphabetic characters to lowercase.
- **`isalnum()`** — checks whether a character is a letter or digit.

### 4. String Comparison

String comparisons can be affected by uppercase and lowercase differences.

For example, uppercase and lowercase versions of the same word are not automatically equal. Converting strings to a common case can help when a problem requires case-insensitive comparison.

### 5. Reversing a String

A string can be reversed using slicing or by converting it into a list and applying the two-pointer technique.

Because strings are immutable, swapping individual characters requires a mutable representation, such as a list.

### 6. Anagrams and Frequency Counting

Two strings are anagrams when they contain the same characters with the same frequencies, even if the characters appear in a different order.

A dictionary can track character frequencies:
- Increase counts for characters in the first string.
- Decrease counts for characters in the second string.
- If all final counts are zero, the character frequencies match.

Unequal string lengths can be checked early because such strings cannot be anagrams.

**Time complexity:** O(n + m), where `n` and `m` are the lengths of the two strings.

---

## Day 4 — Sorting, Lambda, Dictionaries and Sets

### 1. Sorting

Sorting arranges elements in a particular order, usually ascending or descending.

Python provides two common approaches:
- **`sorted()`** returns a new sorted list and leaves the original collection unchanged.
- **`.sort()`** sorts a list in place and returns `None`.

### 2. The `key` Parameter

The `key` parameter specifies which value Python should use when comparing elements during sorting.

It is useful when sorting:
- Tuples by their second element.
- Records by a particular field.
- Strings by a chosen property.

### 3. Lambda Functions

A lambda is a small anonymous function that can be written in a single expression.

When used with sorting, it can extract the value that determines the sorting order.

Understanding the relationship between `sorted()`, `key` and `lambda` helps when solving problems involving pairs or structured data.

### 4. Dictionaries

A dictionary stores information as key-value pairs.

Important operations include:
- Adding new key-value pairs.
- Updating existing values.
- Checking whether a key exists.
- Accessing values using their keys.

Dictionaries are particularly useful for frequency counting, tracking information and solving lookup problems.

### 5. Sets

A set is a collection of unique elements.

Important properties:
- Duplicate elements are removed.
- Membership checks are typically efficient.
- Sets are useful for identifying unique values and detecting duplicates.
- A set should not be used when the original order or repeated occurrences must be preserved.

### 6. Removing Duplicates from a Sorted Array

In a sorted array, duplicate values appear next to one another.

A useful approach is to traverse the array and keep a value only when it differs from the last value already retained.

This problem helps develop the ability to use the sorted order of data to simplify a solution.

---

## Day 5 — Mixed Array and String Problems

### 1. Contains Duplicate

**Problem:** Determine whether a list contains any repeated value.

A set can be used to remove duplicates. If the set contains fewer elements than the original list, at least one duplicate exists.

**Concepts learned:** Sets, uniqueness and collection length.

### 2. Best Time to Buy and Sell Stock

**Problem:** Find the maximum profit from buying a stock on one day and selling it on a later day.

The initial brute-force approach considers possible buying and selling day pairs.

Important concepts:
- Buying must happen before selling.
- Profit is the selling price minus the buying price.
- The maximum profit should be tracked.
- A brute-force approach can be optimized by tracking the minimum price seen so far.

**Brute-force time complexity:** O(n²).

### 3. Two Sum

**Problem:** Find two distinct indices whose corresponding values add up to a target.

The initial brute-force approach checks pairs of elements using nested loops.

Important concepts:
- Array indexing.
- Nested loops.
- Pair selection without reusing the same index.
- Comparing a calculated sum with a target.
- Returning indices rather than values when required.

**Brute-force time complexity:** O(n²).

### 4. Valid Palindrome

**Problem:** Determine whether a string is a palindrome while ignoring spaces, punctuation and letter case.

General approach:
1. Convert the string to lowercase.
2. Keep only alphanumeric characters.
3. Compare the cleaned string with its reverse.

**Concepts learned:** String processing, character filtering, slicing and comparison.

**Time complexity:** O(n).

### 5. Valid Anagram

**Problem:** Determine whether two strings contain the same characters with identical frequencies.

The dictionary frequency-counting technique can be applied to solve this problem.

**Concepts learned:** Dictionaries, character counting, frequency differences and early length checks.

**Time complexity:** O(n + m).

---

## Key Lessons from Week 1

- Big O notation helps compare algorithm efficiency.
- Lists are mutable, while strings and tuples are immutable.
- Two pointers can simplify reversal and palindrome problems.
- Slicing provides a convenient way to extract or reverse sequences.
- Dictionaries are useful for frequency counting and lookups.
- Sets are useful for uniqueness and duplicate detection.
- Sorting with a custom key helps organize structured data.
- Nested loops often produce O(n²) solutions.
- Understanding brute force first makes optimization easier.
- Testing edge cases is an important part of problem solving.
