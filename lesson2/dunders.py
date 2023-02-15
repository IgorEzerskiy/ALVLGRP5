class Employee:
    def __init__(self, name, weight, age, gender):
        self.name = name
        self.weight = weight
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name}"

    def __lt__(self, other):
        return self.weight * .6 + self.age * .4 < other.weight * .6 + self.age * 0.4

    def __le__(self, other):
        return self.weight <= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __getattribute__(self, item):
        if item == 'age' and self.gender == 'F':
            raise ValueError
        return super().__getattribute__(item)

    # def __add__(self, other):
    #     return self.__class__(name=f"{self.name} {other.name}"...)

    # def __call__(self, task_id):
    #     print(f'{self.name} working on {task_id}')

    def __dict__(self):
        pass
    # def __repr__(self):
    #     return f"{self.name}"


if __name__ == '__main__':
    mike = Employee('Mike', 90, 15, 'M')
    mike2 = Employee('Mike', 45, 40, 'M')
    jane = Employee('Jane', 50, 46, 'F')
    will = Employee('Will', 101, 90, 'M')

    # willmike =  mike + will  -> mike will, ['python', 'js', 'sql'], max([s1, s2])

    print(mike)
    print(mike2)
    print(will)
    print(jane)

    print(mike.weight < mike2.weight)
    print(mike.age < mike2.age)

    print(jane.age)

    # will(1235)
