import os
import random
from Chess.images import ChessMain3 as chess
from os import startfile
import cv2
import numpy as np
import pandas as pd
import time
import webbrowser


def clearscreen():
    os.system('cls')


def mainmenu():
    print('''
    
    Welcome to Helpfulbot Python
    
    What would you like to work on today?
    
    1. Notes
    2. Entertainment
    3. Toolbox
    4. Personal Notes
    5. About Helpfulbox
    6. Exit
    
    
    ''')
    mainmenuchoice = input(' ').lower()

    if mainmenuchoice == 'notes' or mainmenuchoice == '1':
        clearscreen()
        notes()
    elif mainmenuchoice == 'entertainment' or mainmenuchoice == '2':
        clearscreen()
        entertainmentmenu()
    elif mainmenuchoice == 'personal notes' or mainmenuchoice == '4':
        personalnotesmenu()
    elif mainmenuchoice == 'exit' or mainmenuchoice == '6':
        print('Goodbye')
        quit()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        mainmenu()

def personalnotesmenu():
    clearscreen()
    print('''
    Welcome to Personal Notes!
    
    1. Birthdays
    2. Emails
    3. League Accounts
    4. Journal
    5. Python Ideas
    6. Exit''')

    personalnotesmenuchoice = input(' ').lower()

    if personalnotesmenuchoice == 'birthdays' or personalnotesmenuchoice == '1':
        personalnotesbirthdaysmenu()
    elif personalnotesmenuchoice == 'emails' or personalnotesmenuchoice == '2':
        print(underconstruction)
        personalnotesmenu()
    elif personalnotesmenuchoice == 'league accounts' or personalnotesmenuchoice == '3':
        personalnotesleagueaccounts()
        personalnotesmenu()
    elif personalnotesmenuchoice == 'journal' or personalnotesmenuchoice == '4':
        print(underconstruction)
        personalnotesmenu()
    elif personalnotesmenuchoice == 'python ideas' or personalnotesmenuchoice == '5':
        personalnotespythonideasmenu()
    elif personalnotesmenuchoice == 'exit' or personalnotesmenuchoice == '6':
        clearscreen()
        mainmenu()
    else:
        print(imsorry)
        input(' ')
        personalnotesmenu()

def personalnotesbirthdaysmenu():
    print('''
    Who's Birthday information did you need?
    
    1. Siblings
    2. Max
    3. April
    4. Others
    5. Exit
    
    ''')

    personalnotesbirthdaysmenuchoice = input(' ').lower()

    if personalnotesbirthdaysmenuchoice == 'siblings' or personalnotesbirthdaysmenuchoice == '1':
        print(siblingbirthday)
        input(' ')
        clearscreen()
        personalnotesbirthdaysmenu()
    elif personalnotesbirthdaysmenuchoice == 'max' or personalnotesbirthdaysmenuchoice == '2':
        print(maxbirthday)
        input(' ')
        clearscreen()
        personalnotesbirthdaysmenu()
    elif personalnotesbirthdaysmenuchoice == 'april' or personalnotesbirthdaysmenuchoice == '3':
        print(aprilbirthday)
        input(' ')
        clearscreen()
        personalnotesbirthdaysmenu()
    elif personalnotesbirthdaysmenuchoice == 'others' or personalnotesbirthdaysmenuchoice == '4':
        print(othersbirthday)
        input(' ')
        clearscreen()
        personalnotesbirthdaysmenu()
    elif personalnotesbirthdaysmenuchoice == 'exit' or personalnotesbirthdaysmenuchoice == '5':
        clearscreen()
        personalnotesmenu()
    else:
        print(imsorry)
        input(' ')
        personalnotesbirthdaysmenu()



siblingbirthday = '''Phenix's birthday is on March 17th
Chynna's birthday is on March 28th
Reeve's birthday is on August 29th
'''
maxbirthday = "Max's birthday is on June 13th"
aprilbirthday = "April's birthday is on September 20th"
otherbirthdays = '''Goose's birthday is on May 2nd
                 River's birthday is on September 22nd
                 Steven's birthday is on May 28th'''


def personalnotesleagueaccounts():
    print('Here is your league account info')
    f = open('D:\Sterling\Passwords\LoLNamesandPass.txt', 'r')
    print(f.read())
    print('Would you like to open the text file with notepad?')
    personalnotesleagueaccountschoice = input(' ').lower()

    if personalnotesleagueaccountschoice == 'yes':
        startfile('D:\Sterling\Passwords\LoLNamesandPass.txt')
        personalnotesmenu()
    else:
        personalnotesmenu()


