def get_missing_number(lst):
    return set(range(lst[len(lst)-1])[1:]) - set(l)
l = list(range(1,100))
l.remove(25)
print(get_missing_number(l))
