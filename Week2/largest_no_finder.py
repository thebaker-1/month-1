arr = [1,2,4,323,32,34,34]

# option 1 print(max(arr)) or 
res = float("-inf")
for val in arr:
    if val > res:
        res = val
print(res)              
