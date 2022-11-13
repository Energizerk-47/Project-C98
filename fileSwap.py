fileName=input("Enter Your File Name--")
f=open(fileName)

print(f.read())

fileLines=f.readlines()
print(fileLines)
for line in fileLines:
    print(line)