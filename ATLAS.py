import shelve
import os
import datetime
from datetime import datetime
import time
import sys
import subprocess

def createtopic():
    data=shelve.open('command_data')
    
    new=input("Name the new category: ")
    typ=input("type? [list, dict, str or int] > ")
    
    if typ == 'list':
        data[new]=[]
        
    elif typ== 'dict':
        data[new]={}

    elif typ=='str':
        data[new] = ''
        
    elif typ == 'int':
        value=input("Value > ")
        data[new]=value
        
    data.close()
    print("done")

def createevent():
    day=input("Which day? (Please specify according to calendar and to 2 characters like 01. Leave blank for non-specific event) > ")
    
    if day == '' or day == ' ':
        d=''
        
    else:
        d=day+'.'
        
    hour=input("Which hour? (24 hour formatting used) > ")
    event=input("What is the event called? > ")
    
    string=d+hour+'.'+event
    print(string)
    
    data=shelve.open('command_data')
    
    for topic in data:
        print(topic)
        
    decision=input("Which topic is this in? > ")
    
    newEventsList=data[decision]
    newEventsList.append(string)
    
    data[decision]=newEventsList
    print(data[decision])
    data.close()

def cls():
    for x in range(200):
        print('\n')

def config():
    import sys
    import subprocess
    while 1:
        for x in range(200):
            print('\n')
        preferred=input("What % of brightness do you prefer? > ")
        brightness(preferred)
        r = subprocess.run('py --version', stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        pyver=r.stdout.decode()
        print("[1] Brightness: " + preferred + '%')
        if Shell == 1:
            toType='Normal [VoiceRec off]'
        elif Shell == 0:
            toType='Normal [VoiceRec on]'
        elif start == 2 and Shell == 0:
            toType='Recently Updated [VoiceRec on]'
        elif start == 2 and Shell == 1:
            toType='Recently Updated [VoiceRec off]'
        elif start == 0:
            toType='Recently Installed [First boot, VoiceRec on]'
        elif start == 0 and Shell == 1:
            toType='Recently Installed [First boot, VoiceRec off due to missing requirements]'
        print("[2] Startup Condition: " + toType)
        print("---------------------------------------------")
        print("General info:\n    OS : " + sys.platform + "\n    Python Version : " + pyver)
        print("---------------------------------------------")
        import shelve
        data=shelve.open('command_data')
        a=input("Change categories ('e' to exit, 1 for brightness and 2 for startup) \n> ")
        if a.lower() == 'e':
            break
        elif a == '1':
            for x in range(200):
                print('\n')
            print("Current brightness: " + preferred + '%')
            new=input("New brightness: ")
            try:
                new=int(new)
                brightness(new)
            except ValueError:
                print("Not a number.")
                import time
                time.sleep(1)
            for x in range(200):
                print('\n')
        elif a == '2':
            for x in range(200):
                print('\n')
            while 1:
                print("Would you like to enable text prompt\ninstead of voice prompt?")
                voice=input("[Y/N] > ")
                if voice.lower() == 'y' or voice.lower()=='ye' or voice.lower == 'yes':
                    data['manual'] = True
                    val=1
                else:
                    val=0
                    pass
                print("Which startup condition would you like?\n[1]    Normal\n[2]    Recently updated")
                while True:
                    a=input("Choice: ")
                    if a == '1':
                        data['startupcond'] = 1
                        c='Normal'
                        break
                    elif a == '2':
                        data['startupcond'] = 2
                        c='Recently Updated'
                        break
                    else:
                        print("Not a valid choice")
                for x in range(200):
                    print('\n')
                if val == 1:
                    print("Text Prompt mode: [On]")
                elif val == 0:
                    print("Voice Prompt mode [Off]")
                print("Startup Mode: " + c)
                conf=input("--------------------------------------------------\nCONFIRMATION [Y/N] > ")
                if conf.lower() == 'y' or conf.lower() == 'ye' or conf.lower() == 'yes':
                    break
                else:
                    pass

def changebg(path):                                                                 #Changes background when /path/ is given
    import ctypes
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)                      # Don't ask me how this works. it just does.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def brightness(percent):                                                            #Changes brightness with cmd.
    import subprocess                           
    import os                                   

    r = subprocess.run('powercfg -q | find "Power Scheme GUID" & powercfg -q | find "(Display)" & powercfg -q | find "(Display brightness)"',
                       stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)  # Run command to find the 3 screens that are displayed. This is essential.
    
    PowerScheme=r.stdout[19:55].decode()                                            # Find the ID of screen 1 and decode (subprocess returns bytes)
    DisplayBrightness=r.stdout[86:122].decode() 
    Display=r.stdout[159:195].decode()          
    
    Brightness=str(percent)                                                         # Set brightness variable to given percentage. (no need for '%' sign)
    string='powercfg -SetAcValueIndex ' + PowerScheme + ' ' + DisplayBrightness + ' ' + Display + ' ' + Brightness 
    subprocess.run(string, shell=True)                                              # Execute command that sets the power scheme for displays without shell.
    string='powercfg -S ' + PowerScheme                                             # Set the activation command.
    subprocess.run(string, shell=True)                                              # Execute activation command.
    print(r.stderr.decode())

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def hibernate():
    os.system('shutdown /h')                                                        # Hibernate from shell.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def theme(theme):                                                                   #Changes 'themes' according to time or mood. idk. use it as you wish ;]
    
    qwe=os.getcwd()                                                                 # Get and store the current directory. This will be important later on.
    
    if theme == 'day':                   
        os.chdir('Backgrounds\Day')                                                 # Go to 'day' themed folder.
        
        import random                                                               # This import is done because random and randint aren't used anywhere else...
        from random import randint       
        
        a=random.randint(1, 10)                                                     # Picks a random number for the amount of pictures in the 'day' section. (currently 10)
        
        asd='\day' + str(a)+'.jpg'                                                  # Assemble the picture name. the '\' in '\day' is for the os path to be recognizable
        path=qwe+'\Backgrounds\Day'+asd                                             # This is where getcwd is used. DIR + section + random number + jpg (all pictures are JPGs)
        
        changebg(path)                                                              # Changebg function is called with the now formed path to an existing pictre.
        brightness(50)                                                              # Brightness will become a preferrable option soon.


        
    elif theme == 'night':               
        os.chdir('Backgrounds\_Night')                                              # Go to 'night' themed folder
        
        import random                                                               # Same as before
        from random import randint                                                  # Makin' sure they're imported.
        
        a=random.randint(1, 10)                                                     # 10 images, 10 possibilities.
        
        asd='\_night' + str(a)+'.jpg'                                               # Assemble image name.
        path=qwe+'\Backgrounds\_Night'+asd                                          # This is tricky. Unicodeescape won't allow me to put \Night because it's a '\n' character... an _ solves everything
        
        changebg(path)                                                              # Changes background like before
        brightness(10)                                                              # Lowers brightness

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def patch():                                                                        # Online patch (local only)
    import socket                                                                   # Importing socket for server.
    s = socket.socket()                                                             # And setting up socket object.

    host = '127.0.0.1'   
    port = 6789          


    
    while True:         
        
        try:             
            s.connect((host, port))                                                 # Try to connect to localhost on port 6789
            break                                                                   # If successful, exit this loop.
        
        except Exception as e:  
            print(str(e))       
            print("Retrying")                                                       # Notify the user of retry...
            time.sleep(1)                                                           # Wait a second and retry!
            

    
    self = 'ATLAS.py' 
    st = os.stat(self)                                                              # Get stats of the self. [size only]
    
    data = s.recv(20480).decode() 
    
    if eval(data) > st.st_size:                                                     # If the size is greater than this code's, then this code is outdated. If not, nothing happens.
        print("upgrade needed") 

        buffSize = 20480 + eval(data)                                               # As the code is developed, greater buffer size is required.
        data = s.recv(buffSize).decode()                                            # Receive new code. 
        
        a = open('ATLAS.py', 'w')     
        a.write(data)                                                               # Write new code
        print("done")                                                               # Done #
        
    else:                                                                           # If the size is smaller...
        print("nope")                                                               # Then notify the user that no upgrades are required.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
        
