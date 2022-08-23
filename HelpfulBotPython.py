import os
import random
from Chess.images import ChessMain3 as chess
from os import startfile
import TicTacToePygame2
import cv2
import numpy as np
import pandas as pd
import time
import webbrowser
import string
from random import randint


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
    elif mainmenuchoice == 'toolbox' or mainmenuchoice == '3':
        clearscreen()
        toolboxmenu()
    elif mainmenuchoice == 'personal notes' or mainmenuchoice == '4':
        print('Sorry this is section is only for me')
        mainmenu()
    elif mainmenuchoice == 'exit' or mainmenuchoice == '6':
        print('Goodbye')
        quit()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        mainmenu()


# Where I stored my variables

imsorry = "I'm sorry I didn't understand that"
imsorrywrong = "I'm sorry that isn't the correct answer"
underconstruction = "I'm sorry this page is still under construction"
chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Where I am registering webbrowser

webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))


# notes menu
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
        spanishsentencemenu()
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


def spanishsentencemenu():
    print('''
    
    Spanish Sentence Menu
    1. Sentence set 1
    2. Sentence set 2
    3. Exit
    
    
    ''')

    spanishsentencemunuchoice = input(' ').lower()

    if spanishsentencemunuchoice == 'sentence set 1' or spanishsentencemunuchoice == '1':
        clearscreen()
        spanishsentenceset1()
    elif spanishsentencemunuchoice == 'sentence set 2' or spanishsentencemunuchoice == '2':
        print(imsorry)
        clearscreen()
        spanishsentencemenu()
    elif spanishsentencemunuchoice == 'exit' or spanishsentencemunuchoice == '3':
        clearscreen()
        spanishmenu()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        spanishsentencemunu()


def spanishsentenceset1():
    spanishsentencelist1 = [1, 2, 3, 4]
    spanishsentencechoice1 = random.sample(spanishsentencelist1, 4)
    if spanishsentencechoice1 == [1, 2, 3, 4]:
        spanishsentence1()
        spanishsentence2()
        spanishsentence3()
        spanishsentence4()
    elif spanishsentencechoice1 == [1, 2, 4, 3]:
        spanishsentence1()
        spanishsentence2()
        spanishsentence4()
        spanishsentence3()
    elif spanishsentencechoice1 == [1, 3, 2, 4]:
        spanishsentence1()
        spanishsentence3()
        spanishsentence2()
        spanishsentence4()
    elif spanishsentencechoice1 == [1, 3, 4, 2]:
        spanishsentence1()
        spanishsentence3()
        spanishsentence4()
        spanishsentence2()
    elif spanishsentencechoice1 == [1, 4, 2, 3]:
        spanishsentence1()
        spanishsentence4()
        spanishsentence2()
        spanishsentence3()
    elif spanishsentencechoice1 == [1, 4, 3, 2]:
        spanishsentence1()
        spanishsentence4()
        spanishsentence3()
        spanishsentence2()
    elif spanishsentencechoice1 == [2, 1, 3, 4]:
        spanishsentence2()
        spanishsentence1()
        spanishsentence3()
        spanishsentence4()
    elif spanishsentencechoice1 == [2, 1, 4, 3]:
        spanishsentence2()
        spanishsentence1()
        spanishsentence4()
        spanishsentence3()
    elif spanishsentencechoice1 == [2, 3, 1, 4]:
        spanishsentence2()
        spanishsentence3()
        spanishsentence1()
        spanishsentence4()
    elif spanishsentencechoice1 == [2, 3, 4, 1]:
        spanishsentence2()
        spanishsentence3()
        spanishsentence4()
        spanishsentence1()
    elif spanishsentencechoice1 == [2, 4, 1, 3]:
        spanishsentence2()
        spanishsentence4()
        spanishsentence1()
        spanishsentence3()
    elif spanishsentencechoice1 == [2, 4, 3, 1]:
        spanishsentence2()
        spanishsentence4()
        spanishsentence3()
        spanishsentence1()
    elif spanishsentencechoice1 == [3, 1, 2, 4]:
        spanishsentence3()
        spanishsentence1()
        spanishsentence2()
        spanishsentence4()
    elif spanishsentencechoice1 == [3, 1, 4, 2]:
        spanishsentence3()
        spanishsentence1()
        spanishsentence4()
        spanishsentence2()
    elif spanishsentencechoice1 == [3, 2, 1, 4]:
        spanishsentence3()
        spanishsentence2()
        spanishsentence1()
        spanishsentence4()
    elif spanishsentencechoice1 == [3, 2, 4, 1]:
        spanishsentence3()
        spanishsentence2()
        spanishsentence4()
        spanishsentence1()
    elif spanishsentencechoice1 == [3, 4, 1, 2]:
        spanishsentence3()
        spanishsentence4()
        spanishsentence1()
        spanishsentence2()
    elif spanishsentencechoice1 == [3, 4, 2, 1]:
        spanishsentence3()
        spanishsentence4()
        spanishsentence2()
        spanishsentence1()
    elif spanishsentencechoice1 == [4, 1, 2, 3]:
        spanishsentence4()
        spanishsentence1()
        spanishsentence2()
        spanishsentence3()
    elif spanishsentencechoice1 == [4, 1, 3, 2]:
        spanishsentence4()
        spanishsentence1()
        spanishsentence3()
        spanishsentence2()
    elif spanishsentencechoice1 == [4, 2, 1, 3]:
        spanishsentence4()
        spanishsentence2()
        spanishsentence1()
        spanishsentence3()
    elif spanishsentencechoice1 == [4, 2, 3, 1]:
        spanishsentence4()
        spanishsentence2()
        spanishsentence3()
        spanishsentence1()
    elif spanishsentencechoice1 == [4, 3, 1, 2]:
        spanishsentence4()
        spanishsentence3()
        spanishsentence1()
        spanishsentence2()
    elif spanishsentencechoice1 == [4, 3, 2, 1]:
        spanishsentence4()
        spanishsentence3()
        spanishsentence2()
        spanishsentence1()
    else:
        print(imsorry)
        mainmenu()
    print('good job! you completed Sentence Set 1!')
    input(' ')
    clearscreen()
    spanishsentencemenu()


