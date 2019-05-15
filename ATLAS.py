#----------------------#
#-    Version 1.27    -#
#----   Assistant  ----#
#----------------------#

def changebg(path): # changes background when /path/ is given
    import ctypes
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0) # Don't ask me how this works. it just does.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def hibernate(): # Simple hibernation function.
    import os # Get os imported for hibernation
    
    os.system('shutdown /h') # Hibernate from shell.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def theme(theme):                        # Changes 'themes' according to time or mood.
    import os                            # Import os for directories.
    
    qwe=os.getcwd()                      # Get and store the current directory. This will be important later on.
    print(os.getcwd())                   # Debug (optional)
    
    if theme == 'day':                   # Theme checker IF 1.
        os.chdir('Backgrounds\Day')      # Go to 'day' themed folder.
        
        import random                    # STILL importing stuff xD
        from random import randint       # <insert comment here>
        
        a=random.randint(1, 10)          # Picks a random number for the amount of pictures in the 'day' section. (currently 10)
        
        asd='\day' + str(a)+'.jpg'       # Assemble the picture name. the '\' in '\day' is for the os path to be recognizable
        path=qwe+'\Backgrounds\Day'+asd  # This is where getcwd is used. DIR + section + random number + jpg (all pictures are JPGs)
        print(path)                      # Optional debug again.
        
        changebg(path)                   # Changebg function is called with the now formed path to an existing pictre.
        brightness(50)                   # Brightness will become a preferrable option soon.

######################################################
        
    elif theme == 'night':               # Theme checker IF 2.
        os.chdir('Backgrounds\_Night')   # Go to 'night' themed folder
        
        import random                    # Same as before
        from random import randint       # Makin' sure they're imported.
        
        a=random.randint(1, 10)          # random figure from 1 to 10
        
        asd='\_night' + str(a)+'.jpg'    # assemble image name
        path=qwe+'\Backgrounds\_Night'+asd  # This is tricky. Unicodeescape won't allow me to put \Night because it's a '\n' character... an _ solves everything
        print(path)                      # Optional debug
        
        changebg(path)                   # Changes background like before
        brightness(10)                   # Lowers brightness

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def patch(): # Online patch (local only)
    import socket # Importing socket for server.
    s = socket.socket() # And setting up socket object.

    host = '127.0.0.1'   #Host...
    port = 6789          #And port. These make an address.
    
    while True:          # While true loop for connecting. Brings fail chance to 0
        
        try:             # 'Try' opens error handler
            import time  # import time for retry function.
            s.connect((host, port))  # Try to connect to localhost on port 6789
            break        # If successful, exit this loop.
        
        except Exception as e:  # If not...
            print(str(e))       # Print the cause (kinda debug)
            print("Retrying")   # Notify the user of retry...
            time.sleep(1)       # Wait a second and retry!
            
    import os #once the loop finished, we need the OS module again
    
    self = 'ATLAS.py' #Set up the filename to recognize self.
    st = os.stat(self) # Get stats of the code. INCLUDES SIZE
    #s.send(str(st.st_size).encode())
    
    data = s.recv(20480).decode() # Receive size.
    
    if eval(data) > st.st_size: # If the size is greater than this code's, then this code is outdated. If not, nothing happens.
        print("upgrade needed") # Show the user that upgrades are required.
        
        data = s.recv(20480).decode() #Receive new code. The greater the code, the greater the buffer size has to be. NOTE: work on buffer adjustments.
        print(data)                   #Show the new code.
        
        a = open('ATLAS.py', 'w')     #Open self
        a.write(data)                 #Write new code
        print("done")                 # Done #
        
    else:                       # If the size is smaller...
        print("nope")           # Then notify the user that no upgrades are required.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
        
jokes = ['how did the skeleton know it was going to rain. he felt it in his bones',    # Tons of bad puns. Written by the edgelords of the internet.
         'what did the skeleton say while riding his harry davison\'s. i am bone to be wild.',
         'i know a lot of skeleton jokes. maybe you wil find one; humerus.',
         'what did the doctor say to the skeleton with a cold. you\'re going tibia fine.',
         'i don\' trust stairs... they\'re always up to something.',
         'i\'m reading a book about anti-gravity. it\'s impossible to put down.',
         'i wondered why the baseball was getting bigger. then it hit me.',
         'how did the skeleton know it was going to rain. he read the weather forecast,dummy.' ]

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def speak(words):     #Here's how this code speaks. This makes it stand out from the others.
    import os         # So... Import OS YET AGAIN!

    a = open("speech.vbs", 'w')     # Open the speech VBS file. (It's a nice coding language to learn, VBS is.)
    stuff = 'Dim sapi\nSet sapi=CreateObject("sapi.spvoice")\nsapi.Speak "'+words+'"'     # Set up the file.
    
    a.write(stuff) # Write the file.
    a.close()      # Close the file and save it.
    
    file = 'speech.vbs' #Identi-file.
    os.startfile(file)  #Start it.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def recall_commands(command, s=True):         # This is what makes this code remember stuff.
    import shelve   # Get shelve imported.
    
    cmd = shelve.open("command_data")  # Get the command list directory (yes, it's a dir)
    commands = cmd["cmd"]                   # Store it as a variable.
    
    def fire(func_list):               # Define the command firing code.
        func_list()                    # Command name + () = command fired.
        
    if s == True:                      # 's' stand for 'Show', which is a basic trigger for the firing mechanism
        fire(commands[command])        # Pass args into command
        
    elif s == False or s == None:      # If 's' key is false, then it's a testfire and nothing happens
        pass                           # pass
    
    cmd.close()                        # Close file.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

