class student:
    grade = 10
    print("Hi i am a student of grade",grade)

ob = student()



class Vehicle:
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage


vehicle1 = Vehicle(240, 18)


print("The max speed of vehicle is", vehicle1.max_speed)
print("The mileage of vehicle is", vehicle1.milage)



#class parrot
class Parrot:
    #class attributes/variables
    species = "bird"
    #instance attributes/variables
    def __init__(self, name, age):
        self.name = name
        self.age = age

#instances of class parrot
a = Parrot("Aarav",10)
b = Parrot("Ishan",7)

print(a.name, a.age, a.species)
print(b.name, b.age, b.species)