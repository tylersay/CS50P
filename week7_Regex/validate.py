import re


email = input("what is your email? ").strip()

# \w is short for word char
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")