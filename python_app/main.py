X = 1
Y = 1

s = input()
while len(s) > 0:
	c = int(s[2:])
	prevX = X
	prevY = Y
	if X + c <= 100 and s[0] == 'R':
		X += c
		step = 1
	else:
	    if X - c >= 0 and s[0] == 'L':
	    	X -= c
	    	step = -1
	    else:
	    	if Y + c <= 100 and s[0] == 'D':
	    		Y += c
	    		step = 1
	    	else:
	    		if Y - c >= 0 and s[0] == 'U':
	    			Y -= c
	    			step = -1
	    		else:
	    			print("!Robot crashed!")
	    			break
	if prevX == X and prevY == Y:
		print("No need to move")

	while prevX != X:
		prevX += step
		print(str(prevX) + ',' + str(Y))
	while prevY != Y:
		prevY += step
		print(str(X) + ',' + str(prevY))
	s = input()