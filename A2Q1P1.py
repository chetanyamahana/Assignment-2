str = "Python is a case sensitive language"
print(len(str))

rev=str[::-1]
print(rev)
print(str[slice(10,26)])
 

new_str = str.replace("a case sensitive", "object oriented" )
print(str)
print(new_str)

index = str.find('a')
print("Substring 'a' found at index:", index)

def remove(str):
   return str.replace(" ", "")
print(remove(str))


