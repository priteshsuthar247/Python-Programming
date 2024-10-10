def tuple_operations():
    print("Demonstarion of tuple operations.")
    t1 = (1, 2, 3, 4, 5)
    print(f"Original tuple t1 is: {t1}")
    t2 = t1[1:3]
    print(f"Slicing tuple t1 reults in: {t2}")
    t3 = t1 + t2
    print(f"Concatnating t1 and t2 results in: {t3}")
    t4 = t1 * 2
    print(f"Performing repeatation on t1 results in: {t4}")
    print(f"Is 9 present in tuple t1: {9 in t1}")
    print(f"length of tuple t2 is: {len(t1)}")

def list_operations():
    print("Demonstarion of list operations.")
    l1 = [1, 2, 3, 4, 5]
    print(f"Original tuple t1 is: {l1}")
    l2 = l1[1:3]
    print(f"Slicing tuple t1 reults in: {l2}")
    l3 = l1 + l2
    print(f"Concatnating t1 and t2 results in: {l3}")
    l4 = l1 * 2
    print(f"Performing repeatation on t1 results in: {l4}")
    print(f"Is 9 present in tuple t1: {9 in l1}")
    print(f"length of tuple t2 is: {len(l1)}")

def dictionary_operations():
    print("Demonstarion of dictionary operations.")
    d1 = {'Name': 'Charlie',
               'Age' : 35,
               'City': 'Los Angeles'
        } 
    print(d1)
    d2=d1
    print("Deleting City from the dictionary")
    del d2['City'] 
    print(d2) 
    print("Is Age present in dictionary:", 'Age' in d1)
    d3 = {'Gender': 'Male',
               'Salary' : 150
        }
    print("Merging d1 and d4")
    d4 = d1 | d3
    print(d4)
    
tuple_operations()
print()
list_operations()
print()
dictionary_operations()