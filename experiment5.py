5.	##Write a python program to find sum of all even numbers between 1 to n.##
n = int(input("Enter a number: "))
sum = 0
i = 2

while i <= n:
    sum += i
    i += 2

print("Sum =", sum)