def spanishsentence1():
    print('''
    Translate the sentence
    
    Quisiera unas papas fritas.
    ''')
    spanishsentence1choice = input('   ').lower()

    if spanishsentence1choice == 'i would like some french fries' or \
            spanishsentence1choice == 'i would like french fries':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishsentence1choice == 'exit' or spanishsentence1choice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishsentencemenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsentence1()


def spanishsentence2():
    print('''
    Translate the sentence

    El cafe esta listo.
    ''')
    spanishsentence2choice = input('   ').lower()

    if spanishsentence2choice == 'the coffee is ready':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishsentence2choice == 'exit' or spanishsentence2choice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishsentencemenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsentence2()


def spanishsentence3():
    print('''
    Translate the sentence

    La leche esta en la heladera.
    ''')
    spanishsentence3choice = input('   ').lower()

    if spanishsentence3choice == 'the milk is in the fridge':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishsentence3choice == 'exit' or spanishsentence3choice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishsentencemenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsentence3()


def spanishsentence4():
    print('''
    Translate the sentence

    Tienen helado de chocolate y vainilla.
    ''')
    spanishsentence4choice = input('   ').lower()

    if spanishsentence4choice == 'they have chocolate and vanilla ice cream':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishsentence4choice == 'exit' or spanishsentence4choice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishsentencemenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsentence4()


# entertainment menu
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
    3. Tic Tac Toe
    4. Exit
    
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
    elif entertainmentgamesmenuchoice == 'chess' or entertainmentgamesmenuchoice == '3':
        if __name__ == '__main__':
            TicTacToePygame2.main()
            clearscreen()
            entertainmentgamesmenu()
    elif entertainmentgamesmenuchoice == 'exit' or entertainmentgamesmenuchoice == '4':
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


# toolbox menu
def toolboxmenu():
    print('''

    Welcome to the Toolbox Menu!
    What can I help you with?

    1. Password Generator
    2. Exit


    ''')

    toolboxmenuchoice = input(' ').lower()

    if toolboxmenuchoice == 'password generator' or toolboxmenuchoice == '1':
        passwordgenerator()
        passwordgeneratorloop()
    if toolboxmenuchoice == 'exit' or toolboxmenuchoice == '2':
        mainmenu()
    else:
        print(imsorry)
        toolboxmenu()


def passwordgeneratorloop():
    passwordgeneratoranswer = input('Would you like another password? Y/N ').lower()
    if passwordgeneratoranswer == 'y' or passwordgeneratoranswer == 'yes':
        passwordgenerator()
        passwordgeneratorloop()
    else:
        toolboxmenu()


