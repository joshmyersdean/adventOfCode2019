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

def partTwo(tmp):
    target = 19690720
    for i in range(100):
        for j in range(100):
            # reset the array
            nums = tmp[:]
            nums[1] = i
            nums[2] = j
            pointer = 0
    	    for k in range(0, len(nums), 4):
                if nums[k] == 99:
                    break
                if nums[k] == 1:
                    nums[nums[k+3]] = nums[nums[k+1]] + nums[nums[k+2]]
                elif nums[k] == 2:
                    nums[nums[k+3]] = nums[nums[k+1]] * nums[nums[k+2]]
            if nums[0] == target:
                return 100*nums[1] + nums[2]

if __name__ == '__main__':
    with open('input.txt', 'rt') as f_obj:
        f_split = [i.split(',') for i in f_obj][0][::-1]
        num = [int(i) for i in f_split][::-1]
        nums = num[:]
    print(partOne(num))
    print(partTwo(nums))