jokes = ['how did the skeleton know it was going to rain. he felt it in his bones', # Tons of bad puns. Written by the edgelords of the internet.
         'what did the skeleton say while riding his harry davison\'s. i am bone to be wild.',
         'i know a lot of skeleton jokes. maybe you wil find one; humerus.',
         'what did the doctor say to the skeleton with a cold. you\'re going tibia fine.',
         'i don\' trust stairs... they\'re always up to something.',
         'i\'m reading a book about anti-gravity. it\'s impossible to put down.',
         'i wondered why the baseball was getting bigger. then it hit me.',
         'how did the skeleton know it was going to rain. he read the weather forecast,dummy.' ]

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def speak(words):                                                                   #Here's how this code speaks. This makes it stand out from the others.

    a = open("speech.vbs", 'w')                                                     # Open the speech VBS file. (It's a nice coding language to learn, VBS is.)
    stuff='Dim sapi\nSet sapi=CreateObject("sapi.spvoice")\nsapi.Speak "'+words+'"' # Set up the file.
    
    a.write(stuff) 
    a.close()                                                                       # Close the file and save it.
    
    file = 'speech.vbs'                                                             #Identi-file.
    os.startfile(file)  

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def recall_commands(command, s=True):                                               #This is what makes this code remember stuff.
    
    cmd = shelve.open("command_data")                                               # Get the command list directory (yes, it's a dir and not a list, but I'm too lazy to change it)
    commands = cmd["cmd"]                                                           # Store it as a variable.
    
    def fire(func_list):                                                            # Define the command firing code.
        func_list()                                                                 # Command name + () = command fired. This is useful for tons of stuff... #themoreyouknow
        
    if s == True:                                                                   # 's' stand for 'Show', which is a basic trigger for the firing mechanism
        fire(commands[command])                                                     # Pass args into command
        
    elif s == False or s == None:                                                   # If 's' key is False, then it's a testfire and nothing happens
        pass                           
    
    cmd.close()                                                                     # Close file.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

