import numpy as np
import time
from colorama import Fore, Style

totalFrames = int(input("\nEnter Number of frames: ")) #Input

data = [] #Data generation
for i in range(totalFrames):
    byte = ''.join(np.random.choice(["0", "1"]) for _ in range(8))
    data.append(byte)
print(Fore.BLUE + f"\nTransmit Data:{data}" + Style.RESET_ALL)

n = 0 #Frame Number
ack = 1 #Acknowlegment Number
seq = 0 #Seq numbering from 0

while seq < totalFrames:

    print(Fore.YELLOW + f"\nSENDER: Transmitting.... |(Frame{n}),(Seq{seq}),({data[seq]})|..... Timer Started"+ Style.RESET_ALL)
    
    control = np.random.choice([0, 1, 2, 3, 4, 5], p=[0.5, 0.3, 0.05, 0.05, 0.05, 0.05]) #case control

    if(control==0):  #Successful Transmission Case
        print(Fore.GREEN + f"RECIEVER: Received.... |(Frame{n}),(Seq{seq}),({data[seq]})|")
        print(f"SENDER's RECIEVER: |Ack{ack}|....  Delete copy of tx frame and slide window!"+ Style.RESET_ALL)
        seq += 1 #Sliding window by 1 frame
        n += 1
        ack += 1

    elif(control==1): #Frame Corrupted Case
        corrupt = ''.join(np.random.choice(["0", "1"]) for _ in range(8)) #Corruption
        checkSum = sum(list(map(int,data[seq]))) #sum of transmitted frame
        sumValue = sum(list(map(int,corrupt))) #sum of received frame
        print(Fore.MAGENTA + f"RECIEVER: Received.... |(Frame{n}),(Seq{seq}),({corrupt})|")
        print(f"Check Sum: {checkSum}, Sum of Corrupt frame: {sumValue}")
        if (checkSum != sumValue): #Checksum process
            print("RECIEVER: Received Corrupted Frame....  Discard frame!")
        else:
            print("RECIEVER: Checksum - False Positive....  Discard frame!")
        print(Fore.RED + f"SENDER's RECIEVER: Timeout!! |Ack{ack}| Not Received (Frame Corrupted)" + Style.RESET_ALL)

    elif(control==2): #Frame lost case
        print(Fore.RED + f"RECIEVER: Not Received.... |(Frame{n}),(Seq{seq}),({data[seq]})|")
        print(f"SENDER's RECIEVER: Timeout!! |Ack{ack}| Not Received (Frame lost)"+ Style.RESET_ALL)

    elif(control==3): #Frame delayed case
        print(Fore.RED + f"RECIEVER: Not Received.... |(Frame{n}),(Seq{seq}),({data[seq]})|")
        print(f"SENDER's RECIEVER: Timeout!! |Ack{ack}| Not Received (Frame delayed)" + Style.RESET_ALL)

    elif(control==4): #Acknowledgement case
        print(Fore.RED + f"RECIEVER: Received.... |(Frame{n}),(Seq{seq}),({data[seq]})|")
        print(f"SENDER's RECIEVER: Timeout!! |Ack{ack}| Not Received (Acknowledgement delayed)" + Style.RESET_ALL)

    elif(control==5): #Acknowledgement lost case
        print(Fore.RED + f"RECIEVER: Received.... |(Frame{n}),(Seq{seq}),({data[seq]})|")
        print(f"SENDER's RECIEVER: Timeout!! |Ack{ack}| Not Received (Acknoledgement lost))" + Style.RESET_ALL)

    if n > 1: #Modulo 2 arithmetic of frame numbering
        n = 0
    if ack > 1:
        ack = 0
    
    time.sleep(1)

time.sleep(1)
print(Fore.BLUE+"Congratulation!! Successfully transmitted all frames in the message.\n" + Style.RESET_ALL)
