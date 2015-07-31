__author__ = 'spotapov'
import urllib
def read_test():
    open_file = open("C:/Users/SPotapov/PycharmProjects/untitled1/check_profanity.txt")
    text = open_file.read()
    print(text)
    open_file.close()
    check_profanity(text)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    out = connection.read()
    print(out)
read_test()