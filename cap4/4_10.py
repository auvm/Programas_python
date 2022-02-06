#from exercise 4_9.py 

ten_cubes = [i**3 for i in range(1,11)]
import py_compile

print("The complete list is: \n",ten_cubes)

print("The first three items in the list are: ",ten_cubes[:3])
print("Three items from the middle of the list are: ",ten_cubes[4:7])
print("The last three items in the list are: ",ten_cubes[-3:])
