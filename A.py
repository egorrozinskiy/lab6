inp = open("input.txt","r")
wr = open("output.txt","w")
s = list(inp.readlines())
ns = list(map(int,s[1].split(" ")))
for i in range(int(s[0])):
  if ns.count(ns[i]) == 2:
    wr.write(str(ns[i]))
    wr.close()
    inp.close()
    break
  if ns.count(ns[int(s[0])-1-i]) == 2:
    wr.write(str(ns[int(s[0])-1-i]))
    wr.close()
    inp.close()
    break
