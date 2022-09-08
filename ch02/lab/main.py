import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 3
print(classes_per_week, type(classes_per_week))
cost_per_class = cost_per_week / classes_per_week
print(cost_per_class, type(cost_per_class))
print("Your cost per class amount to:", cost_per_class)


#Part B
keyboardSwitches = ["alpaca", "cream", "tangerine", "boba", "zealio", "oil king", "silk", "cherry", "gateron", "kalih"]
switchChoice = random.choice(keyboardSwitches)
print(f"You should build your next keyboard using {switchChoice} switches.")