#Take input from user
n=int(input("Enter the number of rows :"))

print("Pyramid Pattern")
for i in range(1,n+1):
    spaces=" " * (n-i)
    stars="* "*i
    print(spaces+stars)