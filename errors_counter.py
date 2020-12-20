def errors_count(a, b):
    count = 0
    if len(a) != len(b):
        print("ERROR a b")
    else:
        for i in range(0, len(a)):
            if a[i] != b[i]:
                count+=1
    return count

#print(errors_count('110101101110101101110101101110101101', '000101101000101101000101101000101101'))