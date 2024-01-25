"""
Question:
- There are 100 doors in a row, they are all initially closed.
- You make 100 passes by the doors.
- On the first pass, you visit every door in sequence and toggle its state: 
  if the door is closed -> you open it 
  if it's open -> you close it.
- The second time, you only visit every second door (door 2,4,6...) and toggle it.
- The third time, you visit every third door (dooe 3,6,9...) and toggle it.\
- Continue this pattern until you only visit the 100th' door and toggle it. 

Which doors are open and which are closed after the last pass?
"""

number_of_doors = 100

# initiate all doors to be closed. 
# added 1 to match the indexes 1-100 afterwards. (ignoring index 0)
doors = [False] * (number_of_doors + 1)

# 100 passes by the doors = 100 iterations
for i in range(1,number_of_doors+1):
    # select the doors
    for j in range(i,number_of_doors+1,i):
      doors[j] = not doors[j]

# debug
# print(doors[1:])

# print the indices of the open doors at the end
for k in range(1,number_of_doors+1): 
    if doors[k]: 
        print(k, end=", ")



#********************************************************************************

# Alternative solution:        
# # iterations:
# for i in range(1,number_of_doors+1):
#     j = 1
#     while j <= number_of_doors//i:
#         doors[i*j] = not(doors[i*j])
#         j += 1
