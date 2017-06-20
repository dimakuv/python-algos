Algorithms from "Introduction to Algorithms" written in Python

# Quick Usage

`./testsort.py heap.minheap` for sorting algos
`./test.py hashtable.openaddressing` for other algos (must implement func `test`)

# TODO

* Interval tree
* 2-3-4 tree
* Minimum spanning tree

# Random Notes

## Python

**Built-in functions are fast** -- built-in functions are written in C and highly optimized. For performance, one should use them even when there is a more pythonic way of solving the same task, but in pure Python. For example, string functions (e.g., `replace()`) are much faster than custom-made for-loops.

**Functions that work on iterables are slow** -- functions like `max()` take an iterable as argument which is generally slow. Performance of costructs like `max(var1, var2)` is worse than a more verbose `var1 if var1>var2 else var2`.

**Python is a memory hog** -- Python's integers are 24B in size, dicts are ridiculously voracious, and empty objects take ~80B. For tiny objects, one should specify `__slots__ = ['field1', 'field2', ...]` to reduce space waste. *Never play with garbage collection!*

**Inner loops in CPython are slooow** -- In cases you cannot remove inner loops, try running in PyPy.

## Algorithms

**Rabin-Karp algorithm (rolling hash)** -- finds a *set* of `p` patterns (combined length `m`) in a string `n`. Useful when there is one huge string and several patterns (of the same length) to find. Can be twicked to find patterns of different length: need to maintain several rolling hashes over the string. Rolling hash function can be as simple as *addition*. The algorithm can be generalized to 2D case. Average time: `O(n+m)`, worst-case time: `O(nm)`, space `O(p)`.

**Aho-Corasick algorithm** -- finds a *set* of patterns (combined length `m`) in a string `n`. Differs from Rabin-Karp in that the set of patterns is *preprocessed* into a finite state machine resembling a trie-with-failures. Useful when there is a dictionary of patterns such that it is stored in a FSM format and invoked on many strings. Worst-case time: `O(n+m)`, space: `O(m)`.

**Longest Common Subsequence (LCS)** -- dynamic programming algorithm that maintains a 2D table of *lengths of LCS in prefixes*. If we only need the length, can skip the backtracking part and only use *two rows* -- one row of previous lengths + one row of current lengths. This saves space greatly.

**Preprocessing in greedy algorithms** -- algorithms that look like *backtracking* or *dynamic programming* can sometimes be transformed into greedy. The key is to perform some preprocessing on the input that will facilitate finding the optimum local decision.

**Non-recursive DFS is non-trivial** -- non-recursive DFS is *kinda* BFS with a stack instead of a queue. However, it is more complicated because pre- and post-processing are cumbersome. In short, each vertex is added to the stack *two times* -- once for preprocessing and examination of its edges and once for postprocessing. Thus, each vertex has *three stages*: not visited, visited awaiting postprocessing, and visited-and-done. Simple example is in `graph/dfs_nonrecursive.py`.

## Data Structures

**Streaming Median** -- stores a median over the last `n` items in the array. Uses MinHeap + MaxHeap with the invariant that all items in MinHeap are *greater than or equal to* all items in MaxHeap. (I.e., MinHeap provides the minimum item greater than the maximum item in MaxHeap.) The median is always the combination of peeks into MinHeap and MaxHeap. To implement streaming -- when the oldest item is evicted and a new one is appended -- one needs the `remove()` operation in both heaps, which can be implemented in `O(lg n)` time.

## Common Sense

**Counting frequencies** -- counting frequences of letters in alphabet over an input string (distribution of letters) can be beneficial. Python `dict`s are an obvious choice of weapon.

**Principle of mass conservation** -- if some quantity is moved from one container to the other, or the quantities are swapped, it is beneficial to check if the quantity in the initial state equals to the quantity in the final state.

**Iterate over arrays via skipping redundant iterations** -- Knuth-Morris-Pratt and Boyer-Moore string search algorithms are great examples. Basically, if there is a possibility to skip redundant iterations, even though it does not change asymptotic worst-case runtime, it helps a lot in practice.

**Properties of sorted arrays work also on reversed order** -- if some property (e.g., *minimal absolute difference between two consequtive items*) holds for a asc-sorted array, it usually also holds for a reverse-sorted array.

**Minimum number of swaps between two arrays** -- calculated using cycles (see *cyclesort*). The idea is to follow the chain "value at current index in 1st array -> index of this value in 2nd array -> value at new index in 1st array -> etc" thus creating cycles. Length of each cycle gives the number of swaps plus one. 
