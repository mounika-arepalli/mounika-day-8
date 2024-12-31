#write a python program to define a function which prints a multiplication table?
def print_table(n):
    for i in range(1,11):
        print(n,"x",i,"=",(n*i))
    print("-------------------------")
#function call
print_table(5)
print_table(7)
print_table(18)