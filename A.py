inp = open("input.txt","r")
x = open("output.txt","w")
s = list(inp.readlines())
k = list(map(int,s[1].split(" ")))
for i in range(int(s[0])):
  if k.count(k[i]) == 2:
    x.write(str(k[i]))
    x.close()
    inp.close()
    break
  if k.count(k[int(s[0])-1-i]) == 2:
    x.write(str(k[int(s[0])-1-i]))
    x.close()
    inp.close()
    break
