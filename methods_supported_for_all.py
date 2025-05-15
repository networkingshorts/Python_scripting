✅ Commonly Used List Methods
Method	Description
append(x)	Adds x to the end of the list.
extend(iter)	Extends list by appending elements from another iterable.
insert(i, x)	Inserts x at index i.
remove(x)	Removes first item with value x.
pop([i])	Removes and returns item at index i (default last).
clear()	Removes all items from the list.
index(x)	Returns index of first item with value x.
count(x)	Returns the count of x in the list.
sort()	Sorts the list in-place (ascending by default).
reverse()	Reverses the list in-place.
copy()	Returns a shallow copy of the list.

🔹 pop() without an index removes the last element.
🔹 pop(i) removes the element at index i.

🔁 Supported List Operators
Operator	Description
+	Concatenation: [1, 2] + [3] → [1, 2, 3]
*	Repetition: [1, 2] * 3 → [1, 2, 1, 2, 1, 2]
in / not in	Membership test
len(list)	Returns number of items
list[i]	Index access
list[i:j]	Slicing
list[i] = x	Item assignment
del list[i]	Delete element
del list[i:j]	Delete a slice


🧼 Whitespace and Casing
Method	Description
strip()	Removes leading/trailing whitespace
lstrip()	Removes leading whitespace
rstrip()	Removes trailing whitespace
lower()	Converts all characters to lowercase
upper()	Converts all characters to uppercase
capitalize()	Capitalizes the first character
title()	Capitalizes the first character of each word
swapcase()	Swaps case: upper ↔ lower

🔍 Searching and Counting
Method	Description
find(sub)	Returns index of first occurrence, or -1
rfind(sub)	Returns index of last occurrence, or -1
index(sub)	Like find() but raises ValueError if not found
rindex(sub)	Like rfind() but raises error if not found
count(sub)	Returns number of occurrences of substring

🔄 Replacing and Splitting
Method	Description
replace(old, new)	Replaces all occurrences of old with new
split(sep)	Splits string into list at separator
rsplit(sep)	Splits from the right
splitlines()	Splits at line breaks
partition(sep)	Splits into a 3-tuple: before, sep, after
rpartition(sep)	Right-side partition

🔤 String Testing (Returns True/False)
Method	Description
startswith(sub)	Checks if string starts with substring
endswith(sub)	Checks if string ends with substring
isalpha()	All characters are letters
isdigit()	All characters are digits
isalnum()	All characters are alphanumeric
isspace()	All characters are whitespace
islower()	All letters are lowercase
isupper()	All letters are uppercase
istitle()	True if string is in title case

🧱 Padding and Alignment
Method	Description
center(width)	Centers string with spaces
ljust(width)	Left-justifies string
rjust(width)	Right-justifies string
zfill(width)	Pads string on the left with zeros

🔧 Encoding & Other Utilities
Method	Description
encode()	Encodes string to bytes
format()	Formats string with placeholders
format_map(dict)	Like format() but uses a dictionary
casefold()	Aggressive lowercasing for comparison
maketrans()	Used with translate() to replace characters
translate(mapping)	Replaces characters using a translation table



📘 Common Dictionary Methods
Method	Description
get(key[, default])	Returns the value for key, or default if not found
keys()	Returns a view of all keys
values()	Returns a view of all values
items()	Returns a view of all key-value pairs as tuples
update([other])	Updates the dictionary with another dictionary or key-value pairs
pop(key[, default])	Removes specified key and returns its value
popitem()	Removes and returns the last inserted key-value pair
clear()	Removes all items from the dictionary
copy()	Returns a shallow copy of the dictionary
setdefault(key[, default])	Returns value if key exists; sets it to default if not
fromkeys(seq[, value])	Creates a new dictionary from a sequence of keys and a value


✅ Basic Set Methods
Method	Description
add(elem)	Adds elem to the set
remove(elem)	Removes elem; raises KeyError if not found
discard(elem)	Removes elem if present (no error if not)
pop()	Removes and returns an arbitrary element
clear()	Removes all elements from the set
copy()	Returns a shallow copy

🔁 Set Operations
Method	Description
union(other) or `	`
intersection(other) or &	Returns a set with common elements
difference(other) or -	Elements in set but not in other
symmetric_difference(other) or ^	Elements in either set, but not both

🧪 In-place Set Operations
These modify the original set:

Method	Description
update(other)	Adds elements from other (like `
intersection_update(other)	Keeps only elements found in both (like &=)
difference_update(other)	Removes elements found in other (like -=)
symmetric_difference_update(other)	Updates to elements in either, but not both (like ^=)

🧠 Set Comparison & Testing
Method	Description
issubset(other) or <=	Checks if current set is a subset of other
issuperset(other) or >=	Checks if current set is a superset of other
isdisjoint(other)	Checks if sets have no elements in common

