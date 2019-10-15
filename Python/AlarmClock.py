  
#      By Naveen Balachandran
#
#
#
#
#
#                    Make sure to put a Sound File where directed
#
#
#
#
#
import datetime
import os
import time
def alarm():
    try:
        almtime = input("Enter time for alarm seperated by ':' ")
        times = almtime.split(":")
        datetime = list(time.localtime())
        if datetime[3]>12 and int(times[0])<12:
            times[0] = int(times[0])+12
        hour = datetime[3]
        hleft = int(int(times[0]) - hour)
        minute = datetime[4]
        second = datetime[5]
        mleft = int(int(times[1]) - minute)
        try:
            sleft = int(int(times[2]) - second)
        except:
            sleft = int(0 - second)
        tleft = (hleft*3600)+(mleft*60)+sleft
        print("Alarm will ring in: "+str(tleft)+" secs")
        time.sleep(tleft)
        print("Wake UP")
        os.system("start #here")        #PUT A SOUND FILE PATH HERE
        main()
    except:
        print("You did something wrong!")
        main()
def timer():
    try:
        timer = input("Enter time to wait in hh:mm:ss format")
        timers = timer.split(":")
        hr = int(timers[0])
        mn = int(timers[1])
        sc = int(timers[2])
        timel = (hr*3600)+(mn*60)+(sc)
        print("Timer will end in: "+str(timel)+" secs")
        time.sleep(timel)
        print("Wake UP")
        os.system("start #here")      #PUT A SOUND FILE PATH HERE
        main()
    except:
        print("Ahh! You did something wrong!")
        main()
def main():
    cmd = str.upper(input('''
What do you like to do?
-------------------------
1) Set an Alarm
2)Set a timer
3)Quit
'''))
    if "ALARM" in cmd or cmd == "1":
        alarm()
    elif "QUIT" in cmd or cmd == "3":
        print("Bye")
    elif "TIMER" in cmd or cmd == "2":
        timer()
    else:
        print("What are trying to do ??")
        main()
print('''
     ___       __          ___      .______      .___  ___.      ______  __        ______     ______  __  ___ 
    /   \     |  |        /   \     |   _  \     |   \/   |     /      ||  |      /  __  \   /      ||  |/  / 
   /  ^  \    |  |       /  ^  \    |  |_)  |    |  \  /  |    |  ,----'|  |     |  |  |  | |  ,----'|  '  /  
  /  /_\  \   |  |      /  /_\  \   |      /     |  |\/|  |    |  |     |  |     |  |  |  | |  |     |    <   
 /  _____  \  |  `----./  _____  \  |  |\  \----.|  |  |  |    |  `----.|  `----.|  `--'  | |  `----.|  .  \  
/__/     \__\ |_______/__/     \__\ | _| `._____||__|  |__|     \______||_______| \______/   \______||__|\__\ 
                                                                                                              ''')
main()
