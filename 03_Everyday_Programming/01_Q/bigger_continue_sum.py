# Let I_m is a sequential series which is given.
# Let S_n is a sub sequential series in I_n. (For n <= m)
# And n(S_n) <= m
# And S_n's sum is biggest rather than rest sub sequential series's sum.
# And R_n is a sub sequential series which start n+1, ..., m
# And n(R_n) = m - n(S_n) , 0 <= n(R_n) <= m-1
# And I_n is a element of I_m. And I_n belong to R_n
# then we should compare between [S_n], [S_n, R_n] [I_n] alias as [A], [B], [C]
# the order of compare operation has 3C2 = 3! / (3-1)! = 3
# for example = max(max(A,B),C) / max(max(A,C),B) / max(max(B,C),A)
# So, Image that for loop with
# for i in range(...):
#     [S_n  ] [S_n,   R_n  ] I_n   # i = n
#     [S_n+1] [S_n+1, R_n+1] I_n+1 # i = n+1
# I_i is easy to update in for loop.
# [R_n] is always trouble maker because [R_n] is complicated.
# In order to create [S_n+1], I need to know [S_n] and [S_n, R_n] and I_n
# But I don't need to know [R_n+1] nor I_n+1
# When [S_n]      is choose for [S_n+1], S_n+1 is same    with S_n. in alias [A]
# When [S_n, R_n] is choose for [S_n+1], S_n+1 is changed with S_n. in alias [B]
# When I_n        is choose for [S_n+1], S_n+1 is changed with S_n. in alias [C]
# Naming(as well as code logic flow) is easy for max(max(B,C),A)
# Also it's easy to use sum of [R_n] rather than use [R_n] as list.
# For example if I_n        is choose, then sum([S_n, R_n]) < I_n i.e. max(B,C) = I_n is easy to calculate.
# For example if [S_n, R_n] is choose, then sum([S_n, R_n]) > I_n i.e. max(B,C)>= I_n is easy to calculate.
# So max(max(B,C),A) is better than others.


# for max(max(A,B),C) : possible
def get_abc(num_list):
    s_n_sum = num_list[0]
    r_n_sum = 0
    for i in range(1, len(num_list)):
        num = num_list[i]                    # update          [C]
        r_n_sum += num                       # update      [B]
        if s_n_sum <= s_n_sum + r_n_sum:     # compare [A] [B]
            s_n_sum += r_n_sum
            r_n_sum = 0
        if s_n_sum <= num:                   # compare [A]     [C]
            s_n_sum = num
            r_n_sum = 0
    return s_n_sum


# for max(max(A,C),B) : error
# def get_acb(num_list):
#     max_sum = num_list[0]
#     s_n_sum = num_list[0]
#     r_n_sum = 0
#     for i in range(1, len(num_list)):
#         num = num_list[i]                    # update          [C]
#         if s_n_sum <= num:                   # compare [A]     [C]
#             max_sum = num
#             r_n_sum = 0
#         r_n_sum += num                       # update      [B]
#         if s_n_sum <= s_n_sum + r_n_sum:     # compare [A] [B]
#             s_n_sum += r_n_sum
#             r_n_sum = 0
#     return max_sum


# for max(max(B,C),A) : easy
def get_bca(num_list):
    all_max_sum = num_list[0]                        # initial max sum of [S_n] [Sn, Rn] In
    new_max_sum = num_list[0]                        # initial max sum of       [Sn, Rn] In
    for i in range(1, len(num_list)):
        num = num_list[i]                            # update          [C]
        new_max_sum = max(new_max_sum + num, num)    # compare     [B] [C] + update r_n_sum
        all_max_sum = max(new_max_sum, all_max_sum)  # compare [A] [B]
    return all_max_sum

# a = [-1, 3]
# a = [-1, 3, -1]
a = [-1, 3, -1, 5]
print(get_abc(a))
# print(get_acb(a))
print(get_bca(a))

# a = [-5, -3]
a = [-5, -3, -1]
print(get_abc(a))
# print(get_acb(a))
print(get_bca(a))

a = [2, 4, -2, -3, 8]
print(get_abc(a))
# print(get_acb(a))
print(get_bca(a))
