import schedule
import time

def job():
    # Call your fraud detection + insert logic here
    pass

schedule.every(30).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)