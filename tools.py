from datetime import datetime, timedelta

def getCurrentDateTimeIso():
	now = datetime.now()
	corrected_time = now + timedelta(hours=2)
	return corrected_time.strftime("%Y-%m-%d %H:%M:%S")