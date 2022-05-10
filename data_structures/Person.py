class Person:
    """Class Person displaying person info\n"""
    # class variable
    person_total = 0

    def __init__(self, name, age, height, occupation):
        self.name = name
        self.age = age
        self.height = height
        self.occupation = occupation
        Person.person_total += 1

    def display(self):
        print("{} is {} years old and {} cm tall.".format(self.name, self.age, self.height))

    # getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHeight(self):
        return self.height

    # round to 2 decimal places
    def getHeightInInches(self):
        return round(self.height / 2.54, 2)

    def getOccupation(self):
        return self.occupation

    # setters
    def setName(self, new_name):
        self.name = new_name

    def setAge(self, new_age):
        self.age = new_age

    # height set in cm
    def setHeight(self, new_height):
        self.height = new_height

    def setOccupation(self, new_occupation):
        self.occupation = new_occupation

    # manip
    def hadBirthday(self):
        self.age += 1


# printing doc string
print(Person.__doc__)
# creating class instances
person1 = Person('John', 40, 96, 'salesman')
person2 = Person('Lila', 32, 102, 'artist')
person3 = Person('Ariel', 18, 130, 'mermaid princess')

dmv_queue = {'1': person1, '2': person2, '3': person3}

# access w/ key
for key in dmv_queue:
    dmv_queue[key].display()

# list w/ tuple
queue_items = dmv_queue.items()
for item in queue_items:
    item[1].display()


print('\nThe queue has {} {}.\n'.format(Person.person_total, 'person' if Person.person_total == 1 else 'people'))
