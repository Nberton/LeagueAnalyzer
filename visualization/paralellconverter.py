import os.path


#creates a dictionary of the stats
def gameAnalyzer(inFile):
	#get champ name from user
	champ = raw_input("Please input Champion Name: ")
	#get champ lane from user
	lane = raw_input("Please input Lane: ")
	#read that file
	countMap = dict()
	for line in inFile:
		work = line.rstrip().split()
		key = str(work[2])
		if not key in countMap:
			countMap[key] = 1
		else:
			countMap[key] += 1 
		print key
	outLine = (champ + ',' + lane + ',' + str(countMap['q']) + ',' 
		+ str(countMap['w']) + ','  + str(countMap['e']) + ','+ str(countMap['r']) + ',' 
		+ str(countMap['d']) + ',' + str(countMap['f']))
	print outLine
	return outLine


def main():
	print "Paralell Coordinates constructor for keys"
	#create header row
	outfileN = raw_input("Please enter a file name: ")
	outfileN += '.csv'
	of = open(outfileN,'w')
	outLine = "Champion,Lane,Q,W,E,R,D,F\n"
	of.write(outLine)
	#enter input loop
	count = 0
	inFN = raw_input("please input a datafile Name: ")
	while(inFN != 'end' and inFN != 'q'):
		print inFN
		#check for valid file
		if not os.path.isfile(inFN):	#if failed go around
			print "That is not a valid file! Please try again or q to exit"
			inFN = raw_input("please input a datafile Name or q:")
			continue
		count += 1
	 	#else analyze the game and throw it in the data file
	 	inF = open(inFN)
	 	outLine = gameAnalyzer(inF)
	 	of.write('\n'+outLine)
	 	inFN = raw_input("please input a datafile Nam or q: ")
	#end program with some checking output
	print "Wrote " + str(count) + " Games of data"
	print "Closing File Writer"


if __name__ == '__main__':
	main()