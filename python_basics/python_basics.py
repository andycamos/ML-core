
# types

print(type(10))
print(type(2.718))
print(type("hello"))

x = 10
print(x)
x = 100
print(x)

y = 3.14
x = x * y

print(type(x))


# list
a = [1,3,5,7,9]

print(a)
print(len(a))

print(a[0])
print(a[-1])

print(a[0:3:2])

# dict key-value
b = {"apple": 3, "milk":2 }
print(b["apple"])

# function
def hello(object):
    print(f"hello {object}")

hello("cat")

# class
class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")
    def hello(self):
        print(f"Hello {self.name}!")
    def goodbye(self):
        print(f"Goodbye {self.name}!")


m = Man("David")
m.hello()
m.goodbye()