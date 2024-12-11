
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


# Columns
# from the left to the right
# let it be as it is

c1 = [r1[0], r2[0], r3[0], r4[0], r5[0], r6[0], r7[0], r8[0], r9[0]]
c2 = [r1[1], r2[1], r3[1], r4[1], r5[1], r6[1], r7[1], r8[1], r9[1]]
c3 = [r1[2], r2[2], r3[2], r4[2], r5[2], r6[2], r7[2], r8[2], r9[2]]

c4 = [r1[3], r2[3], r3[3], r4[3], r5[3], r6[3], r7[3], r8[3], r9[3]]
c5 = [r1[4], r2[4], r3[4], r4[4], r5[4], r6[4], r7[4], r8[4], r9[4]]
c6 = [r1[5], r2[5], r3[5], r4[5], r5[5], r6[5], r7[5], r8[5], r9[5]]

c7 = [r1[6], r2[6], r3[6], r4[6], r5[6], r6[6], r7[6], r8[6], r9[6]]
c8 = [r1[7], r2[7], r3[7], r4[7], r5[7], r6[7], r7[7], r8[7], r9[7]]
c9 = [r1[8], r2[8], r3[8], r4[8], r5[8], r6[8], r7[8], r8[8], r9[8]]

# 3 x 3
# from top left to bottom right (reading direction)

tbt1 = [r1[0], r1[1], r1[2], r2[0], r2[1], r2[2], r3[0], r3[1], r3[2]]
tbt2 = [r1[3], r1[4], r1[5], r2[3], r2[4], r2[5], r3[3], r3[4], r3[5]]
tbt3 = [r1[6], r1[7], r1[8], r2[6], r2[7], r2[8], r3[6], r3[7], r3[8]]

tbt4 = [r4[0], r4[1], r4[2], r5[0], r5[1], r5[2], r6[0], r6[1], r6[2]]
tbt5 = [r4[3], r4[4], r4[5], r5[3], r5[4], r5[5], r6[3], r6[4], r6[5]]
tbt6 = [r4[6], r4[7], r4[8], r5[6], r5[7], r5[8], r6[6], r6[7], r6[8]]

tbt7 = [r7[0], r7[1], r7[2], r8[0], r8[1], r8[2], r9[0], r9[1], r9[2]]
tbt8 = [r7[3], r7[4], r7[5], r8[3], r8[4], r8[5], r9[3], r9[4], r9[5]]
tbt9 = [r7[6], r7[7], r7[8], r8[6], r8[7], r8[8], r9[6], r9[7], r9[8]]


rows = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
columns = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
three_by_three = [tbt1, tbt2, tbt3, tbt4, tbt5, tbt6, tbt7, tbt8, tbt9]

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

# pattern that checks if a number can be insterted into the cell
# its cross checking if the number already exists in a number group (rows, columns, 3 x 3)
def cross_check_numbers():
    pass
# if the missing number exists -> check the next number
def next_number_in_list():
    pass

# if there is only one number left - > insert the number into the cell

manipulate_zero_index(r1)
