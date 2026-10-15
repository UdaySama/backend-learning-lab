def create_Message(name):
    message = f"Hello, {name}"
    return message


greeting = create_Message('Amey')
print(greeting)
# B. What will print(message) do?
# print(message) NameError: name 'message' is not defined

# A. What will print(greeting) output? :- print the amey "Hello, Amey"
# B. What will print(message) do?
# C. Why?
# :- beacuse we have declrated the message in the function which is local 


# - function name :- create_Message
# - parameter :- (name)
# - argument :- ('Amey')
# - local variable :- message
# - returned value :- return message
# - variable receiving the returned value :- greeting