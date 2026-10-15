def check_age(age):
    if age >= 18:
        return "Adult"
    elif age >= 13 :
        return "Teenager"
    elif age <= 13:
        return "Child"
    else:
        return 'Invalid'

result = check_age(12)
print(result)
print(check_age(10))
print(check_age(12))
print(check_age(13))
print(check_age(17))
print(check_age(18))
print(check_age(25))


