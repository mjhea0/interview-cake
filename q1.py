def reverse_list_string(string_list):
    size = len(string_list)
    for i in range(0, size/2):
        string_list[i], string_list[size-1-i] = string_list[size-1-i], string_list[i]
    return string_list

print reverse_list_string(["t","e","s","t"]) == ["t","s","e","t"]
print reverse_list_string(["g","o","d"]) == ["d","o","g"]


def reverse_list(my_list):
    return my_list[::-1]

print reverse_list(["t","e","s","t"]) == ["t","s","e","t"]
print reverse_list(["g","o","d"]) == ["d","o","g"]

