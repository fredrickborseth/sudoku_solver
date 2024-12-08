
# Rows
# from the top to the bottom.
# change values here.

r1 = [9, 2, 3, 4, 5, 6, 8, 0, 1]
r2 = [0, 0, 1, 0, 0, 0, 0, 0, 0]
r3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
r4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
r5 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
r6 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
r7 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
r8 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
r9 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

rows = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

def manipulate_zero_index(num_group):
    n = finding_missing_number(num_group)
    working_num_list = num_group.index(0)
    num_group.insert(working_num_list, n)
    num_group.remove(0)
    print(num_group)
    

def finding_missing_number(nums):
    n = len(nums) + 1
    total = sum([num for num in range(0, n)])
    return total - sum(nums)
    

def the_sudoku_format(x):
    for nums in rows:
        print(nums)


manipulate_zero_index(r1)
