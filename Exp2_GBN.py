import numpy as np
import time
from colorama import Fore, Style

totalFrames = int(input("\nEnter total number of frames: "))
windowSize = int(input("Enter the Window Size: "))

data = [] #Data generation
for i in range(totalFrames):
    byte = ''.join(np.random.choice(["0", "1"]) for _ in range(8))
    data.append(byte)
print(Fore.BLUE + f"\nTransmit Data:{data}\n" + Style.RESET_ALL)

seq = 0 # sequence index(0, totalframes)
ack = 0 # ack pointer - (seq+1) % windowSize 
f = 0 #  frame pointer - seq % windowSize
base = 0 # base value of the window
s = 0 # frame index inside the window

while seq < totalFrames:

    for i in range(base, min(base + windowSize, totalFrames)): # i - index of window (Window Definition)
        s = i % windowSize
        print(Fore.YELLOW + f"SENDER: Transmitting.... |(Frame{s}),(Seq{i}),({data[i]})|"+ Style.RESET_ALL)
        time.sleep(0.5)
    print(Fore.CYAN + "\nSENDER: Timer Started\n"+ Style.RESET_ALL) 

    ack = (seq+1) % windowSize
    f = seq % windowSize

    control = np.random.choice([0, 1, 2, 3, 4, 5], p=[0.5, 0.1, 0.1, 0.1, 0.1, 0.1]) #case control

    if control == 0: #Successful Transmission
        print(Fore.GREEN + f"RECIEVER: Received.... |(Frame{f}),(Seq{seq}),({data[seq]})|")
        print(f"RECEIVER: |Ack{ack}|")
        print(f"SENDER's RECIEVER: |Ack{ack}|....  Delete copy of tx frame and slide window!\n"+ Style.RESET_ALL)
        seq += 1
        base += 1

    elif(control==1): #Frame Corrupted Case
        corrupt = ''.join(np.random.choice(["0", "1"]) for _ in range(8)) #Corruption
        print(Fore.MAGENTA + f"RECIEVER: Received.... |(Frame{f}),(Seq{seq}),({corrupt})|")
        checkSum = sum(list(map(int,data[seq]))) #sum of transmitted frame
        sumValue = sum(list(map(int,corrupt))) #sum of received frame
        print(f"Check Sum: {checkSum}, Sum of Corrupt frame: {sumValue}")
        if (checkSum != sumValue): #Checksum process
            print("RECIEVER: Received Corrupted Frame....  Discard frame!")
        else:
            print("RECIEVER: Checksum - False Positive....  Discard frame!")
        print(Fore.RED + f"SENDER's RECIEVER: Timeout!! |Ack{ack}| Not Received (Frame Corrupted)\n" + Style.RESET_ALL)

    elif(control==2): #Frame lost case
        print(Fore.RED + f"RECIEVER: Not Received.... |(Frame{f}),(Seq{seq}),({data[seq]})|")
        print(f"SENDER's RECIEVER: Timeout!! |Ack{ack}| Not Received (Frame lost)\n"+ Style.RESET_ALL)

    elif(control==3): #Frame delayed case
        print(Fore.RED + f"RECIEVER: Not Received.... |(Frame{f}),(Seq{seq}),({data[seq]})|")
        print(f"SENDER's RECIEVER: Timeout!! |Ack{ack}| Not Received (Frame delayed)\n" + Style.RESET_ALL)

    elif(control==4): #Acknowledgement case
        print(Fore.RED + f"RECIEVER: Received.... |(Frame{f}),(Seq{seq}),({data[seq]})|")
        print(f"SENDER's RECIEVER: Timeout!! |Ack{ack}| Not Received (Acknowledgement lost)\n"+ Style.RESET_ALL)

    elif(control==5): #Acknowledgement lost case
        print(Fore.RED + f"RECIEVER: Received.... |(Frame{f}),(Seq{seq}),({data[seq]})|")
        print(f"SENDER's RECIEVER: Timeout!! |Ack{ack}| Not Received (Acknowledgement delayed)\n" + Style.RESET_ALL)
      

    time.sleep(1)

time.sleep(1)
print(Fore.BLUE+"Congratulation!! Successfully transmitted all frames in the message.\n" + Style.RESET_ALL)