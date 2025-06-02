
current_year = int(input("Enter the current year: "))
current_month = int(input("Enter the current month: "))
current_day = int(input("Enter the current day: "))


birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))


age = current_year - birth_year


if (birth_month, birth_day) > (current_month, current_day):
    age = age - 1

if 0 <= age <= 17:
    category = "I"
elif 18 <= age <= 36:
    category = "II"
elif 37 <= age <= 60:
    category = "III"

print("You are", age, "years old.")
print("Age category:", category)
