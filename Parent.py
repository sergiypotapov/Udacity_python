__author__ = 'spotapov'
class Parent():
    def __init__(self, last_name, eyes):
        print("Parent constructor was called")
        self.last_name = last_name
        self.eyes = eyes
    def show_info(self):
        print("Name " + self.last_name)
        print("Eyes " + self.eyes)

class Child(Parent):
    print("Child cunstructior is working")
    def __init__(self, last_name, eyes, toys):
        Parent.__init__(self, last_name, eyes)
        self.toys = toys
    def show_info(self):
        print("Bamboleo!")
#billy_cyrys = Parent("cyrys", "blues")
#print(billy_cyrys.last_name+billy_cyrys.eyes)
#billy_cyrys.show_info()
miley_cyrys = Child("cyrys", "blues", "5")
#print(miley_cyrys.toys)
miley_cyrys.show_info()