x = str(3)
y = int(3)
z = float(5)
print(type(x), x, y+z)
a = 4
A = "Manoj"
print(a, A)
b,c,d = "Orange", "Banana","Cherry"
f = g = h = "Madhav"
print(f,g,h)
print(b,c,d)
fruits = ["apple", "banana", "cherry"]
q,w,e = fruits
print(q,w,e)
r = "awesome"

def myFunc():
    #global r
    r = 'fantastic'
    print("Python is "+r)

myFunc()
print("Python is "+r)