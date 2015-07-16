__author__ = 'spotapov'
import webbrowser
import time

count = 0

print("The program started on " +time.ctime())
while count < 3:
    time.sleep(1
    )
    webbrowser.open("http://google.com")
    count = count + 1
    print("Break #" +str(count) +" started on " + time.ctime())

else:
    print("Bye")
