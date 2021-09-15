set_1 = set(input('Enter set A:').replace(' ', ''))
set_2 = set(input('Enter set B:').replace(' ', ''))
set_3 = set(input('Enter set C:').replace(' ', ''))


def Union(a, b):
    set_res = set(b)
    for el in a:
        set_res.add(el)
    return set_res


def Intersection(a, b):
    set_res = set()
    for el in a:
        if el in b:
            set_res.add(el)
    return set_res


def Difference(a, b):
    set_res = set(a)
    for el in b:
        if el in a:
            set_res.discard(el)
    return set_res


def Compliment(a, univ):
    set_res = set(univ)
    for el in univ:
        if el in a:
            set_res.discard(el)
    return set_res


universal_set = Union(Union(set_1, set_2), set_3)

print(f'''
You enter:
    set A: {set_1}
    set B: {set_2}
    set C: {set_3}

-------Operations for set A-------
A union B: {Union(set_1,set_2)}
A intersection B: {Intersection(set_1,set_2)}
A difference B: {Difference(set_1,set_2)}

A union C: {Union(set_1,set_3)}
A intersection C: {Intersection(set_1,set_3)}
A difference C: {Difference(set_1,set_3)}

A compliment: {Compliment(set_1,universal_set)}

-------Operations for set B-------
B difference A: {Difference(set_2,set_1)}

B union C: {Union(set_2,set_3)}
B intersection C: {Intersection(set_2,set_3)}
B difference C: {Difference(set_2,set_3)}

B compliment: {Compliment(set_2,universal_set)}

-------Operations for set C-------
C difference A: {Difference(set_3,set_1)}
C difference B: {Difference(set_3,set_2)}

C compliment: {Compliment(set_3,universal_set)}
''')
