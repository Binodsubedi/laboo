n = 1
def fun(n):
    if n==1:
        return 3
    else:
        return 3 + fun(n-1)

ans = fun(3)
print(ans)
# can also be recognized as multiple terms substitution method