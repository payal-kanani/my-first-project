'''
#Iterating over a List
fruits = ["Apple", "Banana" ,"Cherry", "Mango"]
for fruit in fruits:
    print(fruit)


#Iterating over a String
word = 'Hello'
for char in word:
    print(char)


for i in range(0,100,10):
    print(i)


foods = ['Pizza', 'Burger', 'Pasta', 'Salad']
for index in range(len(foods)):
    print(index, foods[index])
print(foods)
'''


#while loop
'''
i = 1
while i <= 5:
    print(i)
    i += 1
print("loop ended")

# braek statement
i = 1
while i <=10:
    if i>7:
        break
    print(i)
    i += 1
print("loop ended")


i = 1
while i < 10:
    i += 1
    if i < 6:
        continue
    print(i)
print("loop ended")


i = 2
while i < 10:
    j = 2
    while j*j <= i:
        if not i % j:
            break
        j += 1
    if j > i/j:
        print(f'{i} is a prime number')
    i += 1
print("loop ended")
'''

num = int(input("Pleanse enter a number: "))


if num <= 1:
    print(f"{num} is not a prime number")
elif num == 2:
    print(f"{num} is a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")