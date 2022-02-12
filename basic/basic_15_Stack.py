class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return not self.items

stk = stack()
print(stk.isEmpty())
stk.push(1)
stk.push(2)
print(stk.pop())
print(stk.pop())
print(stk.isEmpty())

def push(a):
    lst.append(a)
def pop():
    del lst[len(lst)-1]
def peek():
    print(lst[len(lst)-1])

lst = []

push(15)
push(54321)
push(1)
push("hi")
push("˚¬˚")

print(lst)

pop()
peek()
print(lst)
