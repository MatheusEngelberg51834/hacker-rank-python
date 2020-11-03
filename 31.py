from collections import OrderedDict

ordered_dictionary = OrderedDict()

# for _ in range(int(input())):
#     inpt = input().split()
#     if inpt[0] + inpt[1] not in ls and inpt[0] not in ls:
#         if len(inpt) == 3:
#             ordered_dictionary[inpt[0] + ' ' + inpt[1]] = int(inpt[2])
#             ls.append(inpt[0] + inpt[1])
#         else:
#             ordered_dictionary[inpt[0]] = int(inpt[1])
#             ls.append(inpt[0])
#     elif inpt[0] + inpt[1] in ls or inpt[0] in ls:
#         if len(inpt) == 3:
#             name = inpt[0] + ' ' + inpt[1]
#             ordered_dictionary[inpt[0] + ' ' + inpt[1]] = int(inpt[2]) + ordered_dictionary[name]
#         else:
#             name = inpt[0]
#             ordered_dictionary[inpt[0]] = int(inpt[1]) + ordered_dictionary[name]

# for item in ordered_dictionary:
#     print(item, ordered_dictionary[item])

for _ in range(int(input())):
    inpt = input().split()
    if len(inpt) == 3:
        ordered_dictionary[inpt[0] + ' ' + inpt[1]] = int(inpt[2])
    else:
        ordered_dictionary[inpt[0]] = int(inpt[1])

ordered_dict1 = OrderedDict()

for item in ordered_dictionary:
    try:
        ordered_dict1[item] = ordered_dictionary[item] + ordered_dict1[item]
    except KeyError:
        ordered_dict1[item] = ordered_dictionary[item]

for item in ordered_dict1:
    print(item, ordered_dict1[item])