z=0.1+0.1+0.1-0.3

print(z) # this will give exact value


import decimal

print(
    decimal.Decimal('0.1')+
    decimal.Decimal('0.1')+
    decimal.Decimal('0.1')-
    decimal.Decimal('0.3')
    )




# type()
# id()
# isinstance()


xz=(9,8,7,"two",True)

print(type(xz))
print(id(xz)) #gives unique value
print(isinstance(xz,list))