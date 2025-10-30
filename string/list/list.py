
#list methods and operations in Python
#append, insert, remove, pop, index, count, 
# sort, sorted, reverse, extend, copy, copied, clear



#creating an empty list
my__empty_list = list()
empty_empty_list2 = []
#creating a list with initial elements
my_list1 = [1, 2, 3, 4, 5]
my_list2 = ["Hi", "Great", "Hello", 3.14, "Hello", "Hello"]

print("print the element with index 2 in the list :", (my_list2[2]))  #Accessing elements by index

my_list2[1] = "Wonderful"  #Modifying elements
print(("Print the list with changed element on the position 1:", (my_list2)))

append_element = my_list2.append("New Element")  #Adding elements
print(("Print the list after appending 'New Element':", (my_list2)))

insert_element = my_list2.insert(2, "Inserted Element")  #Inserting elements at specific position
print(("Print the list after inserting 'Inserted Element' at index 2:", (my_list2)))

list_length = len(my_list2)  #Getting the length of the list
print("Length of the list is:", list_length)

list_slice = my_list2[1:4]  #Slicing the list
print("Sliced list from index 1 to 3:", list_slice)

list_concatenation = my_list1 + my_list2  #Concatenating lists
print("Concatenated list:", list_concatenation) 

list_repetition = my_list1 * 2  #Repeating lists
print("Repeated list:", list_repetition)    

list_removal = my_list2.remove(3.14)  #Removing elements
del my_list2[0]  #Deleting elements by index
print(("Print the list after removing '3.14':", (my_list2)))

popped_element = my_list1.pop()  #Popping the last element in the list
popped_element_index = my_list1.pop(1)  #Popping element at specific index
print("Popped element:", popped_element)
print("Popped element at index 1:", popped_element_index)
print("List after popping an element:", my_list1)

list_index = my_list2.index("Hi")  #Finding index of an element
print("Index of 'Hi' in the list:", list_index)

list_count = my_list2.count("Hello")  #Counting occurrences of an element
print("Count of 'Hello' in the list:", list_count)

my_list2.sort()  #Sorting the list
print("Sorted list:", my_list2) 
sorted_list =sorted(my_list1)  #Sorting using sorted() function

my_list2.reverse()  #Reversing the list
print("Reversed list:", my_list2) 

print(my_list2[1].upper())  #Using string method on list element
print(my_list2[2].lower())  #Using string method on list element
print(my_list2[0].title())  #Using string method on list element

print(my_list2[-5])  #Accessing elements using negative indexing

extended_list = my_list1.extend([6, 7, 8])  #Extending the list with another list
print("Extended list:", my_list1)

copied_list = my_list2.copy()  #Copying the list
print("Copied list:", copied_list)

sorted_list = sorted(my_list1)  #Creating a sorted copy of the list
print("Sorted copy of the list:", sorted_list)  

reversed_list1 = copied_list.sort(reverse=True)  #Creating a reversed copy of the list

cleared_list = my_list1.clear()  #Clearing all elements from the list
print("Cleared list:", my_list1)
