#Maria Loren I. Ignacio
#https://github.com/lorenignacio
#lorenignacio00@gmail.com
#Remove Duplicate



class Stack:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5, 6]

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def byeduplicate(self):
        return byeduplicate(self.items)


if __name__ == "__main__":
    s = Stack()
    x = 0
    while x <= 100:
        s.push(x)
        x += 1

    Stack = input("Enter numbers:")
    Stack = list(Stack)
    s = []

    for i in Stack:
        if i not in s:
            s.append(i)

    print s
