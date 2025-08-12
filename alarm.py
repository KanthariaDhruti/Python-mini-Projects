import datetime
import time

# Step 1: Get alarm time from user
alarm_time = input("Enter alarm time (HH:MM:SS) in 24-hour format: ")

print(f"Alarm set for {alarm_time}...")

# Step 2: Keep checking the time
while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("Wake up! ⏰")
        break
    time.sleep(1)  # Wait 1 second before checking again
