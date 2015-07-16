__author__ = 'spotapov'
def read_test():
    file = open("C:/Users/SPotapov/PycharmProjects/untitled1/check_profanity.txt")
    text = file.read()
    print(text)
    file.close()
read_test()