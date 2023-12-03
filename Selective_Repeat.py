import numpy as np
import time
from colorama import Fore, Style

totalFrames = int(input("\nEnter total number of frames: "))
windowSize = int(input("Enter the Window Size: "))

next_seq_num = 0
base = 0

print("")
for i in range(base, min(base + windowSize, totalFrames)):
    print(Fore.YELLOW + f"SENDER: Transmitting.... |(Frame{i%(windowSize*2)}),(Seq{i})|" + Style.RESET_ALL)
    time.sleep(0.5)

window = list(range(base, min(base + windowSize, totalFrames)))

while base < totalFrames:
    print(Fore.CYAN + f"\nSENDER WINDOW: {window}\n"+ Style.RESET_ALL )
    
    control = np.random.choice([1, 0,-1], p=[0.5, 0.25, 0.25])

    if control == 1: #Successful Transmission
        print(Fore.GREEN + f"SENDER's RECIEVER: |ACK for frame {window[0]}|\n"+ Style.RESET_ALL)
        window.remove(window[0])
        base += 1
        next_seq_num = base + windowSize - 1
        if next_seq_num < totalFrames:
            print(Fore.YELLOW + f"SENDER: Transmitting.... |(Frame{next_seq_num%(windowSize*2)}),(Seq{next_seq_num})|" + Style.RESET_ALL)
            window.append(next_seq_num%(windowSize*2))

    elif control == 0: #Negative acknowledgement case
        print(Fore.RED +f"SENDER'S RECEIVER: |NAK{window[0]}|\n" + Style.RESET_ALL)
        window.append(window[0])
        print(Fore.YELLOW + f"SENDER: Transmitting.... |(Frame{window[0]%(windowSize*2)}),(Seq{window[0]})|" + Style.RESET_ALL)
        window.remove(window[0])

    elif control == -1: #Timeout Case
        print(Fore.RED + f"SENDER's RECEIVER: Timeout!! |ACK for frame {window[0]}| not received\n" + Style.RESET_ALL)
        window.append(window[0])
        print(Fore.YELLOW + f"SENDER: Transmitting.... |(Frame{window[0]%(windowSize*2)}),(Seq{window[0]})|" + Style.RESET_ALL)
        window.remove(window[0])
    
    time.sleep(0.5)

time.sleep(1)
print(Fore.BLUE+"Congratulation!! Successfully transmitted all frames in the message.\n" + Style.RESET_ALL)
