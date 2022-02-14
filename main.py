import random
#Part A
weeks = 16
classes = 5
tuition = 6000
classes_per_week = 3
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
cost_per_class = ((cost_per_week/classes_per_week))
print("Cost per class:", cost_per_class)
#Part B
mylist = ("abc","100","1","computer science","10.99")
result = random.choice(mylist)
print(result)