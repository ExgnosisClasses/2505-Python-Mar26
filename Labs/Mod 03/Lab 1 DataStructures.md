# Lab 3-1 : Data Structures

In this lab you will create and use some of the basic data structures

For the exercises that follow, we will use the sentence "it was the best of times and it was the worst of time" as the data and then store it in the different data structures.

You will:
- Store the sentence as a list, tuple, and set
- Compare how these structures behave
- Convert between them
- Create a dictionary of word counts

# Step 1: Store the Sentence

```python
sentence = "it was the best of times and it was the worst of time"
words = sentence.split()

words_list = list(words)
words_tuple = tuple(words)
words_set = set(words)

print("List:", words_list)
print("Tuple:", words_tuple)
print("Set:", words_set)
```

**Explanation**:
- `split()` turns the string into a list of words.
- `list()` is mutable and ordered.
- `tuple()` is immutable and ordered.
- `set()` is mutable and **unordered** with **unique elements only**.

---

## Step 2: Modify the List and Try with Tuple

```python
# Modify the list
words_list.append("again")
print("Modified List:", words_list)

# Attempt to modify the tuple (this will raise an error)
try:
    words_tuple[0] = "changed"
except TypeError as e:
    print("Cannot modify tuple:", e)
```

 **Explanation**:
- Lists can be modified (added, removed, changed).
- Tuples cannot be modified after creation — they are immutable.

---

## Step 3: Show Underlying Ordering

```python
print("Original List Order:", words_list)
print("Original Tuple Order:", words_tuple)
print("Set Order (may vary):", words_set)
```

**Explanation**:
- List and tuple preserve the word order.
- Set does **not** preserve order and removes duplicates.

---

## Step 4: Convert Between Structures

```python
# Convert set to list
set_to_list = list(words_set)

# Convert list to set
list_to_set = set(words_list)

# Convert list to tuple
list_to_tuple = tuple(words_list)

print("Set to List:", set_to_list)
print("List to Set:", list_to_set)
print("List to Tuple:", list_to_tuple)
```

**Explanation**:
- Conversions are easy in Python but affect order and mutability.
- Useful for deduplicating (set) or locking structure (tuple).

---

## Use Case Summary

| Structure | Ordered | Mutable | Allows Duplicates | Use Case Example                 |
|-----------|---------|---------|-------------------|----------------------------------|
| List      | Yes     | Yes     | Yes               | Sequence of steps or results     |
| Tuple     | Yes     | No      | Yes               | Fixed config values or arguments |
| Set       | No      | Yes     | No                | Unique test IDs or keywords      |

---

## Bonus: Word Count Dictionary

### Problem:
Create a dictionary that counts the number of times each word appears in the sentence.

### Solution:
```python
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print("Word Counts:", word_counts)
```

 **Explanation**:
- `get(word, 0)` handles new words gracefully.
- Great for summarizing logs, test results, and counts in reports.

---
