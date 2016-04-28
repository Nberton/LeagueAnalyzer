import os.path


#creates a dictionary of the stats
def gameAnalyzer(inFileName):
	inFile = open(inFileName + '/keylogs.txt')
	infoFile = open(inFileName + '/README.txt')
	info = list()
	for line in infoFile:
		info.append(line)
	#get champ name from user
	champ = info[0].rstrip()
	#get champ lane from user
	lane = info[1].rstrip()
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
	inFile.close()
	infoFile.close()
	return outLine


def main():
	print "Parallel Coordinates constructor for keys"
	#create header row
	outfileN = raw_input("Please enter an output file name: ")
	outfileN += '.csv'
	of = open(outfileN,'w')
	outLine = "Champion,Lane,Q,W,E,R,D,F"
	of.write(outLine)
	#enter input loop
	count = 0
	inFN = raw_input("please input a data folder Name: ")
	while(inFN != 'end' and inFN != 'q'):
		print inFN
		#check for valid file
		if not os.path.exists(inFN):	#if failed go around
			print "That is not a valid file! Please try again or q to exit"
			inFN = raw_input("please input a datafile Name or q:")
			continue
		count += 1
	 	#else analyze the game and throw it in the data file
	 	outLine = gameAnalyzer(inFN)
	 	of.write('\n'+outLine)
	 	inFN = raw_input("please input a datafile Nam or q: ")
	#end program with some checking output
	print "Wrote " + str(count) + " Games of data"
	print "Closing File Writer"


if __name__ == '__main__':
	main()