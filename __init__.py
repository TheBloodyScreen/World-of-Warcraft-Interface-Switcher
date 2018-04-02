import os
import time
import shutil
from bloodyterminal import btext


# quality of life things
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def drawMainMenu():
    clear()
    btext.info('    Please choose your action')
    btext.info('1   set interface and wtf directorys')
    btext.info('2   set interface 1 active')
    btext.info('3   set interface 2 active')
    btext.info('4   restore backup')
    btext.info('5   quit')
    time.sleep(1)
    choice = input('choose a number: ')

    if choice == '1':
        clear()
        btext.info('please enter the path to your interface directory!')
        btext.info('0 to not change the current directory.')
        with open('./InterfaceSwitcher/dir.txt', 'r') as dirs:
            dirs = dirs.readlines()
        dirData = [dirs[0], dirs[1]]
        btext.info('the current directorys are: ')
        btext.info('interface: ' + dirs[0])
        btext.info('wtf: ' + dirs[1])

        interfaceDir = input('path to interface: ')
        if interfaceDir == '0':
            pass
        elif os.path.exists(interfaceDir):
            btext.success('input accepted!')
            dirData[0] = (interfaceDir + '\n')
        else:
            btext.warning('your input seems to be invalid, please try again')

        wtfDir = input('path to wtf: ')
        if wtfDir == '0':
            pass
        elif os.path.exists(wtfDir):
            btext.success('input accepted!')
            btext.info('returning to main menu...')
            dirData[1] = (wtfDir)
            time.sleep(3)
        else:
            btext.warning('your input seems to be invalid, please try again')
            btext.info('returning to main menu...')
            time.sleep(3)

        with open('./InterfaceSwitcher/dir.txt', 'w') as file:
            file.writelines(dirData)

        drawMainMenu()

    elif choice == '2':
        clear()
        btext.info('are you sure you want to set interface 1 as active?')

        if input('y/n: ') == 'y':
            clear()
            btext.info('deleting current interface...')
            time.sleep(1)
            with open('./InterfaceSwitcher/dir.txt', 'r') as dirs:
                dirs = dirs.readlines()

            try:
                os.rmdir(dirs[0][:-1])
                os.rmdir(dirs[1])
                btext.success('interface deleted!')
            except os.error as e:
                btext.debug('Directory not deleted. Error: %s' % e)
                btext.warning('failed to delete interface')
                btext.warning('please try again!')
                time.sleep(1)
                drawMainMenu()

            btext.info('copying interface 1...')
            time.sleep(3)

            try:
                shutil.copytree('./InterfaceSwitcher/interface_1/interface', dirs[0][:-1])
                shutil.copytree('./InterfaceSwitcher/interface_1/wtf', dirs[1])
                btext.success('interface copied!')
                time.sleep(1)
            except shutil.Error as e:
                btext.debug('Directory not copied. Error: %s' % e)
                btext.warning('failed to copy interface')
                btext.warning('please try again!')
                time.sleep(1)
                drawMainMenu()

            btext.success('new interface copied!')
            btext.info('returning to main menu...')
            time.sleep(1)

        drawMainMenu()

    elif choice == '3':
        clear()
        btext.info('are you sure you want to set interface 2 as active?')

        if input('y/n: ') == 'y':
            clear()
            btext.info('deleting current interface...')
            time.sleep(1)
            with open('./InterfaceSwitcher/dir.txt', 'r') as dirs:
                dirs = dirs.readlines()

            try:
                os.rmdir(dirs[0][:-1])
                os.rmdir(dirs[1])
                btext.success('interface deleted!')
            except os.error as e:
                btext.debug('Directory not deleted. Error: %s' % e)
                btext.warning('failed to delete interface')
                btext.warning('please try again!')
                time.sleep(1)
                drawMainMenu()

            btext.info('copying interface 1...')
            time.sleep(3)

            try:
                shutil.copytree('./InterfaceSwitcher/interface_2/interface', dirs[0][:-1])
                shutil.copytree('./InterfaceSwitcher/interface_2/wtf', dirs[1])
                btext.success('interface copied!')
                time.sleep(1)
            except shutil.Error as e:
                btext.debug('Directory not copied. Error: %s' % e)
                btext.warning('failed to copy interface')
                btext.warning('please try again!')
                time.sleep(1)
                drawMainMenu()

            btext.success('new interface copied!')
            btext.info('returning to main menu...')
            time.sleep(1)

        drawMainMenu()


btext.info('Welcome to InterfaceSwitcher!')
btext.info('checking for IS directory...')
ISdir = './InterfaceSwitcher'


if os.path.exists(ISdir):
    btext.success('directorys found!')
    time.sleep(1)
    drawMainMenu()
else:
    btext.info('no directorys found, creating...')
    try:
        os.makedirs('./InterfaceSwitcher')
        os.makedirs('./InterfaceSwitcher/interface_1')
        os.makedirs('./InterfaceSwitcher/interface_1/interface')
        os.makedirs('./InterfaceSwitcher/interface_1/WTF')
        os.makedirs('./InterfaceSwitcher/interface_2')
        os.makedirs('./InterfaceSwitcher/interface_2/interface')
        os.makedirs('./InterfaceSwitcher/interface_2/WTF')
        os.makedirs('./InterfaceSwitcher/interface_1_backup')
        os.makedirs('./InterfaceSwitcher/interface_1_backup/interface')
        os.makedirs('./InterfaceSwitcher/interface_1_backup/WTF')
        os.makedirs('./InterfaceSwitcher/interface_2_backup')
        os.makedirs('./InterfaceSwitcher/interface_2_backup/interface')
        os.makedirs('./InterfaceSwitcher/interface_2_backup/WTF')
        open('./InterfaceSwitcher/dir.txt', 'w')
        btext.success('directorys created!')
        time.sleep(1)
        drawMainMenu()
    except:
        btext.warning('failed to create directorys!')
        btext.warning('please try again!')
