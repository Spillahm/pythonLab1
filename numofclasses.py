#ask how mny classes

num_of_classes = int(input("Enter the number of classes you are taking:"))
class_list = [] # empty class to store the class names4

#using for loop to ask for the name of each class

for c in range (0, num_of_classes):
    class_name = input(f"Enter the name of class number {c + 1}:")
    class_list.append(class_name)

#for loop to print each class in the list
for c in range(len(class_list)):
    print(f"Class { c+ 1}: {class_list[c]}")
