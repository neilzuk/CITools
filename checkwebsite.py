# Simple script for checking if a website returns an expected response code
# checkwebsite.py https://example.com 200

import requests
import sys


def getwebsitestatus(url):
    r = requests.get(url)
    return r.status_code


def checkargv():
    if len(sys.argv) < 3:
        print("Incorrect number of args")
        return False
    elif not str.isdigit(sys.argv[2]):
        print("Expected status code must be a number")
        return False

    return True


def main():
    if checkargv():

        url = sys.argv[1]
        expectedstatus = int(sys.argv[2])
        actualstatus = getwebsitestatus(url)

        if expectedstatus == actualstatus:
            print("{0} returned the expected {1}".format(url, actualstatus))
            sys.exit(0)
        else:
            print("{0} returned {1} instead of the expected {2}".format(url, actualstatus, expectedstatus))
            sys.exit(1)

    else:
        print("Correct usage: python checkwebsite.py https://example.com 200")
        sys.exit(1)

if __name__ == '__main__':
    main()
