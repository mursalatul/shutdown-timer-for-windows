import datetime as dt
import time as tm
import os

# Print iterations progress
# from stackoverflow . Link: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


def shutdown(time):
	"""Shutdown after time minutes"""
	per_hyphen_time = ((time * 60) / 100) # time = minutes . so we are converting it into seconds (time * 60) 
												# and dividing by 100 means find per hyphen time for the progress bar
	# telling the user that shutdown counter is on
	print(f"\nYour Computer Will be Shutdown After {time} minutes\nPress CTRL+C or Close terminal to cancel it.\n")
	# setting staring point into 0
	printProgressBar(0, 100, prefix = 'Progress:', suffix = 'Complete', length = 100)
	# looping time
	for i in range(100):
		tm.sleep(per_hyphen_time)
		printProgressBar(i + 1, 100, prefix = 'Progress:', suffix = 'Complete', length = 100)
	os.system("shutdown /s /t 1") # shutdown command. it will run after progress bar complete

def minute_left(itime):
	"""process clock time"""
	# present time
	now = dt.datetime.now().strftime("%I/%M/%S") #converting present time into 12 hour base time with datetime.strftime()
													#datetime.strftime() also convert the datetime object into string
	now = dt.datetime.strptime(now, "%I/%M/%S")	# converting 12 hour base present time from string to datetime object
	
	# input time
	try:
		# check if user inter a wrong time input.example 24 base time format
		if itime.find("/") != -1:
			target_time = dt.datetime.strptime(itime, "%I/%M")
		elif itime.find(":") != -1:
			target_time = dt.datetime.strptime(itime, "%I:%M")
		elif itime.find("-") != -1:
			target_time = dt.datetime.strptime(itime, "%I-%M")
		# datetime obj - datetime obj returns timedelta obj
		return ((target_time - now).seconds // 60) + 1 # addding extra 1 min cause after dividing it can give floor value
	except:
		print("Invalid Time format.\nPlease Provide 12Hour Time Format with proper seperator(/, :, -)\n")
		return False
	
	

def shutdown_process (way):
	if(way == '1'):
		# shutdown at the inputed time.
		timer = input("When You Want To Shutdown(hh/mm): ").replace(" ", "")
		timer = minute_left(timer)
		if timer == False:
			shutdown_process('1')
		else:
			shutdown(timer)
	else:
		# shutdown after input minutes
		timer = int(input("How long will it take to close(mm): ").replace(" ", "")) 
		shutdown(timer)

# starting program
while True:
	method = input("Type the number of method you want to use:\n1.Shutdown at(Time)\n2.Shutdown after(Minutes)\n(1 or 2) : ")	
	if method == '1' or method == '2':
		break
shutdown_process(method)