def percentage_to_letter(score=0):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def is_passing(letter=None):
    return letter in "ABC"


score = int(input("Enter your grade: "))

letter_grade = percentage_to_letter(score)
passing = is_passing(letter_grade)
print(f"Your grade is {letter_grade}, Passing: {passing}")
