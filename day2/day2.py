def partOne(nums):
    # replace per the instructions
    nums[1] = 12
    nums[2] = 2
    for i in range(0, len(nums), 4):
        if nums[i] == 99:
            return nums[0]
        if nums[i] == 1:
            nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
        elif nums[i] == 2:
             nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
        i += 4

if __name__ == '__main__':
    with open('input.txt', 'rt') as f_obj:
        f_split = [i.split(',') for i in f_obj][0][::-1]
        nums = [int(i) for i in f_split][::-1]
    print(partOne(nums))
