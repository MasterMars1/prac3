name=input("Please enter your name here:")
while len(name)<=0:
    print("Please enter a vaild name")
    name=input("Please enter your name again here")

print(name[::2])

for i in range(0,len(name),2):
    print(name[i],end='')
#command