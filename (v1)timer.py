import time

def start_timer():
    print("\n" + "=" * 40)
    print("Timer started! FOcus on ur study, GOOD LUCK!")
    print("=" * 40)
    time.sleep(time_total)

    print("\n" + "=" * 40)
    print(f"Times up and good job!, im very proud of u!🔥🔥")
    print("=" * 40)

print("=" * 40)
print("           Study Time Program")
print("=" * 40)

while True:
    timee = input(f"How long u going to study today, in hours or minutes (H/M)?: ").strip().upper()

    if timee == "H":
        try:
            time_seconds = int(input(f"How many hours u want to study today?: "))
            time_total = time_seconds * 3600
            break
        except ValueError:
            print("Invalid input! please enter a number for hours")
    elif timee == "M":
        try:
            time_seconds = int(input(f"How many minutes u want to study today?: "))
            time_total = time_seconds * 60
            break
        except ValueError:
            print("Invalid input! please enter a number for minutes")
    else:
        print(f"{timee} is invalid, please enter(H/M).")

print("=" * 40)

while True:
    startt = input("u wanna start now?(Y/N): ").upper()
    if startt == "Y":
        start_timer()
        break
    elif startt == "N":
        print("Ok take ur time")
        break
    else:
        print("invalid input")