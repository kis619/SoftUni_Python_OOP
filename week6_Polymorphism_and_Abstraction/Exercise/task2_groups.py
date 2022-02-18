class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, second_person):
        return Person(self.name, second_person.surname)

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_group = self.people + other.people
        new_name = f"{self.name} {other.name}"
        return Group(new_name, new_group)

    def __getitem__(self, index):
        return f"Person {index}: {repr(self.people[index])}"

    def __repr__(self):
        members = ', '.join(repr(person) for person in self.people)
        return f"Group {self.name} with members {members}"


p0 = Person("Aliko", "Dangote")
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3
first_group = Group("__VIP__", [p0, p1, p2])
second_group = Group("Special", [p3, p4])
third_group = first_group + second_group
print(len(first_group))
print(second_group)
print(third_group[0])
for person in third_group:
    print(person)

""" object.__getitem__(self, key)

    Called to implement evaluation of self[key]. For sequence types, 
the accepted keys should be integers and slice objects. 
Note that the special interpretation of negative indexes 
(if the class wishes to emulate a sequence type) is up to the __getitem__() method.
If key is of an inappropriate type, TypeError may be raised;
if of a value outside the set of indexes for the sequence (after any special interpretation of negative values),
IndexError should be raised. For mapping types, if key is missing (not in the container), KeyError should be raised.

Note

for loops expect that an IndexError will be raised for illegal indexes
to allow proper detection of the end of the sequence."""
