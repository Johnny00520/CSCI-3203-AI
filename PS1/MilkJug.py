#!/usr/bin/env python3

#For first element in the list
#	for i in list ----(0,1,2,3)
#		if element is not i:
#			pair = (element, i)
#list.append(pair)

#pour array[from_value] 
#initializing globals
visited_state = []
final_state_list = []
number_of_states = 1

def milkJug(array, from_value, to):
	global visited_state
	temp_list = list(array)
	print (str(temp_list))
	#Find the maximum pourable amount

	if to == 0:
		maximum = 40
	elif to == 1:
		maximum = 40
	elif to == 2:
		maximum = 5
	elif to == 3:
		maximum = 4
        
        # how many you can pour for you to pour

	pourable = maximum - array[to]

	#If from<pourable -- pour FROM value into TO
	#Else (FROM >= pourable) -- pour pourable from FROM into TO
	if from_value!=to:
		if temp_list[from_value]<=pourable:
			temp_list[to]=temp_list[to]+temp_list[from_value]
			temp_list[from_value]=0
		else:
			temp_list[from_value]=temp_list[from_value]-pourable
			temp_list[to]=temp_list[to]+pourable

	#Check if state has been visited previously
	if temp_list in visited_state:
		#print("This permutation has been seen before!")
        #        print("state has been visited: " , visited_state)
		return False
	elif temp_list[2]==2 and temp_list[3]==2:
		final_state_list.append(temp_list)
		return True
	else:
		visited_state.append(temp_list)

	#Recursively call function w/current array
	for i in range(0,4):
		for j in range(0,4):
			goal_reached = milkJug(temp_list, i, j)

			if goal_reached == True:
				final_state_list.append(temp_list)
				return True

if __name__== "__main__":
    array = [40, 40, 0, 0]
    milkJug(array, 0, 0)
    #print (str(visited_state[::-1]))
    print (str(final_state_list[0:-1]))

