#write a python program to define a function which prints a multiplication table from 1 to n?
def print_table(n):
    for i in range(1,11):
        print(n,"x",i,"=",(n*i))
    for j in range(1,5):
        print("10*5:5",11)
    print("-------------------------")
#function call
print_table(5)
print_table(7)
print_table(18)