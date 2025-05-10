
Company_names_location={"HCLTech":"Mumbai","TCS":"Mumbai","WIPRO":"Mumbai","JUNIPER":"Banglore","TEJAS NETWORKS":"Banglore"}

print(Company_names_location.items())
#dict_items([('HCLTech', 'Mumbai'), ('TCS', 'Mumbai'), ('WIPRO', 'Mumbai'), ('JUNIPER', 'Banglore'), ('TEJAS NETWORKS', 'Banglore')])

'''In Python, the .items() method on a dictionary does not return a list directly. Instead, it returns a view object that behaves like a dynamic iterable view of the dictionary’s key-value pairs.
To get a list of the items, you can convert it:
    dict.items() → returns a view (dict_items)

list(dict.items()) → returns a list of (key, value) tuples
    
Dictionaries in Python are not indexed by position, but by keys. So you cannot access dictionary items using numeric indices like you would with a list.'''

print(Company_names_location)
#{'HCLTech': 'Mumbai', 'TCS': 'Mumbai', 'WIPRO': 'Mumbai', 'JUNIPER': 'Banglore', 'TEJAS NETWORKS': 'Banglore'}

names_list=list(Company_names_location.items())
print(f"Converted Dict into List {names_list}")

#Converted Dict into List [('HCLTech', 'Mumbai'), ('TCS', 'Mumbai'), ('WIPRO', 'Mumbai'), ('JUNIPER', 'Banglore'), ('TEJAS NETWORKS', 'Banglore')]

print(Company_names_location.keys())
#dict_keys(['HCLTech', 'TCS', 'WIPRO', 'JUNIPER', 'TEJAS NETWORKS'])
key_list= list(Company_names_location.keys())
print(key_list[0])

print(Company_names_location.values())
#dict_values(['Mumbai', 'Mumbai', 'Mumbai', 'Banglore', 'Banglore'])


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 3, 'd': 5}


dict1_keys=dict1.keys()
dict2_keys=dict2.keys()
print(dict1_keys)
#dict_keys(['a', 'b', 'c'])
print(dict2_keys)
#dict_keys(['b', 'c', 'd'])
dict1_values=set(dict1.values())
dict2_values=set(dict2.values())
print(dict1_values)
#{1, 2, 3}
print(dict2_values)
#{2, 3, 5}
#In Python, dictionaries don't directly support set operations like intersection and union, but you can apply those operations to their keys, values, or items using the set type.
#For intersection we can use & and for union we can use | 

comman_keys= dict1_keys & dict2_keys
print(f"Comman in both keys: {comman_keys}")
#Comman in both keys: {'c', 'b'}
comman_values= dict1_values & dict2_values
print(f"Comman in both values: {comman_values}")
#Comman in both values: {2, 3}

not_comman_keys= dict1_keys ^ dict2_keys
print(f"Not Comman in both keys: {not_comman_keys}")
#Not Comman in both keys: {'a', 'd'}
not_comman_values= dict1_values ^ dict2_values
print(f"Not Comman in both values: {not_comman_values}")
'''while in difference if dict1 dont have a key and dict2 have it, in differance it ignores the key of dict2
#Not Comman in both values: {1, 5}

ChatGPT said:
You're absolutely right — and that's a key detail when working with set difference in dictionaries.
When you do:

diff_keys = dict1.keys() - dict2.keys()
This gives you:

Keys that are in dict1 but not in dict2.

So, any key that's only in dict2 gets ignored, because you're subtracting dict2.keys() from dict1.keys() — not the other way around
o Include All "Not Common" Keys (from both dictionaries):
You should use symmetric difference:


not_common_keys = dict1.keys() ^ dict2.keys()
print(not_common_keys)
This gives you:

All keys that are in either dict1 or dict2, but not in both.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

print(dict1.keys() - dict2.keys())  # {'a'}
print(dict2.keys() - dict1.keys())  # {'c'}
print(dict1.keys() ^ dict2.keys())  # {'a', 'c'}

'''
for key,value in dict1.items():
    if key in not_comman_keys or value in not_comman_values:
        print({key:value})
#{'a': 1}
#output dict3 = {'a':1,'d':5}

dict3 = dict1.items() ^ dict2.items()
print(f'Using Symmetric difference: {dict3}')
#Using Symmetric difference: {('d', 5), ('a', 1)}