# password generator
def passwordgenerator():
    text_file = open('textfiles\\usa.txt', 'r')
    file_content = text_file.read()
    content_list = file_content.split('\n')

    # user inputs length of password they would like
    length = None

    while length == None:
        try:
            length = int(input('\nPassword length: '))
        except:
            print('sorry that isnt a number')

    # variables
    num = string.digits
    symbols = string.punctuation

    random3 = randint(1, 3)
    random2 = randint(1, 2)
    number_of_numbers = random2
    number_of_words = random3
    randomnumbers = random.choices(num, k=number_of_numbers)
    randompuncutation = random.choices(symbols, k=number_of_numbers)
    temp2 = ''.join(randompuncutation) + ''.join(randomnumbers)
    temp3 = ''.join(random.sample(temp2, len(temp2)))

    content_list_sorted = sorted(content_list, key=len)

    oneletterword = []
    twoletterword = []
    threeletterword = []
    fourletterword = []
    fiveletterword = []
    sixletterword = []
    sevenletterword = []
    eightletterword = []
    nineletterword = []
    tenletterword = []
    elevenletterword = []
    twelveletterword = []
    thirteenletterword = []

    for i in content_list_sorted:
        if len(i) == 1:
            oneletterword.append(i)
        elif len(i) == 2:
            twoletterword.append(i)
        elif len(i) == 3:
            threeletterword.append(i)
        elif len(i) == 4:
            fourletterword.append(i)
        elif len(i) == 5:
            fiveletterword.append(i)
        elif len(i) == 6:
            sixletterword.append(i)
        elif len(i) == 7:
            sevenletterword.append(i)
        elif len(i) == 8:
            eightletterword.append(i)
        elif len(i) == 9:
            nineletterword.append(i)
        elif len(i) == 10:
            tenletterword.append(i)
        elif len(i) == 11:
            elevenletterword.append(i)
        elif len(i) == 12:
            twelveletterword.append(i)
        elif len(i) == 13:
            thirteenletterword.append(i)
        else:
            pass

    number_of_characters = length - len(temp3)

    if number_of_characters == 1:
        password = random.choice(oneletterword) + temp3
    elif number_of_characters == 2:
        password = random.choice(twoletterword) + temp3
    elif number_of_characters == 3:
        password = random.choice(threeletterword) + temp3
    elif number_of_characters == 4:
        password = random.choice(fourletterword) + temp3
    elif number_of_characters == 5:
        password = random.choice(fiveletterword) + temp3
    elif number_of_characters == 6:
        passcombo = randint(1, 4)
        if passcombo == 1:
            password = random.choice(sixletterword) + temp3
        if passcombo == 2:
            password = random.choice(threeletterword) + random.choice(threeletterword) + temp3
        if passcombo == 3:
            password = random.choice(fourletterword) + random.choice(twoletterword) + temp3
        if passcombo == 4:
            password = random.choice(twoletterword) + random.choice(fourletterword) + temp3
    elif number_of_characters == 7:
        passcombo = randint(1, 5)
        if passcombo == 1:
            password = random.choice(sevenletterword) + temp3
        if passcombo == 2:
            password = random.choice(threeletterword) + random.choice(fourletterword) + temp3
        if passcombo == 3:
            password = random.choice(fourletterword) + random.choice(threeletterword) + temp3
        if passcombo == 4:
            password = random.choice(twoletterword) + random.choice(fiveletterword) + temp3
        if passcombo == 5:
            password = random.choice(fiveletterword) + random.choice(twoletterword) + temp3
    elif number_of_characters == 8:
        passcombo = randint(1, 4)
        if passcombo == 1:
            password = random.choice(eightletterword) + temp3
        if passcombo == 2:
            password = random.choice(fourletterword) + random.choice(fourletterword) + temp3
        if passcombo == 3:
            password = random.choice(fiveletterword) + random.choice(threeletterword) + temp3
        if passcombo == 4:
            password = random.choice(threeletterword) + random.choice(fiveletterword) + temp3
    elif number_of_characters == 9:
        passcombo = randint(1, 6)
        if passcombo == 1:
            password = random.choice(nineletterword) + temp3
        elif passcombo == 2:
            password = random.choice(fourletterword) + random.choice(fiveletterword) + temp3
        elif passcombo == 3:
            password = random.choice(fiveletterword) + random.choice(fourletterword) + temp3
        elif passcombo == 4:
            password = random.choice(threeletterword) + random.choice(threeletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 5:
            password = random.choice(sixletterword) + random.choice(threeletterword) + temp3
        elif passcombo == 6:
            password = random.choice(threeletterword) + random.choice(sixletterword) + temp3
    elif number_of_characters == 10:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + temp3
        elif passcombo == 2:
            password = random.choice(fiveletterword) + random.choice(fiveletterword) + temp3
        elif passcombo == 3:
            password = random.choice(sixletterword) + random.choice(fourletterword) + temp3
        elif passcombo == 4:
            password = random.choice(fourletterword) + random.choice(sixletterword) + temp3
        elif passcombo == 5:
            password = random.choice(fourletterword) + random.choice(threeletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 6:
            password = random.choice(threeletterword) + random.choice(fourletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 7:
            password = random.choice(threeletterword) + random.choice(threeletterword) \
                       + random.choice(fourletterword) + temp3
        elif passcombo == 8:
            password = random.choice(fiveletterword) + random.choice(threeletterword) \
                       + random.choice(twoletterword) + temp3
        elif passcombo == 9:
            password = random.choice(threeletterword) + random.choice(twoletterword) \
                       + random.choice(fiveletterword) + temp3
        elif passcombo == 10:
            password = random.choice(twoletterword) + random.choice(fiveletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 11:
            password = random.choice(threeletterword) + random.choice(fiveletterword) \
                       + random.choice(twoletterword) + temp3
        elif passcombo == 12:
            password = random.choice(fiveletterword) + random.choice(twoletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 13:
            password = random.choice(fourletterword) + random.choice(fourletterword) \
                       + random.choice(twoletterword) + temp3
        elif passcombo == 14:
            password = random.choice(fourletterword) + random.choice(twoletterword) \
                       + random.choice(fourletterword) + temp3
        elif passcombo == 15:
            password = random.choice(twoletterword) + random.choice(fourletterword) \
                       + random.choice(fourletterword) + temp3
    elif number_of_characters == 11:
        passcombo = randint(1, 8)
        if passcombo == 1:
            password = random.choice(elevenletterword) + temp3
        elif passcombo == 2:
            password = random.choice(sixletterword) + random.choice(fiveletterword) + temp3
        elif passcombo == 3:
            password = random.choice(fiveletterword) + random.choice(sixletterword) + temp3
        elif passcombo == 4:
            password = random.choice(sevenletterword) + random.choice(fourletterword) + temp3
        elif passcombo == 5:
            password = random.choice(fourletterword) + random.choice(fiveletterword) \
                       + random.choice(twoletterword) + temp3
        elif passcombo == 6:
            password = random.choice(fiveletterword) + random.choice(fourletterword) \
                       + random.choice(twoletterword) + temp3
        elif passcombo == 7:
            password = random.choice(sixletterword) + random.choice(threeletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 8:
            password = random.choice(sixletterword) + random.choice(threeletterword) \
                       + random.choice(threeletterword) + temp3
    elif number_of_characters == 12:
        passcombo = randint(1, 10)
        if passcombo == 1:
            password = random.choice(twelveletterword) + temp3
        elif passcombo == 2:
            password = random.choice(sixletterword) + random.choice(sixletterword) + temp3
        elif passcombo == 3:
            password = random.choice(sevenletterword) + random.choice(fiveletterword) + temp3
        elif passcombo == 4:
            password = random.choice(fiveletterword) + random.choice(sevenletterword) + temp3
        elif passcombo == 5:
            password = random.choice(eightletterword) + random.choice(fourletterword) + temp3
        elif passcombo == 6:
            password = random.choice(fourletterword) + random.choice(eightletterword) + temp3
        elif passcombo == 7:
            password = random.choice(threeletterword) + random.choice(threeletterword) \
                       + random.choice(sixletterword) + temp3
        elif passcombo == 8:
            password = random.choice(threeletterword) + random.choice(sixletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 9:
            password = random.choice(sixletterword) + random.choice(threeletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 10:
            password = random.choice(fourletterword) + random.choice(fourletterword) \
                       + random.choice(fourletterword) + temp3
    elif number_of_characters == 13:
        passcombo = randint(1, 12)
        if passcombo == 1:
            password = random.choice(thirteenletterword) + temp3
        elif passcombo == 2:
            password = random.choice(sevenletterword) + random.choice(sixletterword) + temp3
        elif passcombo == 3:
            password = random.choice(sixletterword) + random.choice(sevenletterword) + temp3
        else:
            password = random.choice(eightletterword) + random.choice(fiveletterword) + temp3
    elif number_of_characters == 14:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(fourletterword) + random.choice(tenletterword) + temp3
        elif passcombo == 2:
            password = random.choice(fiveletterword) + random.choice(nineletterword) + temp3
        elif passcombo == 3:
            password = random.choice(sixletterword) + random.choice(eightletterword) + temp3
        elif passcombo == 4:
            password = random.choice(sevenletterword) + random.choice(sevenletterword) + temp3
        elif passcombo == 5:
            password = random.choice(eightletterword) + random.choice(sixletterword) + temp3
        elif passcombo == 6:
            password = random.choice(sixletterword) + random.choice(eightletterword) + temp3
        elif passcombo == 7:
            password = random.choice(tenletterword) + random.choice(fourletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(fiveletterword) + temp3
    elif number_of_characters == 15:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(fiveletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(sixletterword) + temp3
    elif number_of_characters == 16:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(elevenletterword) + random.choice(fiveletterword) + temp3
        else:
            password = random.choice(tenletterword) + random.choice(sixletterword) + temp3
    elif number_of_characters == 17:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(twelveletterword) + random.choice(fiveletterword) + temp3
        else:
            password = random.choice(elevenletterword) + random.choice(sixletterword) + temp3
    elif number_of_characters == 18:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(twelveletterword) + random.choice(sixletterword) + temp3
        else:
            password = random.choice(elevenletterword) + random.choice(sevenletterword) + temp3
    elif number_of_characters == 19:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(twelveletterword) + random.choice(sevenletterword) + temp3
        else:
            password = random.choice(elevenletterword) + random.choice(eightletterword) + temp3
    elif number_of_characters == 20:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(twelveletterword) + random.choice(eightletterword) + temp3
        else:
            password = random.choice(elevenletterword) + random.choice(nineletterword) + temp3
    elif number_of_characters == 21:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(twelveletterword) + random.choice(nineletterword) + temp3
        else:
            password = random.choice(elevenletterword) + random.choice(tenletterword) + temp3
    elif number_of_characters == 22:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(twelveletterword) + random.choice(tenletterword) + temp3
        else:
            password = random.choice(elevenletterword) + random.choice(elevenletterword) + temp3
    elif number_of_characters == 23:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(fiveletterword) \
                       + random.choice(eightletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(fiveletterword) \
                       + random.choice(nineletterword) + temp3
    elif number_of_characters == 24:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(fiveletterword) \
                       + random.choice(nineletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(fiveletterword) \
                       + random.choice(tenletterword) + temp3
    elif number_of_characters == 25:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(sixletterword) \
                       + random.choice(nineletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(tenletterword) \
                       + random.choice(sixletterword) + temp3
    elif number_of_characters == 26:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(sevenletterword) \
                       + random.choice(nineletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(tenletterword) \
                       + random.choice(sevenletterword) + temp3
    elif number_of_characters == 27:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(eightletterword) \
                       + random.choice(nineletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(tenletterword) \
                       + random.choice(eightletterword) + temp3
    elif number_of_characters == 28:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(nineletterword) \
                       + random.choice(nineletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(tenletterword) \
                       + random.choice(nineletterword) + temp3
    elif number_of_characters == 29:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(nineletterword) \
                       + random.choice(tenletterword) + temp3
        else:
            password = random.choice(tenletterword) + random.choice(tenletterword) \
                       + random.choice(nineletterword) + temp3
    elif number_of_characters == 30:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(fiveletterword) \
                       + random.choice(tenletterword) + random.choice(fiveletterword) + temp3
        else:
            password = random.choice(tenletterword) + random.choice(tenletterword) \
                       + random.choice(fiveletterword) + random.choice(fiveletterword) + temp3
    elif number_of_characters == 31:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(sixletterword) \
                       + random.choice(tenletterword) + random.choice(fiveletterword) + temp3
        else:
            password = random.choice(tenletterword) + random.choice(tenletterword) \
                       + random.choice(sixletterword) + random.choice(fiveletterword) + temp3
    elif number_of_characters == 32:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(sixletterword) \
                       + random.choice(tenletterword) + random.choice(sixletterword) + temp3
        else:
            password = random.choice(tenletterword) + random.choice(tenletterword) \
                       + random.choice(sixletterword) + random.choice(sixletterword) + temp3
    else:
        password = 'sorry we currently do not support that many characters at the moment'

    print(password)


# personal notes menu
def personalnotesmenu():
    clearscreen()
    print('''
    Sorry this is for my personal use only''')

mainmenu()
