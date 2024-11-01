f=open("mountain.txt", "r")
s="["
for i in f.readlines():
    s+=i[:-1]
s=s[:-1]
s+="]"
print(s)