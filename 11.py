s = 'banana'

vowels = ['a', 'e', 'i', 'o', 'u']

vow = True
vowel_points = 0

letters = [letter for letter in s]

if vow:
    word = ''
    vowel_ = ''
    for vowel in vowels:
        if vowel in s:
            vowel_points += 1
            word += vowel
            vowel_ += vowel

print(vowel_points)

# for a in s:
#     for b in s:
#         print(a, b)

# for c in s:
#     print(c)

# for d in s:
#     for e in s:
#         for f in s:
#             print(d, e, f)

# for g in s:
#     for h in s:
#         for i in s:
#             for j in s:
#                 print(g, h, i, j)
    
# for k in s:
#     for l in s:
#         for m in s:
#             for n in s:
#                 print(k, l, m, n)