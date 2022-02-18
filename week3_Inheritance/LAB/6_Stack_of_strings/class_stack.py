class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        last_element = self.data[-1]
        self.data = self.data[:-1]
        return last_element

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return True if not self.data else False

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


st = Stack()
st.push("4")
st.push("5")
print(st.pop())
print(st)
print(st.top())
print(st.is_empty())
print(st)
st.pop()
print(st.is_empty())