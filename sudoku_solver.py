
# Rows
# from the top to the bottom.
# change values here.

r1 = [9, 2, 3, 4, 5, 6, 7, 0, 1]
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
    working_num_list = num_group.index(0)
    num_group.insert(working_num_list, 8) # needs a way to find the missing number in the list
    num_group.remove(0)  # removing the zero in the list
    print(num_group)


def finding_missing_number():
    pass


def the_sudoku_format(x):
    for nums in rows:
        print(nums)

print(r1)



# x = (r1.index(0))
# y = r1.insert(x, 8)
# z = r1.remove(0)

manipulate_zero_index(r1)