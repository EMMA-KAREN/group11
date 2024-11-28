	
def is_sorted_ascending(list):  

# Check if the list is empty or has one element, in which case it's sorted  
if len(list) < 2:  
    return True  

# Iterate through the list and compare each element with the next  
for i in range(len(list) - 1): #loops through list till the end 6           5
    if list[i] > list[i + 1]:  #checks for a greater value
        return False  

return True  
Example
print(is_sorted_ascending([4,0])) 