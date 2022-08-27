import time 
t = int(input("How many seconds do you want to countdown: "))

while t:
    # t // 60 will calculate how many mins are made for the given number
	# for example 60 // 60 will give 1 
	# and 120 will give 2 
	mins = t // 60
	secs = t % 60
	# Format the time
	timer = '{:d}:{:d}'.format(mins,secs)
	print("countdown: ",timer)
	# Wait for 1 second
	time.sleep(1)
	# Decrease the value of t by 1 
	t -= 1
