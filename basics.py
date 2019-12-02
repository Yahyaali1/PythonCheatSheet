student_count = 10
is_out = 4.9
multiple_line_string = """
This is multiple line string
"""
print(student_count)

# Multiple variables can be init as well

x, y = 1, 2
x = y = 1

# Python is a dynamic language

x_int = 1
print(type(x_int))
# All the integer are from class int

# we can define type annotations as well

x_int_annotated: int = 10
x_str_annotated: str = "string"
x_int_annotated = x_str_annotated  # this is still valid

# Mutable and immutable types
# Primitive types are immutable
x_mut = 1
print(id(x_mut))
x_mut = x_mut + 1
print((id(x_mut)))  # Value is stored in new memory location

x_immut = [1, 2, 3]
print(id(x_immut[0]), "Value for variable at index 0 before change value:", x_immut[0])
print(id(x_immut), "Value for list variable")
x_immut[0] = 2
print(id(x_immut[0]), "Value for variable at index 0 value:", x_immut[0])
print(id(x_immut), "Value for list variable")

# Strings
x_str: str = "Python String"
print(len(x_str))
# Square brackets for accessing
print(x_str[0])
# -1 index for wrapping around the end
print(x_str[-1])
# [start:end(not included)] for substring
print(x_str[0:3])
# def value for start = 0 and end = len of string
print(x_str[1:])
print(x_str[:3])
# using bracket notation allocate new memory

# Escape Character
x_escape = "Hello World"
print(x_escape)

# Back slash is considered as escape character
# \" \\ \' \n
x_escape = "Hello \" World"
print(x_escape)

# Formatted strings
# Value is evaluated at runtime
# curly braces can include any valid expression
first = "Yahya"
last = "Ali"
full_name = f"{first} {last}"
full_name_exp = f"{len(first)}"
print(full_name)
print("Valid Expression example", full_name_exp)

# Operators
# - Div for int and floating point
# Exponent operators
# Augmented Operator

class A:
    def __init__(self, *b,**a):
        self.__a="parent" + str(a) + str(b)
        self.normal = "normal"
    
    def read_class_args(self):
        return self.__class__.__dict__.items()   

    def read_inst_args(self):
        return self.__dict__.items()

    def __str__(self):
        return self.__a

class B(A):
    c = "A"
    def __str__(self):
        self._a = "Hello world"
        self.normal = "Normal2"
        return self._a + self.normal


A = A(a="a", b="b", c="c")
second = B(a="a", b="b", c="c")

class C:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def __str__(self):
        return self.a + self.b


second.__class__.c = " changed"
print(second)
print(A)
print(A.read_class_args(), "Expression")
print(second.read_inst_args(), "Expression  Instance args")
print(second.read_class_args(), "Expression  class args")

print(C(**{"a":"a","b":"b", "d":"d"}))


