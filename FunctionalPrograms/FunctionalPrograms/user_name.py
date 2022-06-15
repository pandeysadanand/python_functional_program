"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-02 09:36:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-02 09:50:00
    @Title : Python program to User Input and Replace String Template “Hello <<UserName>>, How are you?”
"""
# Taking user-name
userName = str(input("Enter Your Name : "))

n = len(userName)

# Checking if it contains minimum 3 character
if n >= 3:
    print("Hello", userName, "How are you ?")
else:
    print("User Name contain at least 3 character")
