a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {1, 3, 5, 7, 9}
c = {2, 3, 5, 7}

u_abc = set.union(a, b, c)
i_abc = set.intersection(a, b, c)
i_ab = set.intersection(a, b)
i_ac = set.intersection(a, c)
i_bc = set.intersection(b, c)
only_a = a - i_ab - i_ac
only_b = b - i_ab - i_bc
only_c = c - i_bc - i_ac
only_abc = set.union(only_a, only_b, only_c)
