#HAPPY NEW YEAR 2023

import time
import random
for i in range (1,45):
	print (" ")
s=" " 
for i in range(1,10000):
	count=random.randint(1,100)
	while count>0:
		s+="  "
		count-=1 
		
	if 1%10==0:
		print( f"{s} HAPPY NEW YEAR 2023")
	else:
		print (s+="*")
	s=" "
	time.sleep(0.3)
	
	
