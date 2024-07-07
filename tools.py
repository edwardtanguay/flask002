from datetime import datetime

def getCurrentDateTimeIso():
	now = datetime.now()
	return now.strftime("%Y-%m-%d %H:%M:%S")