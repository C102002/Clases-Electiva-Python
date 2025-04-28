x, y = 2, 4
 
print("x = ", x, ", y =", y)
 
print("\nx + y =", x + y)
print("x.__add__(y) =", x.__add__(y)) # igual que x + y
 
print("\nx * y = ", x * y)
print("x.__mul__(y) = ", x.__mul__(y)) # igual que x * y
 
print("\nx / y = ", x / y)
print("x.__truediv__(y) = ", x.__truediv__(y)) # igual que x / y
 
print("\nx ** y = ", x ** y)
print("x.__pow__(y) = ", x.__pow__(y)) # igual que x ** y
 
print("\nx % y = ", x % y)
print("x.__mod__(y) = ", x.__mod__(y)) # igual que x % y
 
print("\nx == y = ", x == y)
print("x.__eq__(y) = ", x.__eq__(y)) # igual que x == y
 
print("\nx != y = ", x != y)
print("x.__ne__(y) = ", x.__ne__(y)) # igual que x != y
 
print("\nx >= y = ", x >= y)
print("x.__ge__(y) = ", x.__ge__(y)) # igual que x >= y
 
print("\nx <= y = ", x <= y)
print("x.__le__(y) = ", x.__le__(y)) # igual que x <= y
print("------------------------------------------")
 
str1 = "special methods"
 
print("\nstr1 =", str1)
 
print("\n'ods' in str1 =", "ods" in str1)
print("str1.__contains__('ods') =", str1.__contains__("ods")) # igual que "ods" in str1
 
print("\nlen(str1) =", len(str1))
print("str1.__len__() =", str1.__len__()) # igual que len(str1)
print("------------------------------------------")
 
list1 = [11,33, 55]
 
print("\nlist1 =", list1)
 
print("\nlist1[1] =", list1[1])
print("list1.__getitem__(1) =", list1.__getitem__(1)) # igual que list1[1]
print("str(list1) =",str(list1)) # igual que list1.__str__()
print("list1.__str__() =", list1.__str__())