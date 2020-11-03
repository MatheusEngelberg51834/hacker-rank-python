def merge_the_tools(string, k):

    equal_parts = (len(string) + 1) // k

#    string --> split() --> for each subform of the string build a sorted form where the subform has no duplicant characters

    ls = [string[i:len(string) // equal_parts] for i in range(0, len(string), equal_parts)]
    
    sorted_form = ''

    if k == len(string):
        for item in ls:
            if item not in sorted_form:
                sorted_form += item
        print(sorted_form)

    if k != len(string):
            for item in ls:
                for char in item:
                    if char not in sorted_form:
                        sorted_form += char
                print(sorted_form)
                sorted_form = ''

string, k = input(), int(input())
merge_the_tools(string, k)
