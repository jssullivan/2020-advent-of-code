from collections import OrderedDict

input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

input_array = list(map(lambda num: int(num), input.split("\n")))
n = len(input_array)

lookback = 5
valid_nums = OrderedDict()
collision_count = [0] * lookback

def remove_n_items(n):
    for i in range(n):
        valid_nums.popitem(last=False)

last_index = 0
highest_checked_num = lookback
# There is a fundamental problem in this solution where valid_nums is to big (as it has future valid numbers before it should)
# Due to the second part of the problem, and the lack of the negative numbers, I don't believe this can't result in an invalid answer
# Withought building a more custom datastructure map that could handle deletes at arbitrary indexes this is only solvable by unwinding the OrderedDict (n^3)
for i in range(n):
    cur_num = input_array[i]
    # Check if Invalid Number, if valid remove the oldest
    if i >= lookback:
        if cur_num not in valid_nums:
            print("Question 1", cur_num)
            last_index = i
            break
        else:
            collision_index = i % lookback
            remove_n_items(lookback - collision_count[collision_index] - 1)
            collision_count[collision_index] = 0

    # Add the nex valid_nums
    for j in range(i + 1, min(i + lookback, n)):
        total = input_array[i] + input_array[j]
        if total in valid_nums:
            collision_count[valid_nums[total] % lookback] += 1
            valid_nums.move_to_end(total)
        valid_nums[total] = i

curTotal = 0
first_index_in_series = 0
last_index_in_series = 0
i = 0
while i < last_index:
    curNum = input_array[i]
    if curTotal + curNum > input_array[last_index]:
        curTotal -= input_array[first_index_in_series]
        first_index_in_series += 1
    elif curTotal + curNum == input_array[last_index]:
        last_index_in_series = i
        break
    else:
        curTotal += curNum
        i += 1

answer_2 = min(input_array[first_index_in_series:last_index_in_series]) + max(input_array[first_index_in_series:last_index_in_series])

print("Question 2", answer_2)
