from datetime import datetime, timedelta
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

def getCurrentDateTimeIso():
	environment = os.getenv('ENVIRONMENT')
	now = datetime.now()
	if environment != 'development':
		now = now + timedelta(hours=2)
	return now.strftime("%Y-%m-%d %H:%M:%S")