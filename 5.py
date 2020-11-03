# boolean = False
# n = 0
# while boolean == False:
#     if string.find(string) != False:
        # n += 1
    #     string.replace(string, '')
    # else:
    #     return n

#p cada conjunt de len(substring) em len(substring)
#se o conjunto estiver em sequencia e for igual 

string = 'ABCDCDC'
substring = 'CDC'

j = 0

for i in range(0, len(string)):
    string_combination = string[i:i + len(substring)]
    if len(substring) == len(string_combination):
        if str(string_combination) == str(substring):
            j += 1

return j
