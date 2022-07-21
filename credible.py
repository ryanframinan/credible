import argparse
import os
from modules.exact import Exact
from modules.suggest import Suggest


class Credible():
    def validate_args(self):
        parser = argparse.ArgumentParser(description="")
        parser.add_argument("--exact", dest="exact", action='store_true',
                            help="Pass the exact username or domain you want to search for.")
        parser.add_argument("--suggest", dest="suggest", action='store_true', 
                            help="Let Credible suggest a username or domain to output based on your input. This is purposefully 90 accurate.")
        parser.add_argument("-u", metavar="<user>", dest="user", default=None, 
                            help="Pass a single user to scan.")
        parser.add_argument("-d", metavar="<domain>", dest="domain", default=None, 
                            help="Pass a single domain to scan.")
        parser.add_argument("-f", metavar="<file>", dest="file", type=str, default=None, 
                            help="Pass a file containing credential dump one per line to scan. Pattern must be username@example.com:password")
        parser.add_argument("-o", metavar="<outfile>", dest="outfile", type=str, default=None, 
                            help="Save the output to a file.")
        args = parser.parse_args()

        if not (args.exact or args.suggest):
            print("[-] Please specify --exact or --suggest.")
            exit(1)
        if not (args.user or args.domain):
            print("[-] Missing -u or -d argument")
            exit(1)
        if not (args.file):
            print("[-] Missing -f argument")
            exit(1)
        if args.file != None:
            if os.path.exists(args.file) == False:
                print("[-] " + args.file + " doesn't exist in directory")
                exit(1)
        return args

    def show_banner(self):
        with open('banner.txt', 'r') as f:
            data = f.read()
            print("\033[94m%s\033[0;0m" % data)

    def run(self, args):
        if args.user and args.domain:
            email = args.user + "@" + args.domain
            print("[-] Searching for exact email address: " + email)
            e = Exact(email, args.file)
            e.both()
        elif (args.user or args.domain) != None:
            if args.exact:
                if args.user != None:
                    print("[-] Searching for exact username: " + args.user)
                    e = Exact(args.user, args.file)
                    e.username()
                if args.domain != None:
                    print("[-] Searching for exact domain: " + args.domain)
                    e = Exact(args.domain, args.file)
                    e.domain()
            if args.suggest:
                if args.user != None:
                    print("[-] Suggesting for username: " + args.user)
                    s = Suggest(args.user, args.file)
                    s.username()
                if args.domain != None:
                    print("[-] Suggesting for domain: " + args.domain)
                    s = Suggest(args.domain, args.file)
                    s.domain()

if __name__ == "__main__":
    c = Credible()
    c.show_banner()
    args = c.validate_args()
    c.run(args)
