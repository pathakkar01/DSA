def search(ans,nums,i,curr):
    #print(curr)
    if i == len(nums):
        if curr in ans:
            print(curr)
            pass
        else:
            print("else", curr)
            ans.append(curr)
    else:
        curr.append(nums[i])
        search(ans,nums,i+1,curr)
        curr.pop()
        search(ans,nums,i+1,curr)
nums = [1,2,2]
curr = []
ans  = []
search(ans,nums,0,curr)
print(ans)