def notes():
    clearscreen()
    print('''
    
    Welcome to Notes!
    
    1. Spanish
    2. Crash Course (Youtube)
    3. Finance for Everyone: Decisions
    4. Exit
    
    ''')

    noteschoice = input(' ').lower()

    if noteschoice == 'spanish' or noteschoice == '1':
        clearscreen()
        spanishmenu()
    elif noteschoice == 'crash course' or noteschoice == 'crash course youtube' or noteschoice == 'crash course (' \
                                                                                                  'youtube)' or \
            noteschoice == 'crash course yt' or noteschoice == '2':
        clearscreen()
        crashcoursemenu()
    elif noteschoice == 'exit' or noteschoice == '4':
        clearscreen()
        mainmenu()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        notes()


def crashcoursemenu():
    print('''
    Welcome to the Crash Course menu!
    What would you like to look at today?
    
    1. US History
    2. Philosophy
    3. Exit
    
    
    
    ''')

    crashcoursemenuchoice = input(' ').lower()

    if crashcoursemenuchoice == 'us history' or crashcoursemenuchoice == '1':
        clearscreen()
        crashcoursemenuhistory()
    elif crashcoursemenuchoice == 'philosophy' or crashcoursemenuchoice == '2':
        clearscreen()
        crashcoursephilosphy()
    elif crashcoursemenuchoice == 'exit' or crashcoursemenuchoice == '3':
        clearscreen()
        notes()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        crashcoursemenu()


def crashcoursemenuhistory():
    print('''
    Here are your notes on Crash Course US History.
    
    1. The Black Legend
    2. Native Americans
    3. Spaniards
    4. Exit
    
    ''')

    crashcoursemenuhistorychoice = input(' ').lower()

    if crashcoursemenuhistorychoice == 'the black legend' or crashcoursemenuhistorychoice == '1':
        clearscreen()
        crashcourseushistorytheblacklegend()
    elif crashcoursemenuhistorychoice == 'native americans' or crashcoursemenuhistorychoice == '2':
        pass
    elif crashcoursemenuhistorychoice == 'spaniards' or crashcoursemenuhistorychoice == '3':
        pass
    elif crashcoursemenuhistorychoice == 'exit' or crashcoursemenuhistorychoice == '4':
        clearscreen()
        crashcoursemenu()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        crashcoursemenuhistory()


def crashcourseushistorytheblacklegend():
    theblacklegendnotes = open('D:\Sterling\Helpfulbot\TheBlackLegend.txt', 'r')
    print(theblacklegendnotes.read())
    print("\n"
          "I am currently not programmed with any more info the subject currently, so we will have to go back to the "
          "menu, to exit these notes simply type in 1 or exit\n "
          "    ")

    crashcoursehistorytheblacklegendchoice = input(' ').lower()

    if crashcoursehistorytheblacklegendchoice == 'exit' or crashcoursehistorytheblacklegendchoice == '1':
        clearscreen()
        crashcoursemenuhistory()
    else:
        print(imsorry)
        crashcourseushistorytheblacklegend()


def crashcoursemenuphilosophy():
    print('''
    Sorry this page is still under construction
    ''')
    crashcoursemenu()


def spanishmenu():
    print('''
    
    What would you like to work on?
    
    1. Vocab
    2. Sentences
    3. Exit
    
    
    ''')

    spanishmenuchoice = input(' ').lower()

    if spanishmenuchoice == 'vocab' or spanishmenuchoice == '1':
        clearscreen()
        spanishvocabmenu()
    elif spanishmenuchoice == 'sentences' or spanishmenuchoice == '2':
        clearscreen()
        print('im sorry the sentences are not available in this version of helpfulbot')
        spanishmenu()
    elif spanishmenuchoice == 'exit' or spanishmenuchoice == '3':
        clearscreen()
        mainmenu()
    else:
        print(imsorry)
        input('')
        clearscreen()
        spanishmenu()


def spanishvocabmenu():
    print('''
    
    Spanish Vocab Menu
    1. Vocab set 1
    2. Vocab set 2
    3. Exit
    
    
    ''')

    spanishvocabmenuchoice = input(' ').lower()

    if spanishvocabmenuchoice == 'vocab set 1' or spanishvocabmenuchoice == '1':
        clearscreen()
        spanishvocabset1v2()
    elif spanishvocabmenuchoice == 'vocab set 2' or spanishvocabmenuchoice == '2':
        spanishvocabset2()
        clearscreen()
        spanishvocabmenu()
    elif spanishvocabmenuchoice == 'exit' or spanishvocabmenuchoice == '3':
        clearscreen()
        spanishmenu()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        spanishvocabmenu()


