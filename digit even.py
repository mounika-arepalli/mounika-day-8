# print the digit is even or not?
result=lambda a:print("digit") if (a>=-9 and a<=9) else print("number")
result(45)
print("---------------------------------------")
result=lambda a:print("digit") if (a>=-99 and a<=99) else print("number")
result(98)
print("---------------------------------------")
result=lambda a:print("digit") if (a>=-999 and a<=999) else print("number")
result(467)