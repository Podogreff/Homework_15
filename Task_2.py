class Dog:
    def __init__(self, age_factor="dfgdsgdsg"):
        self.age_factor = age_factor

    def human_age(self):
        if isinstance(self.age_factor, str) and self.age_factor.isnumeric() or isinstance(self.age_factor, int):
            return f"The {self.age_factor} years dog is equals {int(self.age_factor) * 4} human years"
        else:
            raise TypeError("Age of the dog should be digit or number")


human = Dog()
print(human.human_age())