global asdf #make a random counter globally available.
asdf = 0 #Random counter

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def joke():     #Tells a random joke.
    import random    #Imports 'random' 
    from random import randint # And 'randint'
    
    if asdf == 0:          #Always true counter for reliability
        asd = 0            # Set another random counter.
        
        for x in list(jokes):            # For each item in the 'jokes' list...
            #print(asd)
            asd += 1                     # Increase the counter by 1.
            
        ok = random.randint(1, asd)      # Selected joke is a random number between 1 and the amount of jokes in total
        asda = jokes[ok]                 # Selected joke is stored as a variable (I like keeping variables short, like 'asda' in this case.)
        
        speak(asda)                      # Say the joke stored in the variable.


'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def internet():  #Internet opener.
    import webbrowser            #Gets default browser.
    webbrowser.open("google.com")#Opens google on it

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def yt():     #YouTube opener.
    import webbrowser             #Gets default browser
    webbrowser.open('youtube.com')#Opens youtube.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def mail():   #Opens gmail the same way as 'internet()' and 'yt()'
    import webbrowser
    webbrowser.open("gmail.com")

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def mute(): #Mutes bot input if necessary.
    global asdf   #Make the counter global.
    asdf = 1      #Set the new global counter to 1

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def unmute(): #Unmutes bot input.
    global asdf
    asdf = 0     #Same as before, but this time the counter is 0

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def hi(): #test function
    print("hello there general kenobi")

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

