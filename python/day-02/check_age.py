def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

result = check_age(20)
print(result)


"""
A. What will print(result) output?
==> Adult
B. Which value does age contain when check_age(20) runs?
==> 20 
C. Which condition is Python checking?
==> age >= 18
D. Which return statement executes?
==> return "Adult"
E. What value does result finally contain?
==> Adult
"""