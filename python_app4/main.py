def distance():
    a = input()
    b = input()

    n, m = len(a), len(b)

    if n>m:
        a, b = b, a
        n, m = m, n
    cur = range(n+1)
    for i in range(1, m+1):
        prev, cur = cur, [i]+[0 for k in range(n)]
        for j in range(1, n+1):
            add = prev[j]+1
            delete = cur[j-1] + 1
            change = prev[j-1]
            if a[j-1] != b[i-1]:
                change += 1
            cur[j] = min(add,delete,change)


    return  cur[n]

t = int(input())
for i in range(t):
    ans = distance()
    if ans ==0:
        print("You're logged in!")
    elif ans==1:
        print("You almost got it. You're wrong in just one spot.")
    elif ans==2:
        print("You almost got it, but you're wrong in two spots.")
    elif ans==3:
        print("You're wrong in three spots.")
    else:
        print("What you entered is too different from the real password.")