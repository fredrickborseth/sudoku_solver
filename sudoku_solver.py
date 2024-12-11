
# Rows
# from the top to the bottom.
# change values here.

r1 = [5, 6, 8, 0, 4, 0, 0, 0, 3]
r2 = [0, 0, 2, 0, 9, 0, 0, 0, 7]
r3 = [0, 9, 7, 8, 6, 0, 0, 0, 0]
r4 = [6, 0, 0, 3, 1, 0, 4, 0, 9]
r5 = [0, 3, 0, 0, 5, 0, 0, 6, 2]
r6 = [0, 1, 9, 6, 0, 0, 5, 0, 8]
r7 = [0, 0, 3, 0, 0, 6, 8, 0, 1]
r8 = [0, 5, 1, 0, 0, 0, 0, 2, 0]
r9 = [9, 0, 0, 7, 0, 0, 3, 4, 5]

rows = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

def finding_missing_number(nums):
    n = len(nums) + 1
    total = sum([num for num in range(0, n)])
    return total - sum(nums)

def how_many_zeros(num_group):
    set_of_nums = set(num_group)
    length_of_set = len(set_of_nums)
    if length_of_set == 9:
        return finding_missing_number(num_group)
    else:
        return 0 # change this to something useful

def manipulate_zero_index(num_group):
    n = how_many_zeros(num_group)
    working_num_list = num_group.index(0)
    num_group.insert(working_num_list, n) # needs a way to find the missing number in the list
    num_group.remove(0)  # removing the zero in the list
    return num_group


manipulate_zero_index(r1)
