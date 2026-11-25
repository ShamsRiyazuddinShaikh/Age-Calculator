from datetime import date


def ageCalculator(birth_date):
    today = date.today()

    if birth_date > today:
        raise ValueError("Birth date cannot be in the future")

    age_year = today.year - birth_date.year
    age_month = today.month - birth_date.month
    age_day = today.day - birth_date.day

    if age_day < 0:
        previous_month = today.month - 1 or 12
        previous_month_year = today.year
        if today.month > 1:
            previous_month_year = today.year
        else:
            previous_month_year = today.year - 1
        next_month = previous_month + 1 if previous_month < 12 else 1
        next_month_year = previous_month_year if previous_month < 12 else previous_month_year + 1
        previous_month_length = (date(next_month_year, next_month, 1)
                            - date(previous_month_year, previous_month, 1)).days
        age_day += previous_month_length
        age_month -= 1

    if age_month < 0:
        age_month += 12
        age_year -= 1

    print(f"your age today is: {age_year} years, {age_month} months, and {age_day} days")


today = date.today()
print("today's date is:", today)

birthDate = input("Enter your birth date in YYYY-MM-DD format:").strip()
try:
    birth_date = date.fromisoformat(birthDate)
    print("your date of birth is:", birthDate)
    ageCalculator(birth_date)
except ValueError as error:
    print("invalid date:", error)