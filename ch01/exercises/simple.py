# part 1
print(10 * 5)
print(10**2)
print(15 / 10)
print(15 // 10)
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
print(10 / 15)  # not exact, trailing 6's

# part 2
rate = float(input("What is the current exchange rate from Euros to Dollars? "))
amount = float(input("How much currency do you want to exchange? "))
total = amount * rate
result = total - 3
print(f"You will have ${result:.2f} after deducting the processing fee.")