global asdf                                                                         #This will be important later.
asdf = 0

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def joke():                          
    import random                                                                   # OK nevermind that part about random not being used anywhere else -_-
    from random import randint 

    if asdf == 0:
        asd = 0                                                                     # Set a counter.
            
        for x in list(jokes):
            asd += 1                     
                
        ok = random.randint(1, asd)                                                 # Selected joke is a random number between 1 and the amount of jokes in total
        asda = jokes[ok]                                                            # Selected joke is stored as a variable (I like keeping variables short, like 'asda' in this case. storenames 100)

        speak(asda)                      

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def internet():  
    import webbrowser            
    webbrowser.open("google.com")

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def yt():     
    import webbrowser             
    webbrowser.open('youtube.com')

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def mail():   
    import webbrowser
    webbrowser.open("gmail.com")

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def mute():                                                                         #Told ya that the counter will be useful later on.
    global asdf   
    asdf = 1      

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def unmute(): 
    global asdf
    asdf = 0     

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

abc={'tell me a joke':joke,                                                         #Defines basic commands
     'tell me a pun':joke,
     'make me laugh':joke,
     'internet':internet,
     'mail':mail,
     'gmail':mail,
     'open my mail':mail,
     'open my gmail':mail,
     'YouTube':yt,
     'open YouTube':yt,
     'start YouTube':yt}

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def createlib(name='cmd', List=abc):                                                #@Sets up bot commands via defined dictionary.@
    
    cmd = shelve.open("command_data")                                               # Create shelve file
    cmd[name] = List                                                                # Make the data.
    cmd["startupcond"] = 0               
    cmd['muted'] = 0

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

