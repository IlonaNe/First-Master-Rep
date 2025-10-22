#creating an empty list
my__empty_list = list()
empty_empty_list2 = []
#creating a list with initial elements
my_list1 = [1, 2, 3, 4, 5]
my_list2 = ["Hi", "Great", 4, "Hello", 3.14]
print(my_list2[2])  #Accessing elements by index
my_list2[1] = "Wonderful"  #Modifying elements
append_element = my_list2.append("New Element")  #Adding elements
print(my_list2.lower())  #This will raise an error because 'list' object has no attribute 'lower'