abc={'tell me a joke':joke,       #Defines basic commands
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

def createlib(name='cmd', List=abc):     #Sets up bot commands via defined dictioary.
    import shelve                        # Import shelve
    
    cmd = shelve.open("command_data")    #Create shelve file
    cmd[name] = List                     # Make the data.
    cmd["startupcond"] = 0               #Create startupcond.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

class update:              # Class an update module.
    
    def define(funcname):       #Define the defining of a definition ... @-@
        asd = open('data.pydata', 'w')      # Open a datafile that can't be read by normal users, then make it empty.
        asd.close()     #Close the datafile
        
        d = 'd' #d
        e = 'e' #e
        f= 'f'  #f makes 'def' (won't let the code write 'def' straight in.)
        arguments=input("Arguments (none is added by default, enter to ignore): ")   #Get args if necessary
        
        if arguments != '' and arguments != ' ': #Check that args aren't spaces or empty
            arguments=arguments
        else:
            arguments=''
            
        string = d + e + f + ' ' + funcname + '(' + arguments + '):' #makes 'def <function(args)>'
        
        abc = open('data.pydata', 'a') #open the datafile
        abc.write(string) #Write the data.
        abc.close()  #Close the datafile

#'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
        
    def newline(text):
        """Writes new line in update data."""
        abc = open('data.pydata', 'a') #open file
        
        abc.write('\n') #Write a newline character
        tw = '    ' + text # Add spacing for code after definition.
        
        abc.write(tw)  #Write the line above.

#'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
        
    def ready(confirmation):
        """Updates code according to signal"""
        import time
        
        try:
            if confirmation == 'yes': #Straightforward code
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

#'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
            
    def update(): #Updates this code from new file.
        import os # Get the OS module

        a = open('ATLAS.py', 'r').read() # Grab the file data
        s = open('old.old', 'w')    # Make a backup just in case ;)
        
        s.write(a)  # Fill backup
        s.close()   # Save backup
        
        f = open('ATLAS.py', 'r').read()    # Grab the file data again
        
        limit = 98 # Tell the code how many characters it needs to skip before it writes the code.
        asd = 0    # Set a nul counter
        result = '' # Set string variables for safety measures.
        result2 = '' # Do it again
        count = 0 # Set another nul counter.
        
        for x in f: # For every character in the file...
            
            count += 1 # Increase the counter by 1
            print("UPDATING: <CHAR: " + str(count) + ">", sep='', end='\r') # Inform the user of the progress
            
            if asd <= limit: # If the second counter (responsible for limiting the update) is less than the limit given
                result = result + x # Add the character to the resulting string
                asd +=1 # And increase the counter by 1
                
            elif asd >= limit: # Otherwise...
                result2 = result2 + x # Add the character to the OTHER resultant string. Do NOT update the counter.
                
        #print(result)
        print("UPDATING: <CHAR: " + str(count) + ">") # Fixes unprecise counter glitch.
        print("---------------------------#") # Separation
        print("UPDATE COMPLETE.") # Inform the user that the update is complete. (new file is successfully written)
        
        self = 'ATLAS.py' # Define the name of the file
        
        os.remove(self) # Remove the old version (doesn't close main window)
        okedoke = open(self, 'w') # Open an empty file with the same name
        okedoke.close() # Close it
        
        okedoke = open('ATLAS.py', 'a') # Open that file again in apeend mode
        okedoke.write(result) # Append the first bit 
        okedoke.write('\n') # Write a new line to separate old code from new code.
        
        now = open('data.pydata', 'r').read() # Open the update data file.
        
        okedoke.write('') # Start the line.
        okedoke.write(now) # Write the new code.
        okedoke.write('\n') # Write ANOTHER new line.
        okedoke.write(result2) # Write the rest of the code.
        okedoke.close() # Close and save the new file.
        
        abcd = 'data.pydata' # Identify data file
        
        os.remove(abcd) # Remove data file (no longer required.)
        input("Press <ENTER> to R E S T A R T.") # Waits for user response in case user is AFK
        
        import shelve # Get shelve in
        
        data = shelve.open('command_data') #Open the datastore file.
        data['startupcond'] = 2 # Change the startup conditions for informative message
        data.close() # Close the file

        speak("RESTARTING...") # State the restart.

        selfie = 'ATLAS.py' # Identify the new code

        os.startfile(selfie) # Start the new code.
        exit() # Exit and restart.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def editor(): #Creates update file
    name = input("Function name (will be added)> ") # Get the new function's name

    update.define(name) # Create the definition.

    while 1: # while True loop so that multiple lines of code can be added

        text = input("EDIT (e to exit) > ") # Input the new commands

        if text == 'e': # If the command is 'e', then exit the editor
            break

        if text != 'e': # Otherwise, add the command(s) onto a new line.
            update.newline(text) # This does it.

    update.ready('yes') # Once finished, initiate the update.

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

def close():
    import shelve # Get shelve

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
    import time

    global Shell
    Shell=shell
    
    speak(smsg)
    time.sleep(6)

    print("SPEAK")

    if shell != 1:
        mic = sr.Microphone()
        r = sr.Recognizer()

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
                    import shelve
                    data = shelve.open("command_data")
                    asd = data["cmd"]
                    print(asd)
                    if shell != 1:
                        speak("now say the name of the function")
                        time.sleep(2)
                        print("now")
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
    platform = sys.platform
    import shelve
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
            import shelve
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
            init()
    if 'win' in platform:
        try:
            import PyInstaller
        except:
            os.system("py -m pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz")
            os.system("python -m pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz")
    else:
        pass
def viewcommands():
    import shelve
    data = shelve.open('command_data')
    print(data['cmd'])
def greeting():
    a=['hello!', 'hi!', 'hello again!', 'nice to see you again!', 'welcome back', 'it\'s me again!']
    import random
    asd=random.choice(a)
    return asd


def startup():
    import shelve
    data=shelve.open('command_data')
    if data['manual'] == True:
        skip=1
    try:
        recall_commands('mail', s=None)
    except Exception as e:
        createlib()
    cmd = shelve.open('command_data')
    start = cmd["startupcond"]
    if start == 0:
        global smsg
        smsg = 'Hello, I am ATLAS: the Automated Tool Library and Assist Station. I have now been successfully installed on this device. I can do many things, like expand my command library given user input. Unless installing some prerequisites failed or voice recognition is still not fixed, you can operate me with your voice.'
        if skip != 1:
            checkprerequisites()
        elif skip==1:
            pass
        input("Press ENTER to continue! =]")
        init(shell)
    if start == 1:
        #global smsg
        if skip == 1:
            shell=1
        smsg = greeting()
        init(shell)
    if start == 2:
        #global smsg
        smsg = 'Updates have been installed.'
        if skip == 1:
            shell=1
        init(shell)

#textCmds() all these were used for testing, too lazy to take them out :P
startup()
#hibernate()
#manualedit()
#theme('night')
#manualedit()
#viewcommands()
#input()
#say()
#brightness(1)

