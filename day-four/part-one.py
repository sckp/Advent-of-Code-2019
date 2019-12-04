import math

count = 0
increase = True

for num in range(372304, 847060):
    strnum = str(num)
    increase = True
    for i in range (0, 5):
        if strnum[i] > strnum[i+1]:
            increase = False
            break
    if increase == True:
        for i in range(0, 5):
            if strnum[i] == strnum[i+1]:
                count = count + 1
                break
print(count)
            