def entertainmentmenu():
    print('''
    
    What would you like to do?
    1. Games
    2. Sports
    3. Videos
    4. Exit
    
    ''')

    entertainmentmenuchoice = input(' ').lower()

    if entertainmentmenuchoice == 'games' or entertainmentmenuchoice == '1':
        clearscreen()
        entertainmentgamesmenu()
    elif entertainmentmenuchoice == 'sports' or entertainmentmenuchoice == '2':
        clearscreen()
        entertainmentsports()
    elif entertainmentmenuchoice == 'videos' or entertainmentmenuchoice == '3':
        clearscreen()
        entertainmentmenuvideos()
    elif entertainmentmenuchoice == 'exit' or entertainmentmenuchoice == '4':
        clearscreen()
        mainmenu()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        entertainmentmenu()


def entertainmentgamesmenu():
    print('''
    Welcome to the Games page!
    
    1. Rock Paper Scissors
    2. Chess
    3. Exit
    
    ''')

    entertainmentgamesmenuchoice = input(' ').lower()
    if entertainmentgamesmenuchoice == 'rock paper scissors' or entertainmentgamesmenuchoice == '1':
        print(underconstruction)
        clearscreen()
        entertainmentgamesmenu()
    elif entertainmentgamesmenuchoice == 'chess' or entertainmentgamesmenuchoice == '2':
        if __name__ == '__main__':
            chess.main()
            clearscreen()
            entertainmentgamesmenu()
    elif entertainmentgamesmenuchoice == 'exit' or entertainmentgamesmenuchoice == '3':
        entertainmentmenu()
    else:
        print(imsorry)
        clearscreen()
        entertainmentgamesmenu()


def entertainmentsports():
    print(underconstruction)
    input(' ')
    clearscreen()
    entertainmentmenu()


def entertainmentmenuvideos():
    print('''
    Here are some videos currently accessible by HelpfulBot
    
    1. South Park Bigger, Longer, and Uncut
    2. Big Hero 6
    3. Spongebob Squarepants
    4. Exit
    ''')

    entertainmentmenuvideoschoice = input(' ').lower()

    if entertainmentmenuvideoschoice == 'southpark bigger longer and uncut' \
            or entertainmentmenuvideoschoice == 'southpark bigger, longer, and uncut' \
            or entertainmentmenuvideoschoice == '1':
        startfile("D:\Sterling\Video\Movies\South Park Bigger, Longer & Uncut (1999)\SouthParkBiggerLongerandUncut.mkv")
        entertainmentmenuvideos()
    elif entertainmentmenuvideoschoice == 'big hero 6' or entertainmentmenuvideoschoice == '2':
        startfile("D:\Sterling\Video\Movies\Big Hero 6 (2014)\Big.Hero.6.2014.720p.BluRay.x264.YIFY.mp4")
        entertainmentmenuvideos()
    elif entertainmentmenuvideoschoice == 'spongebob squarepants' or entertainmentmenuvideoschoice == 'spongebob' or entertainmentmenuvideoschoice == '3':
        entertainmentvideosspongebobmenu()
    elif entertainmentmenuvideoschoice == 'exit' or entertainmentmenuvideoschoice == '4':
        entertainmentmenu()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        entertainmentmenuvideos()


def southparkbiggerlongeranduncut():
    print('Enjoy the show!')
    startfile("D:\Sterling\Video\Movies\South Park Bigger, Longer & Uncut (1999)\SouthParkBiggerLongerandUncut.mkv")
    entertainmentmenuvideos()

    # video = cv2.VideoCapture("D:\Sterling\Video\Movies\South Park Bigger, Longer & Uncut (1999)\SouthParkBiggerLongerandUncut.mkv")

    # while(video.isOpened()):
    #    ret,frame = video.read()

    #    frame = cv2.resize(frame, (1920, 1080))

    #    cv2.imshow("video", frame)

    #    if cv2.waitKey(10) & 0xFF == ord('q'):
    #        break
    #        entertainmentmenuvideos()


