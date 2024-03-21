# Two different types of varible can't be printed simultaneously
# As an example

# print(7 + "Learn Python" + " with Towhid Hossain Alvi")  ---- > wrong

# So we have to all the variable same 
# print(str(7) + " Learn Python" + " with Towhid Hossain Alvi")  --- > here all '1' is integer variable and I converted it into sting (str)

x = 100 
print(str(x) + " = " +  str(type(x)))


y = 3.1416
print(str(y) + " = " +  str(type(y)))

z = 'a'
print(str(z) + " = " +  str(type(z)))

w = "Towhid Hossain Alvi"
print(str(w) + " = " +  str(type(w)))


a = (1,2,3,4,5)  
print(str(a) + " = " +  str(type(a)))


b = {1,2,3,4,5}   
print(str(b) + " = " +  str(type(b)))

c = [1,2,3,4,5]   
print(str(c) + " = " +  str(type(c)))



d = {'name': 'John', 'age': 30}
print(str(d) + " = " +  str(type(d)))

e = True
print(str(e) + " = " +  str(type(e)))

