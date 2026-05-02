def reverse_list(lst):
    if len(lst) == 0:
        return []
    else:
        return [lst[-1]] + reverse_list(lst[:-1])

# Test qilish
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
print(reverse_list(['a', 'b', 'c']))  # ['c', 'b', 'a']
print(reverse_list([10, 20, 30]))  # [30, 20, 10]
