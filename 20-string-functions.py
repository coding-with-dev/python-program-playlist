def trim(str):
    return str.strip()


def exists(str, x):
    return str.find(x)


def titleIt(str):
    return str.title()


def casesSwap(str):
    return str.swapcase()

print(trim("hello"))
print(exists("hello", "llo"))
print(titleIt("hello"))
print(casesSwap("hello"))