import pyttsx3 as p 
import os as o

open='''
open do it pls open it
'''
help='''
__________________________________________________
**************************************************
|                                                 |
| Default OS      : Lin (GNU Linux)               |
| -h              : for help                      |
| exit|quit       : to exit out of program        |
| -h Win          : get list of windows program   |
| -h Lin          : get list of linux programs    |
| exec            : To run the commands directly  |
|                   Only  available for Linux     |
| run             : run program_name file         |

**************************************************
--------------------------------------------------
'''

winos='''
List of Windows Programs are:
      VLC
      Notepad
      Wmplayer
      chrome
      ipconfig
'''
linos='''
List of Linux Programs are:
clear             [Clear the screen]
vlc               [PATH TO FILE]
gedit             [PATH TO FILE]
firefox           [WEB URL]
chromium          [WEB URL]
wget              [URL TO Retrive]
curl              [URL To Retrive]
Install           [To Install Package]
Ping              [Hostname || IP Addr]
ipconfig
virtualbox

'''
stin='''
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗     ███╗   ███╗██╗   ██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    ████╗ ████║╚██╗ ██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║    ██╔████╔██║ ╚████╔╝        ██║   ██║   ██║██║   ██║██║     ███████╗
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║    ██║╚██╔╝██║  ╚██╔╝         ██║   ██║   ██║██║   ██║██║     ╚════██║
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝    ██║ ╚═╝ ██║   ██║          ██║   ╚██████╔╝╚██████╔╝███████╗███████║
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝     ╚═╝     ╚═╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                                                                                                                           '''

p.speak("Welcome to my tools")
print("For help use help or -h")
ost="Lin"
ost=input("Input you OS Win || Lin :")
while True:
  if("Win" in ost):
    print("--------------------------")
    print(stin)
    print("--------------------------")
    print("Your Choices:"  , end='')
    p = input()

    if ("-h Win" in p):
      print(winos)
    elif  ("-h Lin" in p):
      print(linos)
    elif ("run" in p)  and ("chrome" in p):
      o.system("chrome")

    elif (("run" in p) or  ("execute" in p )) and  (("notepad" in p) or ("editor" in p) ) :
      o.system("notepad")

    elif ("run" in p)  and ("player" in p) and ("media" in p):
      o.system("wmplayer")

    elif  ("exit" in p)  or ("quit" in p):
      break

    else:
      print("Please see the help")
      print(help)
  
  elif ("Lin" in ost or "lin" in ost or "Linix" in ost):
    
    print("--------------------------")
    o.system("cat stin|lolcat")
    print("--------------------------")
    
    print("Your Choices:"  , end='')
    p=input()
    

    if ("-h Win" in p):
      print(winos)
    elif  ("exit" in p)  or ("quit" in p):
      break
    elif("clear screen" in p):
      o.system("clear")
    elif  ("-h Lin" in p):
      print(linos)
    elif("exec" in p):
      while exec!=q:
        exec=input("Entre the command to execute or q to quit:",end='')
        if(exec!=q):
          o.system("exec")
    elif("run" in p) and ("gedit" in p):
      o.system("gedit")
    elif("run" in p) and ("vlc" in p):
      o.system("vlc")
    elif("run" in p) and ("firefox" in p):
      o.system("firefox")
    elif("run" in p) and ("chromium" in p):
      o.system("chromium")
    elif("install" in p) or ("Install" in p):
      pro=input("Program to Install")
      o.system("sudo apt install "+str(pro))
    else:
      print("Please see the help & enter valid option")
      print(help)
     
  else:
    
    print("Please see the help & enter valid option")
    print(help)
    print("Please entre valid OS Lin || Win (Linux || Windows)")
    ost=input()