def bighero6():
    print('Enjoy the show!')
    startfile("D:\Sterling\Video\Movies\Big Hero 6 (2014)\Big.Hero.6.2014.720p.BluRay.x264.YIFY.mp4")
    entertainmentmenuvideos()

    # clearscreen()
    # print('Enjoy the show! Press q to exit the video at any time')

    # video = cv2.VideoCapture(
    #    "D:\Sterling\Video\Movies\Big Hero 6 (2014)\Big.Hero.6.2014.720p.BluRay.x264.YIFY.mp4")

    # while (video.isOpened()):
    #    ret, frame = video.read()

    #    frame = cv2.resize(frame, (1920, 1080))

    #    cv2.imshow("video", frame)

    #    if cv2.waitKey(10) & 0xFF == ord('q'):
    #        break
    #        entertainmentmenuvideos()

def entertainmentvideosspongebobmenu():
    print('''
    
    Which season would you like to watch?
    
    1. Season 1
    2. Season 2
    3. Season 3
    4. Exit
    
    
    ''')

    entertainmentvideosspongebobmenuchoice = input(' ').lower()

    if entertainmentvideosspongebobmenuchoice == 'season 1' or entertainmentvideosspongebobmenuchoice == '1':
        webbrowser.get('chrome').open_new(
            "https://www.amazon.com/Help-Wanted-Reef-Blowers-Treedome/dp/B0076QMOOG/ref=sr_1_1?crid=2NUYG86F4DQUB&keywords=spongebob+season+1&qid=1660302132&sprefix=spongebob+season+1%2Caps%2C83&sr=8-1")
        entertainmentvideosspongebobmenu()
    if entertainmentvideosspongebobmenuchoice == 'season 2' or entertainmentvideosspongebobmenuchoice == '2':
        webbrowser.get('chrome').open_new(
            "https://www.amazon.com/Sailor-Mouth-Artist-Unknown/dp/B0076QAL7I/ref=sr_1_2?crid=8XKBPWNGAH0&keywords=spongebob+season+2&qid=1660893232&sprefix=spongebob+season+2%2Caps%2C91&sr=8-2")
        entertainmentvideosspongebobmenu()
    if entertainmentvideosspongebobmenuchoice == 'exit' or entertainmentvideosspongebobmenuchoice == '4':
        entertainmentmenuvideos()
    else:
        print(imsorry)
        entertainmentvideosspongebobmenu()


def jugarfunction():
    print('''
    What does Jugar mean?
    ''')

    jugarfunctionchoice = input('   ').lower()

    if jugarfunctionchoice == 'to play':
        print('''
    Good job!
        
    Jugar means to play!''')
        input('')
        clearscreen()
    elif jugarfunctionchoice == 'exit' or jugarfunctionchoice == 'quit':
        print('time to study more next time!')
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        jugarfunction()


def correrfunction():
    print('''
    What does Correr mean?
    ''')

    correrfunctionchoice = input('   ').lower()

    if correrfunctionchoice == 'to run':
        print('''
    Good job!

    Correr means to run!''')
        input(' ')
        clearscreen()
    elif correrfunctionchoice == 'exit' or correrfunctionchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        correrfunction()


def caminarfunction():
    print('''
    What does Caminar mean?
    ''')
    caminarfunctionchoice = input('     ').lower()

    if caminarfunctionchoice == 'to walk':
        print('''
    Good job!

    Caminar means to walk!''')
        input('  ')
        clearscreen()
    elif caminarfunctionchoice == 'exit' or caminarfunctionchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        caminarfunction()


def nadarfunction():
    print('''
    What does Nadar mean?
    ''')
    nadarfunctionchoice = input('   ').lower()

    if nadarfunctionchoice == 'to swim':
        print('''
    Good job!

    Nadar means to swim!''')
        input(' ')
        clearscreen()
    elif nadarfunctionchoice == 'exit' or nadarfunctionchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        nadarfunction()


#Where I stored my variables

imsorry = "I'm sorry I didn't understand that"
imsorrywrong = "I'm sorry that isn't the correct answer"
underconstruction = "I'm sorry this page is still under construction"
chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

#Where I am registering webbrowser

webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))

