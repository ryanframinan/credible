import argparse
import sys
from modules import *
import re 
import os

# Need to program --path to be implemented.. too lazy right now

class Credible:

    def __init__(self):
        pass

    def validate_args(self):
        parser = argparse.ArgumentParser(description="")
        parser.add_argument("--proxy", metavar="<proxy>", dest="proxy", default=None, 
                            help="Proxy type: l = LinkedIn, m = MyFitnessPal, r = Random, a = all")
        parser.add_argument("--email", metavar="<email>", dest="email", default=None, 
                            help="Pass a single email to scan. TIP: Can scan for username.")
        parser.add_argument("--path", metavar="<path>", dest="path", default=None, help="Pass a file containing emails one per line to scan.")
        args = parser.parse_args()

        if not args.proxy:
            print("[-] Missing --proxy argument")
            exit(1)
        if not (args.email or args.path):
            print("[-] Missing --email or --path argument")
            exit(1)
        if args.path != None:
            if os.path.exists(args.path) == False:
                print("[-] " + args.path + " doesn't exist in directory")
                exit(1)
        
        # email coordination
        #if args.email is not None:
        #    to_search = [args.email]
        #elif arg.path is not None:
        #    with open(args.path) as emails:
        #        to_search = emails.readlines()
        return args

# end validate_args ---------------------------------------------------

    def show_banner(self):
        with open('banner.txt', 'r') as f:
            data = f.read()
            print("\033[94m%s\033[0;0m" % data)

    def run(self, args):
        if args.proxy == 'l' or args.proxy == 'a':
            print("[-] Seaching for breached LinkedIn Credentials")
            linked = linkedin.LinkedIn(args.email)
            linked.linkedin(args.email)

        if args.proxy == 'm' or args.proxy == 'a':
            print("[-] Searching for breached MyFitnessPal Credentials")
            myFit = myfitnesspal.MyFitnessPal(args.email)
            myFit.myfitnesspal(args.email)

        #Add another breach if you want :)
        #if args.proxy == 'r':
        #    print("[-] Searching for breached Credentials (Good Luck!)")
        #    rand = random.Random(to_search)

if __name__ == "__main__":
    c = Credible()
    c.show_banner()
    args = c.validate_args()
    c.run(args)
