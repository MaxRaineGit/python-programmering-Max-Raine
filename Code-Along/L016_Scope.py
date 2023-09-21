# Scope, life-time of a variable.
# Local Scope: Only available locally in a function
# Global Scope: Available through execution of program.

name = "Max"

def main():
    name = "Lucian"
    print(name)

print(name)
main()
print(name)

# # Python doesn't have block scope, but this is used in most other languages, such as c#, c++, java
# if name == "Max":
#     last_name = "Rainé"

# print(last_name)

# for i in range(10):
#     print(i)

# print(f"i = {i}")