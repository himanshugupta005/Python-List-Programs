def seconda_largest(numbers):
    m1,m2=None,None
    for x in numbers:
     if x >=m1:
        m1, m2=x, m1
     elif x > m2:
        m2=x
    return m2