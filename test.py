import sys
import datetime

time = datetime.datetime.now()


def main():
    output = {}
    output["first"] = 'Hi {}, the current time is {}'.format(sys.argv[1], time)
    output["second"] = '/I/hope/this/works'
    return output


if __name__ == "__main__":
    print(main())
