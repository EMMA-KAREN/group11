def unique_list(li):
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = []
    for num in original_list:
        if num not in li:
            new_list.append(num)

return new_list
print(unique_list([2, 5, 9]))
