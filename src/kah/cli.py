import argparse
from kah.db.utils import count, top

def hello_msg():
    return "hello"


def cmd():
    msg = hello_msg()
    # print(msg)

    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    parser.add_argument('-s', '--scount')
    parser.add_argument('-t', '--top', type=int)      
    parser.add_argument('-d', '--dt')

    args = parser.parse_args()
    # print(args.scount, args.top, args.dt)

    if args.scount:
        print(count(args.scount))
    elif args.top:
        if args.dt:
            print(top(args.top, args.dt))
        else:
            parser.error("utilize -t option with the -d option")
    else:
        parser.print_help()

