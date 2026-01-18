
#Threadings:
'''
- Threading means doing multiple tasks at same time with a single programm.
- It is used to increase application performance.
- It execute programm parallely.
- Threads are created multiple levels ,thread can create another thread that thread can create more threads.

# Two Types:
Multilevel Thread:Programm Automatically waits until threads finish.
Multithread: programme manually stop the main program until threads finish.
'''
#Mutlilevel Threading:

import _thread
import time
def play_music():
    for i in range(2):
        print('Playing Music')
        time.sleep(1)
def showLyrics():
    for j in range(2):
        print('show lyrics')
        time.sleep(1)
_thread.start_new_thread(play_music,())
_thread.start_new_thread(showLyrics,())

import time
import _thread
def Video_call():
    for i in range(2):
        print("On_Call")
        time.sleep(1)
def Video_Sending():
    for i in range(2):
        print("Video Sending")
        time.sleep(1)
def Audio_Sending():
    for i in range(2):
        print('Audio Sending')
        time.sleep(1)
_thread.start_new_thread(Video_call,())
_thread.start_new_thread(Video_Sending,())
_thread.start_new_thread(Audio_Sending,())

#MutliThread:

import threading
import time
def payment(utr):
    print(f'Payment Processing-{utr}')
    time.sleep(2)
    print(f'Payment Done {utr}')
    
def sms(utr):
    print(f'Sms Sent...{utr}')
    time.sleep(2)
    print(f'Sms Sent Completed {utr}')
    
t1 = threading.Thread(target=payment,args=(261572,))
t2= threading.Thread(target=sms,args=(26157237,))
t1.start()
t2.start()
t1.join()
t2.join()


import threading
import time
def Cash_withdraw(amount):
    print(f'withdraw processing:{amount}')
    time.sleep(2)
    print(f'Withdraw_completed....')
    
def Sms(amount):
    print(f'Send Sms....')
    time.sleep(2)
    print(f'Sms_completed....')
t1 = threading.Thread(target=Cash_withdraw,args=(2000,))
t2 = threading.Thread(target=Sms,args=(3000,))
t1.start()
t2.start()
t1.join()
t2.join()



#multilevel thread:

import _thread
import time
def salary_credit():
    for i in range(3):
        print('Salary Credited Successfully....   ')
        time.sleep(2)
def Send_sms():
    for i in range(3):
        print('Sms sending Successufully....    ')
        time.sleep(2)
_thread.start_new_thread(salary_credit,())
_thread.start_new_thread(Send_sms,())

#Multi Thread:

import threading
import time
def salary_credit():
    print(f'Salary Credited Successfully.... ')
    time.sleep(2)
    print(f'Salaray Credited to Emoployee Account.... ')
def Send_sms():
    print(f'Send sms Successufully')
    time.sleep(2)
    print(f'Sms send to the employee.....')
t1 = threading.Thread(target=salary_credit,args=())
t2 = threading.Thread(target=Send_sms,args=())
t1.start()
t2.start()
t1.join()
t2.join()

