import time
from plyer import notification

while True:
    print("please sip some water")
    notification.notify(title="please drink some water",
                       message= "You need to drink some water")
    time.sleep(60*60)
