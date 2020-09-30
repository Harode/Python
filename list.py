n = int(input())
L = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    args = line[1:]
    if cmd.lower() != 'print':
        print(args)
        cmd += "(" + ",".join(args) + ")"
        print(cmd)
        eval("L."+cmd)
    else:
        print(L)
