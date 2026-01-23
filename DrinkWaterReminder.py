#Drink Water Reminder=Write a python program which reminds you of drinking water every one or two hours.Your program can either beep or send a notification for a specific operating system.

# Pick ONE reminder style, not all three

#Simplest version Terminal reminder code:-
import time
from datetime import datetime
# Set reminder interval in seconds (3600 = 1 hour, 7200 = 2 hours)
interval = 3600
while True:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 💧 Time to drink water!")
    time.sleep(interval)

#With Beep Sound:-
import time
import winsound
from datetime import datetime
interval = 3600  # 1 hour
while True:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 💧 Drink water!")
    # Frequency (Hz), Duration (ms)
    winsound.Beep(2500, 1500)
    time.sleep(interval)

#Desktop Notification:-
import time
from plyer import notification ##First we need to install this plyer in our computer trough cmd prompt by typing this "pip install plyer".
from datetime import datetime
interval = 3600  # change to 7200 for 2 hours
while True:
    notification.notify(
        title="💧 Water Reminder",
        message="Go drink a glass of water now!",
        timeout=10  # seconds notification stays)
    )
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Reminder sent")
    time.sleep(interval)