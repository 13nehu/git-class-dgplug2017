import webbrowser
import time

alarmTime=raw_input("Enter the time to wake you in HH:MM -")
maxAlarms = input("Enter the max alarms you want -")
count = 0
snooseTime = input("Enter the snoose time -")
currentTime = time.strftime("%H:%M")

while (count!=maxAlarms):
    if currentTime == alarmTime :
        print("Wake Up")
        webbrowser.open("https://www.youtube.com/watch?v=kJ8ftw6czYY")
    time.sleep(snooseTime * 60)
    count=count+1