def spanishvocabset1v2():
    spanishvocabset1list = [1, 2, 3, 4]
    spanishvocabset1v2choice = random.sample(spanishvocabset1list, 4)
    if spanishvocabset1v2choice == [1, 2, 3, 4]:
        jugarfunction()
        correrfunction()
        caminarfunction()
        nadarfunction()
    elif spanishvocabset1v2choice == [1, 2, 4, 3]:
        jugarfunction()
        correrfunction()
        nadarfunction()
        caminarfunction()
    elif spanishvocabset1v2choice == [1, 3, 2, 4]:
        jugarfunction()
        caminarfunction()
        correrfunction()
        nadarfunction()
    elif spanishvocabset1v2choice == [1, 3, 4, 2]:
        jugarfunction()
        caminarfunction()
        nadarfunction()
        correrfunction()
    elif spanishvocabset1v2choice == [1, 4, 2, 3]:
        jugarfunction()
        nadarfunction()
        correrfunction()
        caminarfunction()
    elif spanishvocabset1v2choice == [1, 4, 3, 2]:
        jugarfunction()
        nadarfunction()
        caminarfunction()
        correrfunction()
    elif spanishvocabset1v2choice == [2, 1, 3, 4]:
        correrfunction()
        jugarfunction()
        caminarfunction()
        nadarfunction()
    elif spanishvocabset1v2choice == [2, 1, 4, 3]:
        correrfunction()
        jugarfunction()
        nadarfunction()
        caminarfunction()
    elif spanishvocabset1v2choice == [2, 3, 1, 4]:
        correrfunction()
        caminarfunction()
        jugarfunction()
        nadarfunction()
    elif spanishvocabset1v2choice == [2, 3, 4, 1]:
        correrfunction()
        caminarfunction()
        nadarfunction()
        jugarfunction()
    elif spanishvocabset1v2choice == [2, 4, 1, 3]:
        correrfunction()
        nadarfunction()
        jugarfunction()
        caminarfunction()
    elif spanishvocabset1v2choice == [2, 4, 3, 1]:
        correrfunction()
        nadarfunction()
        caminarfunction()
        jugarfunction()
    elif spanishvocabset1v2choice == [3, 1, 2, 4]:
        caminarfunction()
        jugarfunction()
        correrfunction()
        nadarfunction()
    elif spanishvocabset1v2choice == [3, 1, 4, 2]:
        caminarfunction()
        jugarfunction()
        nadarfunction()
        correrfunction()
    elif spanishvocabset1v2choice == [3, 2, 1, 4]:
        caminarfunction()
        correrfunction()
        jugarfunction()
        nadarfunction()
    elif spanishvocabset1v2choice == [3, 2, 4, 1]:
        caminarfunction()
        correrfunction()
        nadarfunction()
        jugarfunction()
    elif spanishvocabset1v2choice == [3, 4, 1, 2]:
        caminarfunction()
        nadarfunction()
        jugarfunction()
        correrfunction()
    elif spanishvocabset1v2choice == [3, 4, 2, 1]:
        caminarfunction()
        nadarfunction()
        correrfunction()
        jugarfunction()
    elif spanishvocabset1v2choice == [4, 1, 2, 3]:
        nadarfunction()
        jugarfunction()
        correrfunction()
        caminarfunction()
    elif spanishvocabset1v2choice == [4, 1, 3, 2]:
        nadarfunction()
        jugarfunction()
        caminarfunction()
        correrfunction()
    elif spanishvocabset1v2choice == [4, 2, 1, 3]:
        nadarfunction()
        correrfunction()
        jugarfunction()
        caminarfunction()
    elif spanishvocabset1v2choice == [4, 2, 3, 1]:
        nadarfunction()
        correrfunction()
        caminarfunction()
        jugarfunction()
    elif spanishvocabset1v2choice == [4, 3, 1, 2]:
        nadarfunction()
        caminarfunction()
        jugarfunction()
        correrfunction()
    elif spanishvocabset1v2choice == [4, 3, 2, 1]:
        nadarfunction()
        caminarfunction()
        correrfunction()
        jugarfunction()
    else:
        print(imsorry)
        mainmenu()
    print('good job! you complated Vocab Set 1!')
    input(' ')
    clearscreen()
    spanishvocabmenu()

def estarfunction():
    print('''
    What does Estar mean?
    ''')
    estarfunctionchoice = input('   ').lower()

    if estarfunctionchoice == 'to be':
        print('''
    Good job!

    Estar means to be!''')
        input(' ')
        clearscreen()
    elif estarfunctionchoice == 'exit' or estarfunctionchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        estarfunction()

def tenerfunction():
    print('''
    What does Tener mean?
    ''')
    tenerfunctionchoice = input('   ').lower()

    if tenerfunctionchoice == 'to have':
        print('''
    Good job!

    Tener means to have!''')
        input(' ')
        clearscreen()
    elif tenerfunctionchoice == 'exit' or tenerfunctionchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        tenerfunction()

