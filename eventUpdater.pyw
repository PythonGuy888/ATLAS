import time
import os
from datetime import datetime
import shelve
def getdatetime():
    CDT=datetime.now()
    year=CDT.year
    month=CDT.month
    day=CDT.day
    hour=CDT.hour
    minute=CDT.minute
    return [year, month, day, hour, minute]

def timegate():
    DT=getdatetime()
    data=shelve.open('command_data')
    event_list=data['events']
    for item in event_list:
        print(item)
        if item.startswith(str(DT[2])):
            event_day=item[:2]
            event_hour=item[3:5]
            try:
                test=int(event_hour)
                
                if event_hour == str(DT[3]):
                    a=open("Events.txt", 'w')
                    toWrite = item[6:]
                    a.write(toWrite)
                    a.close()
                    file='noti.py'
                    os.startfile(file)
                    tempList=data['events']
                    toPop=tempList.index(item)
                    tempList.pop(toPop)
                    print(toPop)
                    data['events']=tempList
                    data['muted'] = 1
                    data.close()
                    pid=open('pid.pid', 'r').read()
                    import subprocess as s
                    s.Popen('taskkill /F /PID {0}'.format(pid), shell=True)
                    toStart='ATLAS.py'
                    os.startfile(toStart)
            except Exception as e:
                print(str(e))
                continue
        elif item.startswith(str(DT[3])):
            a=open("Events.txt", 'w')
            toWrite=item[3:]
            a.write(toWrite)
            a.close()
            file='noti.py'
            os.startfile(file)
            tempList=data['events']
            toPop=tempList.index(item)
            tempList.pop(toPop)
            data['events']=tempList
            data['muted'] = 1
            data.close()
            pid=open('pid.pid', 'r').read()
            import subprocess as s
            s.Popen('taskkill /F /PID {0}'.format(pid), shell=True)
            toStart='ATLAS.py'
            os.startfile(toStart)
            
while True:
    time.sleep(0.1)
    timegate()
