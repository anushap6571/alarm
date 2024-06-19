import time
import os
from playsound import playsound


def main():
    time_w_colon = input("Enter the time: ")

    times = time_w_colon.split(":")
    print(times[0])
    print(times[1])
    target_hour = int(times[0])
    target_minute = int(times[1])

    now = time.localtime()
    
    hour = now.tm_hour%12
    minute = now.tm_min
    print(hour)
    print(minute)
    stop = False
    #playsound("/Applications/python_projects/alarm/radar.mp3")
    while not stop:
        now = time.localtime()
        hour = now.tm_hour
        minute = now.tm_min
        print("check")
        print(type(minute))
        print(type(target_minute))
        if hour == target_hour and minute == target_minute:
            stop = True
            print("alarm")
            #playsound("/Applications/python_projects/alarm/radar.mp3")
            break
        time.sleep(30)
        

if __name__ == "__main__":
    main()