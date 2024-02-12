dict1 = {'kind':'understanding other as like your world','empathy' : 'we dont know what they are going through','compassion' :'free unlimited kindness to heal someone'}
length = 0 
maxi = 0
mini = 0
for x in dict1.keys() :
    length = len(dict1[x])

    if (length > maxi) :
        maxi = length
        max_value = dict1[x]
        max_key = x
    # elif (max < min) :
    #     min = length
    #     min_value = dict1[x]
    #     min_key = x
    else :

        pass

print ("the maximum length of the value is for the key" ,max_key)
# print ("the minimum length of the value is for the key" ,min_key)

keys = list(dict1.keys())
values = list(dict1.values())
lens = [len(x) for x in values]
max_len = max(lens) 
min_len = min(lens)
max_index = lens.index(max_len)
min_index = lens.index(min_len)

print ("the minimum length of the value is for the key" ,keys[min_index])