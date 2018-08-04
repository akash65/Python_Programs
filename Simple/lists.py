list = ["arun","arun","ajay",34,23,23]
numbers = [34,234,5,23,5555]
print(list)
print(list[2:])
print(list[:3])
list.extend(numbers)
print(list)
list.append("simon")
print(list)
list.insert(3,"sush")
print(list)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
list.pop()
print(list)


def sum(num1,num2):
    val = num1+num2
    print(val)

sum(23,34)