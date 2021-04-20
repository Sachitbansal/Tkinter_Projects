import time

print("Timer")
x = int(input("Seconds: "))
time.sleep(1)
print("Warming: Program will terminate once the timer ends")
time.sleep(2)
print()
while x > 0:
    print(f"Time Remaining: {x} SECONDS")
    time.sleep(1)
    x = x - 1

if x == 0:
    print()
    print("The time is over!")
    quit()
