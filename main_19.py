class Food:
    def __init__(self, foodname, cuisine, ftype):
        self.foodname = foodname
        self.cuisine = cuisine
        self.ftype = ftype

    def getfullCourse(self):
        return self.foodname + "\n" + self.cuisine + "\n" + self.ftype
    
meal1 = Food("parotta", "south Indian", "main course")
meal2 = Food("carrot halwa", "vadakan", "dessert")

print(meal1)
print("food name - ", meal1.foodname)
print("cuisine - ", meal1.cuisine)
print("ftype - ", meal1.ftype, "\n")

print(meal2)
print("food name - ", meal2.foodname)
print("cuisine - ", meal2.cuisine)
print("ftype - ", meal2.ftype)


