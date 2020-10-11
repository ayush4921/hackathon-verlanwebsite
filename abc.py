import re
s= 'n02085620-Chihuahua'
t = re.sub('^s-$-', '', s)
print(t)