class update:                                                                       #Class of my signature update module.
    
    def define(funcname):                                                           #Define the defining of a definition ... @-@
        asd = open('data.pydata', 'w')                                              # Open a datafile that can't be read by normal users, then make it empty.
        asd.close()     
        
        d = 'd' 
        e = 'e' 
        f= 'f'                                                                      # Python won't let the code write 'def' straight in.)*
        arguments=input("Arguments (none is added by default, enter to ignore): ")  #Get args if necessary
        
        if arguments != '' and arguments != ' ':                                    #Check that args aren't spaces or empty
            arguments=arguments
            
        else:
            arguments=''
            
        string = d + e + f + ' ' + funcname + '(' + arguments + '):'                #makes 'def <function(args)>'. This is how I bypassed the issue above (marked with a star)
        
        abc = open('data.pydata', 'a') 
        abc.write(string)                                                           #Write the data.
        abc.close()  


        
    def newline(text):
        """Writes new line in update data."""
        abc = open('data.pydata', 'a')
        
        abc.write('\n')                                                             #Write a newline character
        tw = '    ' + text                                                          # Add spacing for code after definition.
        
        abc.write(tw)  


        
    def ready(confirmation):
        """Updates code according to signal"""
        import time
        
        try:
            if confirmation == 'yes': 
                speak("updating in 3; 2; 1. Updating")
                print("Updating in 3...")
                time.sleep(1)
                print("Updating in 2..")
                time.sleep(1)
                print("Updating in 1.")
                time.sleep(1)
                print("Updating...")
                time.sleep(0.25)
                update.update()
                
        except KeyboardInterrupt:
            print("Update cancelled.")

            
    def update():                                                                   #Updates this code from new file.

        a = open('ATLAS.py', 'r').read()                                            # Grab the file data
        s = open('old.old', 'w')                                                    # Make a backup just in case ;)
        
        s.write(a)  
        s.close()                                                                   # Save backup
        
        f = open('ATLAS.py', 'r').read()
        
        limit = 109                                                                 # Tell the code how many characters it needs to skip before it writes the code.
        asd = 0                                                                     # Set a null counter
        result = ''                                                                 
        result2 = '' 
        count = 0                                                                   # Set another nul counter.
        
        for x in f: 
            
            count += 1 
            print("UPDATING: <CHAR: " + str(count) + ">", sep='', end='\r')         # Inform the user of the progress
            
            if asd <= limit:                                                        # If the second counter (responsible for limiting the update) is less than the limit given
                result = result + x                                                 # Add the character to the resulting string
                asd +=1                                                             # And increase the counter by 1
                
            elif asd >= limit: 
                result2 = result2 + x 
                
        #print(result)
        print("UPDATING: <CHAR: " + str(count) + ">")                               # Fixes unprecise display glitch.
        print("---------------------------#") 
        print("UPDATE COMPLETE.")                                                   # Inform the user that the update is complete. (new file is successfully written)
        
        self = 'ATLAS.py' 
        
        os.remove(self)                                                             # \
        okedoke = open(self, 'w')                                                   # -- Clears file.
        okedoke.close() 
        
        okedoke = open('ATLAS.py', 'a') 
        okedoke.write(result)                                                       # Append the first bit
        okedoke.write('\n')                                                         # Write a new line to separate old code from new code.
        
        now = open('data.pydata', 'r').read() 
        
        okedoke.write('')                                                           # Start the line.
        okedoke.write(now)                                                          # Write the new code.
        okedoke.write('\n')                                                         # Separate the code.
        okedoke.write(result2)                                                      # Write the rest of the code.
        okedoke.close() 
        
        abcd = 'data.pydata'                                                        # Identify data file
        
        os.remove(abcd)                                                             # Remove data file (no longer required.)
        input("Press <ENTER> to R E S T A R T.") 
        
        data = shelve.open('command_data') 
        data['startupcond'] = 2                                                     # Change the startup conditions for informative message
        data.close() 

        speak("RESTARTING...") 

        self = 'ATLAS.py' 

        os.startfile(self) 
        exit() 

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def editor():                                                                       #Creates update file
    name = input("Function name (will be added)> ")                                 # Get the new function's name

    update.define(name)                                                             # Create the definition.

    while 1:                                                                        # while True loop so that multiple lines of code can be added

        text = input("EDIT (e to exit) > ")                                         # Input the new commands

        if text == 'e':                                                             # If the command is 'e', then exit the editor
            break

        if text != 'e':                                                             # Otherwise, add the command(s) onto a new line.
            update.newline(text)                                                    # This does it.

    update.ready('yes')                                                             # Once finished, initiate the update.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def close():

    data=shelve.open('command_data') # Get the data up
    data['startupcond'] = 1 # Set start condition to casual

    exit() # Exit.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def say():
    toSay=input("What should I say? > ")
    speak(toSay)

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def init(shell):
    import speech_recognition as sr

    global Shell
    Shell=shell
    
    speak(smsg)
    time.sleep(6)

    if shell != 1:
        mic = sr.Microphone()
        r = sr.Recognizer()
        print("SPEAK")

    asdf = 0

    while True:
        try:
            if shell != 1:
                with mic as source:
                    audio = r.listen(source)

                inp = r.recognize_google(audio)
                print(inp)
                
            elif shell == 1:
                inp=input("PROMPT > ")


                
            try:
                recall_commands(inp)
                continue
            
            except Exception as e:
                print(str(e))
                speak("Sorry, I don't know that one. Add to library?")
                
                time.sleep(4)
                print("ADD?")


                
                if shell != 1:
                    with mic as source:
                        audio = r.listen(source)
                        
                    decision = r.recognize_google(audio)


                    
                elif shell == 1:
                    decision=input("[Y/N] ")
                    decision=decision.lower()


                    
                if decision == 'yes' or decision=='ye' or decision == 'y':
                    if shell != 1:
                        speak("Say the name of the trigger.")
                        
                        time.sleep(1.5)
                        print("Now.")
                        
                        with mic as source:
                            audio = r.listen(source)
                            
                        name = r.recognize_google(audio)


                        
                    elif shell == 1:
                        speak("Type the name of the trigger.")
                        name=input("Trigger name > ")


                        
                    data = shelve.open("command_data")
                    asd = data["cmd"]
                    print(asd)


                    
                    if shell != 1:
                        speak("now say the name of the function")
                        time.sleep(2)
                        print("now (say manual for manual input)")
                        
                        with mic as source:
                            audio = r.listen(source)
                            
                        func = r.recognize_google(audio)
                        
                        if func == 'manual':
                            func=input("Function name > ")


                            
                    elif shell == 1:
                        speak("now type the name of the function")
                        func=input("Function name > ")


                        
                    try:
                        ok = {name:eval(func)}
                        asd.update(ok)
                        
                        print(asd)
                        
                        data["cmd"] = asd
                        data.close()
                        
                        speak("Thank you for helping me understand")
                        continue
                    
                    except NameError:
                        speak("the function you are trying to give me is undefined. open editor?")
                        time.sleep(7)
                        
                        print("open?")


                        
                        if shell != 1:
                            with mic as source:
                                audio = r.listen(source)
                                
                            yn = r.recognize_google(audio)
                            
                        elif shell == 1:
                            yn=input("[Y/N] ")
                            yn=yn.lower()


                            
                        if yn == 'yes' or yn == 'y' or yn == 'ye':
                            editor()
                            
                        elif yn == 'no' or yn == 'n':
                            speak("ok.")
                            continue


                        
                elif decision == 'no' or decision == 'n':
                    speak("ok, got it")
                    time.sleep(1.5)
                    continue
            
        except Exception as e:
            print("oops " +str(e))


            
