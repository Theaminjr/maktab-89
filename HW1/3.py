#method one
original_list = input().split()
new_list = []
for i in original_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)

#method two
# original_list = input().split()
# print(list(set(original_list)))