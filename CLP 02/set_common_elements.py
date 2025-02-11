list1 = list(map(int, input("Enter first list numbers: ").split()))
list2 = list(map(int, input("Enter second list numbers: ").split()))
common_elements = set(list1) & set(list2)
print("Common Elements:", common_elements)
