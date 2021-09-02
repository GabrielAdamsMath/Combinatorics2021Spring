

nums = []
digits = [0,1,3,4,5,6,7,8]

for i in range(999,8766):
    multDigit = False

    if(i < 4300):
            continue
    if "9" in str(i):
            continue
    if "2" in str(i):
            continue
    for j in digits:
        if str(i).count(str(j)) > 1:
           # print(i)
            multDigit = True
            break
    if multDigit == True:
            continue
    nums.append(i)
print("Total:")
print(len(nums))