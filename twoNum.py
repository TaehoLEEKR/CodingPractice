def solution(nums , target):
    nums.sort()
    left = 0
    right = len(nums) -1
    
    while left <= right:
        res = nums[left] + nums[right]
        if res == target:
            print(nums[left], nums[right])
            return (nums[left], nums[right])
        elif res < target:
            left += 1
        else:
            right -= 1
    return [0,0]
            

        
        


        







solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2]  , 28)

