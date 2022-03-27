t = int(input())

for T in range(t):
    n, m = map(int, input().split())
    LINE = [int(i) for i in input()]
    def xor(i):
        LINE[i] = LINE[i]^1
    h = 0
    days = 0
    for i in range(n):
        if LINE[i]==0:
            if h==0:
                print(LINE, h, days)
                h+=m
                days+=1

            h-=1
            xor(i)

    # print(LINE,h,days)
    if h!=0:
        days -= 1
        h = m-h
        for i in range(0,n)[::-1]:
            if h==0:

                break
            h-=1
            xor(i)

    # print(LINE, h, days)
