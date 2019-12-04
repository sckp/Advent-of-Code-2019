import math

count = 0
increase = True
before = False
after = False

for num in range(372304, 847060):
    strnum = str(num)
    increase = True
    for i in range (0, 5):
        if strnum[i] > strnum[i+1]:
            increase = False
            break
    if increase == True:
        for i in range(0, 5):
            before = False
            after = False
            if strnum[i] == strnum[i+1]:
                if i > 0:
                    if strnum[i-1] == strnum[i]:
                        before = True
                if i < 4:
                    if strnum[i+2] == strnum[i]:
                        after = True
                if before == False and after == False:
                    count = count + 1
                    break
print(count)
            
