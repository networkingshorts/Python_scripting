#write a python program to reverse a list
list_of_numbers = [1,3,467,78,100,211,990]

reverse_list = list_of_numbers[::-1]
#print(reverse_list)

#write a python program to split the list and print the last number first and first numbers in last


split_list = len(list_of_numbers)//2

first_number = (list_of_numbers[:split_list])

last_number = (list_of_numbers[split_list::])

combined_list = last_number + first_number
#print(f"Lists are {combined_list}")


#check if a string is palindrome

s = "madamdefault"
#print(s[::-1])

#Print Fibonacci series: starts with two numbers 0 and 1, After that each subsequent numbers is the sum of the two preceding numbers 

Fibonacci = [0,1] # 0 and 1 is added in list
n = 100
for i in range(2,n):
    Fibonacci.append(Fibonacci[i-1]+Fibonacci[i-2]) #as i=2, 2-1 + 2-2 = 1, i=3 3-1 + 3-2 = 3 and so on
#print(Fibonacci)

#find the largest or smallest numbers in the list

maximum_number = max(list_of_numbers)
#print(maximum_number)

minimum_number = min(list_of_numbers)
#print(minimum_number)


#Print the Prime numbers

'''num = int(input("Enter The Number: "))
if num < 2:
    print("Not a Prime Number")
for i in range(2,int(num**0.5)+1): #If num is 100 square root of 100 is 10 which also represt 100**0.5=10, here range will be 2 to 11
#here +1 is added in range so for square root of 25, range will be 2,5 but i will count 2,3,4 to include 5 in iteration we need to add plus 1
#if num is 3, 3**0.5 = 1.732 which integer is 1, range will be (2,2) which is empty, for loop doesnt run at all
#3 is not divisible by any number other than 1 and itself, meaning it is a prime number
    if num % i == 0:
        #if remainder is 0 then it is not a prime number
        print(f"{num} is Not a Prime Number")
        break
else:
    print(f"{num} is a Prime Number")'''


#write a python code to print a pattern

rows = 5

for i in range(1,rows+1):
    #print('*'*i)


 #count vowels in a given word

 vowels = ['a','e','i','o','u']
 word = 'networkingshorts'
count = 0
for character in word:
    if character in vowels:
        count = count + 1
#print(count)

#Find the maximum number in the list

max_num = [1,45,67,34,100,888,976,567,456,789,345,778]
#print(max(max_num))


lst1 = [1, 2, 3]
lst2 = [4, 5, 6] 

lst3 = []

for i in range(0,3):
    lst3.append(lst1[i]+lst2[i])
    i=i+1
#print(lst3)

#https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/Python%20Coding%20Interview%20Questions%20(Beginner%20to%20Advanced).md#-beginner-level


#To reverse an integer
n = 345678
reverse_num = str(n)
#print(int(reverse_num[::-1]))

#Remove white spaces from a string

strings = "Hello! There, I am Tauheed, How are you?"
split_strings=strings.split(" ")
#split jb use hoga jb hume kisi cheeze se string ko split krna h, jaise yaha space se split kiya h humne
#print(split_strings)
#join ke aage hum . lagakr jisse hume join krna h string ko vo dena hota h yaha jaise humne space hataya string se
joined = "".join(split_strings)
#print(joined)

#Replace IP usimg split and join
IP_address = "192.168.1.1"

split_IP_address = IP_address.split(".")
#print(split_IP_address)
split_IP_address[-1]='5' 
new_ip = ".".join(split_IP_address)
#print(new_ip)

#Find the second largest number in a list

largest_num = [1,45,67,89,43,1334,567,432,567,890,1334]
#largest_num.sort()
#print(largest_num)
#max_num=max(largest_num)
#min_num = min(largest_num) 
#print(largest_num[-2])
largest = second_largest= float('-inf')

#Using For Loop
for num in largest_num:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
    #elif num > second_largest and num !=largest:
        second_largest = num
#print(second_largest)

'''✅ num > second_largest
This checks if the current number is bigger than the current second largest.
→ If it is, then it's a candidate to be the new second largest.

✅ and num != largest
This ensures that we don’t treat a duplicate of the largest number as second largest.'''


#Find all pair of list to sum of the number


