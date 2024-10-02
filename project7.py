from time import *
import random as r
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error+1
        except :
            error = error+1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay,2)
    speed = len(userinput)/time_r
    return round(speed)

test = ["by the terms of this alliance indian rulers were not allowed to keep their independent armed forces they were to be protected by the company soldiers but they had to pay for the subsidary alliance"
,"the company were to maintain their soldiers for the purpose of protection",
"if the indian rulers failed to pay the company a part of their territory would be taken by the britishers",
"the nawabs of awadh were forced to give over half of their territories to britishers",
"hydrabads and alwars were also forced to give their territories on similar grounds"]
test1=r.choice(test)
print ("|||- TYPING SPEED -|||")
print(test1)
print()
time_1 = time()
test_input = input("enter : ")
time_2 = time()

print ("speed : ", speed_time(time_1,time_2,test_input),"word/second")
print ("error : ", mistake(test1,test_input))