def checkprerequisites():
    import shelve
    import socket
    import os
    import time
    import sys
    global platform
    import shelve
    
    platform = sys.platform
    data=shelve.open('command_data')


    
    try:
        if data['manual'] == True:
            init()
            
    except:
        data['manual']=False
        data.close()


        
    else:
        try:
            import speech_recognition as sr
            
        except ImportError:
            print("SpeechRecognition is required to install the program you are trying to run.")
            ask = input("Install module? \n[Y/N]>")


            
            if ask.lower() == 'y' or ask.lower() == 'ye' or ask.lower() == 'yes':
                platform = sys.platform
                
                if 'win' in platform:
                    
                    os.system("python -m pip install SpeechRecognition")
                    os.system("py -m pip install SpeechRecognition")
                    
                    try:
                        import speech_recognition as sr
                        
                    except Exception as e:
                        print("Please install Speech Recognition with the following command(s):\npy -m pip install SpeechRecognition\nOR\npython -m pip install SpeechRecognition\n-----------------------------")
                        input("Installation PAUSED [Press ENTER to continue (but please have the modules installed.).] >")
                        
                elif 'linux' in platform:
                    os.system("sudo apt-get install python-SpeechRecognition")
                    os.system("sudo pip3 install SpeechRecognition")
                    os.system("sudo apt-get install python-pyaudio python3-SpeechRecognition")
                    
                    try:
                        import speech_recognition as sr
                        
                    except Exception as e:
                        print("Please install Speech Recognition with the following command(s):\nsudo apt-get install python-SpeechRecognition\nOR\nsudo pip3 install SpeechRecognition\nOR EVEN\nsudo apt-get install python-pyaudio python3-pyaudio\n--------------------------")
                        input("Installation PAUSED [Press ENTER to continue (but please have the modules installed.).] >")
                        
                elif 'mac' in platform:
                    print("Sorry, currently this operating system type is unsupported for installation. Please be patient, as we are working on fixing this.")
                    time.sleep(5)
                    exit()
                    
            elif ask.lower() == 'n' or ask.lower() == 'no':
                print("Alright, then. See you later.")
                time.sleep(2)
                exit()
        try:
            import pyaudio
            
        except ImportError:
            ask = input("PyAudio is a prerequisite of SpeechRecognition. Install it? \n[Y/N]>")
            
            if ask.lower() == 'y' or ask.lower() == 'ye' or ask.lower() == 'yes':
                
                if 'win' in platform:
                    
                    os.system("python -m pip install pyaudio")
                    os.system("py -m pip install pyaudio")
                    
                    try:
                        import speech_recognition as sr
                        
                    except Exception as e:
                        print("Please install PyAudio with the following command(s):\npy -m pip install pyaudio\nOR\npython -m pip install pyaudio\n-----------------------------")
                        input("Installation PAUSED [Press ENTER to continue (but please have the modules installed.).] >")
                        
                elif 'linux' in platform:
                    os.system("sudo apt-get install python-pyaudio")
                    os.system("sudo pip3 install pyaudio")
                    os.system("sudo apt-get install python-pyaudio python3-pyaudio")
                    
                    try:
                        import speech_recognition as sr
                        
                    except Exception as e:
                        print("Please install PyAudio with the following command(s):\nsudo apt-get install python-pyaudio\nOR\nsudo pip3 install pyaudio\nOR EVEN\nsudo apt-get install python-pyaudio python3-pyaudio\n--------------------------")
                        input("Installation PAUSED [Press ENTER to continue (but please have the modules installed.).] >")
                        
                elif 'mac' in platform:
                    print("Sorry, currently this operating system type is unsupported for installation. Please be patient, as we are working on fixing this.")
                    time.sleep(5)
                    exit()
                    
            elif ask.lower() == 'n' or ask.lower() == 'no':
                print("Alright, then. See you later.")
                time.sleep(2)
                exit()

    try:
        import speech_recognition as sr
        import pyaudio
        
    except:
        print("Could not import requirements.")
        ask=input("Use manual command line? [Y/N] ")
        
        if ask.lower() == 'y' or ask .lower() == 'ye' or ask.lower() == 'yes':
            data=shelve.open('command_data')
            data['manual']=True
            data.close()
            
            bypass=1
            
        elif ask.lower() == 'n' or ask.lower() == 'no':
            pass
        
        if bypass != 1:
            exit()
            
        elif bypass == 1:
            global shell
            shell=1
            
            init(shell)


            
    if 'win' in platform:
        
        try:
            import PyInstaller
            
        except:
            os.system("py -m pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz")
            os.system("python -m pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz")
            
    else:
        pass
    
