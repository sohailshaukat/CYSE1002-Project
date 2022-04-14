import winsound
import time
import os


def sound():
    print("⏰⏰TIMES UP!!! Press ctrl+C to dismiss alarm⏰⏰")
    try:
        while True:
            winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
    except KeyboardInterrupt:
        print("ALARM WAS STOPPED!🔨🔨")
        return


def alarm(n):
    print()
    print('⌚Wait time: ', n, ' seconds.')
    try :
        time.sleep(n)
    except KeyboardInterrupt:
        print("OPERATION WAS STOPPED. EXITING ALARM👋👋")
    else:
        sound()


def main():
    print('What unit of time do you want to wait? \n 1. Hours \n 2. Minutes \n 3. Seconds \n 4. Combination \n 5. Pomdoro')
    main_input = input(":")
    input_destination(main_input)


def input_destination(user_input):
    if user_input == '1':
        user_input = int(input('⏱️Enter the desired hours: '))
        wait_time = (user_input * 60) * 60
        alarm(wait_time)
    elif user_input == '2':
        user_input = int(input('⏱️Enter the desired minutes: '))
        wait_time = user_input * 60
        alarm(wait_time)
    elif user_input == '3':
        user_input = int(input('⏱️Enter the desired seconds: '))
        wait_time = user_input
        alarm(wait_time)
    elif user_input == '4':
        hours = int(input('⏱️Hours: '))
        minutes = int(input('⏱️Minutes: '))
        seconds = int(input('⏱️Seconds: '))
        wait_time = ((hours * 60) * 60) + (minutes * 60) + seconds
        print(wait_time)
        alarm(wait_time)
    elif user_input == '5':
        print('⏰⏰WELCOME TO POMDORO TIMER⏰⏰')
        #Below two are floats because we would like to have decimal input for mins so that way if someone wants to set a timer for 6 seconds, they can pass 0.1 mins as input
        productive_time = float(input("⏱️Enter Productive Time in Mins: "))
        break_time = float(input("⏱️Enter Break Time in Mins: "))
        while True:
            print('💻💻TIME TO WORK!!!💻💻')
            alarm(productive_time*60)
            print('🎊🎊TIME FOR BREAK!!!🎊🎊')
            alarm(break_time*60)
            choice = input('✅Do you want to repeat? [y/n]')
            if choice.lower() == 'n':
                print('EXITING. BYE BYE 👋👋')
                break
            else:
                print('⏰⏰REPEATING POMDORO TIMER⏰⏰')
    else:
        try:
            os.system('cls')
            main()
        except:
            os.system('clear')
            main()


main()
