import argparse
from kah.db.utils import count, top
from tabulate import tabulate

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
        cnt = count(args.scount)
        print(f"The command '{args.scount}' was used {cnt} times")
        # print(count(args.scount))
    elif args.top:
        if args.dt:
            df = top(args.top, args.dt)
            # print(top(args.top, args.dt))

            header = df.columns.tolist()
            print(tabulate(df.values.tolist(), headers=header, tablefmt="outline"))
        else:
            parser.error("utilize -t option with the -d option")
    else:
        parser.print_help()

