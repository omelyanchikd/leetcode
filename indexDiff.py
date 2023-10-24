def index_check(indexes_a, indexes_b, indexDifference):
    i_star = -1
    j_star = -1
    for i in indexes_a:
        for j in indexes_b:
            if abs(i - j) >= indexDifference:
                i_star = i
                j_star = j
                break
    return i_star, j_star


def findIndices(nums, indexDifference, valueDifference):
    if indexDifference == 0 and valueDifference == 0:
        return [0, 0]
    i_star = -1
    j_star = -1
    nums_dict = {}
    for i, num in enumerate(nums):
        if num in nums_dict:
            nums_dict[num].append(i)
        else:
            nums_dict[num] = [i]
    nums.sort()
    min_num = nums[0]
    i = 0
    j = 1
    while i < len(nums) - 1:
        if abs(nums[j] - min_num) >= valueDifference:
            i_star, j_star = index_check(nums_dict[nums[j]], nums_dict[min_num], indexDifference)
            if i_star > -1:
                break
        j += 1
        if j == len(nums):
            i += 1
            j = i + 1
            min_num = nums[i]
    return [i_star, j_star]

if __name__ == '__main__':
    nums = [3, 0, 7]
    indexDifference = 2
    valueDifference = 4
    print(findIndices(nums, indexDifference, valueDifference))
    nums = [5, 1, 4, 1]
    indexDifference = 2
    valueDifference = 4
    print(findIndices(nums, indexDifference, valueDifference))
    nums = [2, 1]
    indexDifference = 0
    valueDifference = 0
    print(findIndices(nums, indexDifference, valueDifference))
    nums = [1, 2, 3]
    indexDifference = 2
    valueDifference = 4
    print(findIndices(nums, indexDifference, valueDifference))
    nums = [5, 10]
    indexDifference = 1
    valueDifference = 2
    print(findIndices(nums, indexDifference, valueDifference))