#print(sum(largest_num))

'''Write a function that takes an IP address string and increments the last octet by 1.
Input: "192.168.1.10"
Output: "192.168.1.11"'''

#Input_by_user = (input("Enter IP Address: "))
#split_IP_address_2 = Input_by_user.split('.')
#split_IP_address_2[-1] = str(int(split_IP_address_2[-1]) + 1)
#print(split_IP_address_2)
#new_ip=".".join(split_IP_address_2)
#print(new_ip)
'''l=[1,2,3,4]
print(type(l))

import array as arr
a = arr.array[1,2,3]
#print(type(a))

set_1 = {1,2,3}
print(set_1[1])'''


'''input_string = "Tauheed Shaikh is learning Python"
chars_to_count = ['t', 'T', 'a', 'n']  # You can include any characters you want

# Create a dictionary to store counts
char_counts = {}

for char in chars_to_count:
    char_counts[char] = input_string.count(char)

# Print the counts
for key, value in char_counts.items():
    print(f"{key}: {value}")
    
    
    input_string = "Tauheed is doing not good in Python"
input_string_lower= input_string.lower()
print(input_string_lower)
Char_to_Count = ["t","p","e","o"]

Char_key_value={}

for char in Char_to_Count:
    Char_key_value[char] = input_string_lower.count(char)
print(Char_key_value)'''


'''Python_string = "Python is a Programming Language"
#output {m:2}
count_char= ["P","t","g","m","a"]

counting_char= {}

for char in count_char:
    counting_char[char] = Python_string.count(char)
print(counting_char)

{'P': 2, 't': 1, 'g': 4, 'm': 2, 'a': 4}

'''

'''dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
#print(dict1.keys())
intersection = {}
#print(dict1['a'])
for key in dict1:
    if key in dict2 and dict1[key] == dict2[key]:
        intersection[key]=dict1[key]

print(intersection)'''

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}

# Find common keys
common = dict1.keys() & dict2.keys()

# Create cleaned versions of both dicts
dict1_clean = {}
dict2_clean = {}

for k in dict1:
    if k not in common:
        dict1_clean[k] = dict1[k]

for k in dict2:
    if k not in common:
        dict2_clean[k] = dict2[k]

# Merge the cleaned dictionaries
result = dict1_clean.copy()
result.update(dict2_clean)

print(result)  # {'a': 1, 'd': 5}




'''Lists and tuples in Python differ significantly in their memory allocation strategies due to their 
mutability. Lists, being mutable, are allocated more memory than they currently need to accommodate 
potential appends or removals. This pre-allocation avoids frequent reallocations, enhancing 
performance during modifications. However, it results in higher memory consumption compared to tuples.
Tuples, on the other hand, are immutable, meaning their size and contents are fixed upon creation. 
This allows Python to allocate only the necessary memory to store the tuple's elements, leading to more 
memory-efficient storage, especially when dealing with a large number of elements. Furthermore, because 
tuples are immutable, they can sometimes take advantage of certain optimizations, such as interning for 
small tuples, which can further reduce memory usage by sharing memory with identical tuples.'''


sort_string='bca'
sort_list_string = list(sort_string)
sort_list_string.sort()
print(sort_list_string)

'''my_list = ["b", "c", "a"]
sorted_list = my_list.sort()  # WRONG: sorted_list will be None
print(sorted_list)            # Output: None
Correct Ways to Sort:
Option 1: Sort in-place

my_list = ["b", "c", "a"]
my_list.sort()
print(my_list)  # Output: ['a', 'b', 'c']
Option 2: Use sorted() to get a new sorted list

my_list = ["b", "c", "a"]
sorted_list = sorted(my_list)
print(sorted_list)  # Output: ['a', 'b', 'c']'''


s = "banana"
distinct_chars = set(s)
print(len(distinct_chars))
#output is 3

'''set does not add duplicate characters ?


ChatGPT said:
Exactly — in Python, a set does not allow duplicate elements. When you convert a string to a set, 
it keeps only one copy of each character.'''

'''index_list=['a', 'b', 'c']
index = [1,2,3]
zipped = list(zip(index_list,index))
print(zipped)

#[('a', 1), ('b', 2), ('c', 3)]'''