def irfunction():
    print('''
    What does Ir mean?
    ''')
    irfunctionchoice = input('   ').lower()

    if irfunctionchoice == 'to go':
        print('''
    Good job!

    Ir means to go!''')
        input(' ')
        clearscreen()
    elif irfunctionchoice == 'exit' or irfunctionchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        irfunction()

def saberfunction():
    print('''
    What does Saber mean?
    ''')
    saberfunctionchoice = input('   ').lower()

    if saberfunctionchoice == 'to know':
        print('''
    Good job!

    Saber means to know!''')
        input(' ')
        clearscreen()
    elif saberfunctionchoice == 'exit' or saberfunctionchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        saberfunction()


def spanishvocabset2():
    spanishvocablist2 = [1, 2, 3, 4]
    spanishvocabset2choice = random.sample(spanishvocablist2, 4)
    if spanishvocabset2choice == [1, 2, 3, 4]:
        estarfunction()
        tenerfunction()
        irfunction()
        saberfunction()
    elif spanishvocabset2choice == [1, 2, 4, 3]:
        estarfunction()
        tenerfunction()
        saberfunction()
        irfunction()
    elif spanishvocabset2choice == [1, 3, 2, 4]:
        estarfunction()
        irfunction()
        tenerfunction()
        saberfunction()
    elif spanishvocabset2choice == [1, 3, 4, 2]:
        estarfunction()
        irfunction()
        saberfunction()
        tenerfunction()
    elif spanishvocabset2choice == [1, 4, 2, 3]:
        estarfunction()
        tenerfunction()
        saberfunction()
        irfunction()
    elif spanishvocabset2choice == [1, 4, 3, 2]:
        estarfunction()
        saberfunction()
        tenerfunction()
        irfunction()
    elif spanishvocabset2choice == [2, 1, 3, 4]:
        tenerfunction()
        estarfunction()
        irfunction()
        saberfunction()
    elif spanishvocabset2choice == [2, 1, 4, 3]:
        tenerfunction()
        estarfunction()
        saberfunction()
        irfunction()
    elif spanishvocabset2choice == [2, 3, 1, 4]:
        tenerfunction()
        irfunction()
        saberfunction()
        estarfunction()
    elif spanishvocabset2choice == [2, 3, 4, 1]:
        tenerfunction()
        irfunction()
        saberfunction()
        estarfunction()
    elif spanishvocabset2choice == [2, 4, 1, 3]:
        tenerfunction()
        saberfunction()
        estarfunction()
        irfunction()
    elif spanishvocabset2choice == [2, 4, 3, 1]:
        tenerfunction()
        saberfunction()
        irfunction()
        estarfunction()
    elif spanishvocabset2choice == [3, 1, 2, 4]:
        irfunction()
        estarfunction()
        tenerfunction()
        saberfunction()
    elif spanishvocabset2choice == [3, 1, 4, 2]:
        irfunction()
        estarfunction()
        saberfunction()
        tenerfunction()
    elif spanishvocabset2choice == [3, 2, 1, 4]:
        irfunction()
        tenerfunction()
        estarfunction()
        saberfunction()
    elif spanishvocabset2choice == [3, 2, 4, 1]:
        irfunction()
        tenerfunction()
        saberfunction()
        estarfunction()
    elif spanishvocabset2choice == [3, 4, 1, 2]:
        irfunction()
        saberfunction()
        estarfunction()
        tenerfunction()
    elif spanishvocabset2choice == [3, 4, 2, 1]:
        irfunction()
        saberfunction()
        tenerfunction()
        estarfunction()
    elif spanishvocabset2choice == [4, 1, 2, 3]:
        saberfunction()
        estarfunction()
        tenerfunction()
        irfunction()
    elif spanishvocabset2choice == [4, 1, 3, 2]:
        saberfunction()
        estarfunction()
        irfunction()
        tenerfunction()
    elif spanishvocabset2choice == [4, 2, 1, 3]:
        saberfunction()
        tenerfunction()
        estarfunction()
        irfunction()
    elif spanishvocabset2choice == [4, 2, 3, 1]:
        saberfunction()
        tenerfunction()
        irfunction()
        estarfunction()
    elif spanishvocabset2choice == [4, 3, 1, 2]:
        saberfunction()
        irfunction()
        estarfunction()
        tenerfunction()
    elif spanishvocabset2choice == [4, 3, 2, 1]:
        saberfunction()
        irfunction()
        tenerfunction()
        estarfunction()
    else:
        print(imsorry)
        mainmenu()
    print('good job! you completed Vocab Set 2!')
    input(' ')
    clearscreen()
    spanishvocabmenu()







mainmenu()
