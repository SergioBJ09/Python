def lltod(ll):
    a={}
    for i,e in enumerate(ll):
        a[e]=i
    return a
print(lltod(["casa","coche","silla","mesa"]))

def ltod(l):
    return {key:value for value,key in enumerate(l)}
print(ltod(["casa","coche","silla","mesa"]))