#noti.py
import os
import shelve
d=shelve.open('command_data')
active=open('stillActive.pyhelp', 'w')
active.write("yes")
active.close()
a=open("Events.txt", 'r')
b=a.read()
print(b + " is set to happen now.\nPress <ENTER> to close this alarm")
a.close()
input()
d['muted'] = 0
d.close()
os.remove('Events.txt')
active=open('stillActive.pyhelp', 'w')
active.write("no")
active.close()
exit()
