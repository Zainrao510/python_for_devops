import psutil

#list is data structure that is used to store multiple items in a single variable. or multiple types of data can be stored in a list. list is mutable, ordered and allows duplicate values.
#array is a data structure that hold multiple items of the same data type. array is mutable, ordered and allows duplicate values.

names = ["zain", "ali", "ahmed", "usman", "bilal"]

names.append("hamza") #add an item to the end of the list
names.insert(2, "hassan") #add an item at a specific index
names.remove("usman") #remove an item from the list
names.pop() #remove the last item from the list
names.sort() #sort the list in ascending order
names.reverse() #reverse the order of the list
names.extend(["umer", "saad"]) #add multiple items to the end of the list

for name in names:
    print(name)

for i in range(5):
    print(psutil.cpu_percent(interval=1))