def viewcommands():
    data = shelve.open('command_data')
    print(data['cmd'])
    
def greeting():
    import random
    
    a=['hello!', 'hi!', 'hello again!', 'nice to see you again!', 'welcome back', 'it\'s me again!']
    asd=random.choice(a)
    
    return asd

def Muted(message="Event active"):

    while True:
        time.sleep(0.1)
        print(message + " [waiting for event deactivation.]", sep='', end='\r')
        
        a=open("stillActive.pyhelp", 'r')
        b=a.read()
        
        if b == 'yes':
            pass
        
        elif b == 'no':
            self='ATLAS.py'
            os.startfile(self)
            exit()

def textCmds():
    global shell
    shell=1

def writePID():
    a=os.getpid()
    
    asd=open('pid.pid', 'w')
    
    asd.write(str(a))
    asd.close()

def startResponse():
    data=shelve.open('command_data')

    if data['manual'] == 'True':
        skip = 1
        
    elif data['manual'] == 'False':
        skip = 0
        
    start = data["startupcond"]
    muted=data['muted']
    
    if muted == 0:
        pass
    
    elif muted == 1:
        start=3

    return [start, muted, skip]



def startup():

    startData = startResponse()
    start=startData[0]
    muted=startData[1]
    skip=startData[2]
    
    try:
        recall_commands('mail', s=None)
        
    except Exception as e:
        createlib()


        
    if start == 0:
        global smsg
        smsg = 'Hello, I am ATLAS: the Automated Tool Library and Assist Station. I have now been successfully installed on this device. I can do many things, like expand my command library given user input. Unless installing some prerequisites failed or voice recognition is still not fixed, you can operate me with your voice.'
        
        if skip == 0:
            checkprerequisites()
            
        elif skip==1:
            shell=1
            pass
        
        init(shell)


        
    if start == 1:
        
        if skip == 1:
            shell=1
            
        smsg = greeting()
        init(shell)
        
    if start == 2:
        smsg = 'Updates have been installed.'
        
        if skip == 1:
            shell=1
            
        init(shell)


        
    if start == 3:
        Muted("Waiting for alarm to end")

startup()
