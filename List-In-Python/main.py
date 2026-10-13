countries = ["Nigeria", "United Kingdom", "Canada", "Tokyo", "Benin", "Niger"]
print(countries[1])
print(countries[2:])
print(countries[3][2])

list1 = [1,2,3,4]
list2 = ["Banana", "Apple", "Orange", "Mango"]
list1.extend(list2)

list2.append('PineApple')
print(list2)

list2.insert(1, 'Cherry')
print(list2)

list2.remove('Banana')
print(list2)

list2.clear()
print(list2)

list1.sort()
print(list1)