
#ZADANIE 2
numbers=(0,100)
cube_list=[]
for number in range(0,100):
    if number % 5 == 0:
        print(number)

print()
print()


cube_list= [number**3 for number in range (0,100) if number % 5 == 0]
print(cube_list)