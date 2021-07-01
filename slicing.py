def print_element(a):
    if len(a)==0:
        return
    print(a[0])
    print_element(a[1:])
print_element([1,2,3])