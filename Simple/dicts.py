dict = {'id':123,'name':"arjun",'age':23,'address':"chennai"}
print(dict)
print(dict['name'])

monthconvers = {
    "jan": "january",
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "m": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sep": "september",
    "oct": "october",
    "nov": "november",
    "dec": "december"

}
print(monthconvers["jul"])
print(monthconvers.get('dec'))

#power calculation using for loop
def pow_using_for(base,pow):
    result = 1
    for count in range(pow):
        result = result * base
    return result

print(pow_using_for(3,10))


#replace alphabets with vowels
def rep_vowels(string):
    sub_string = ""
    for letter in string:
        if letter in "aeiou":
            sub_string = sub_string +'m'
        else:
            sub_string = sub_string +'M'
    return sub_string

print(rep_vowels(input("enter the string: ")))


#file operation
employees = open("employee.txt", "r")

#for value in employees.read():
#for value in employees.readline():
for value in employees.readlines():
    print(value)

employees.close()

