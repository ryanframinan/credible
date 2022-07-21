# Description

Credible sorts through the inputed data breaches and returns any matches in username@email.com:password format. This program will spit out all matches it finds within the database. *A collection of breaches will be linked below*.

## Usage
```
$ python3 credible.py -h
                  ___________________ ______                                 
________________________  /__(_)__  /____  /____            _____________  __
_  ___/_  ___/  _ \  __  /__  /__  __ \_  /_  _ \           ___  __ \_  / / /
/ /__ _  /   /  __/ /_/ / _  / _  /_/ /  / /  __/  ___      __  /_/ /  /_/ / 
\___/ /_/    \___/\__,_/  /_/  /_.___//_/  \___/   _(_)     _  .___/_\__, /  
                                                            /_/     /____/   
Find Credentials Fast

usage: credible.py [-h] [--exact] [--suggest] [-u <user>] [-d <domain>] [-f <file>] [-o <outfile>]

optional arguments:
  -h, --help    show this help message and exit
  --exact       Pass the exact username or domain you want to search for.
  --suggest     Let Credible suggest a username or domain to output based on your input.
  -u <user>     Pass a single user to scan.
  -d <domain>   Pass a single domain to scan.
  -f <file>     Pass a file containing credential dump one per line to scan. Pattern must be
                username@example.com:password
```
Example: Finding emails via exact domain
```
$ python3 credible.py --exact -d company.com -f emails.txt

                  ___________________ ______                                 
________________________  /__(_)__  /____  /____            _____________  __
_  ___/_  ___/  _ \  __  /__  /__  __ \_  /_  _ \           ___  __ \_  / / /
/ /__ _  /   /  __/ /_/ / _  / _  /_/ /  / /  __/  ___      __  /_/ /  /_/ / 
\___/ /_/    \___/\__,_/  /_/  /_.___//_/  \___/   _(_)     _  .___/_\__, /  
                                                            /_/     /____/   
Find Credentials Fast

[-] Searching for exact domain: company.com
[+] Exact Domain Credentials Found:      employee_1@company.com:password
[+] Exact Domain Credentials Found:      employee_2@company.com:password
[+] Exact Domain Credentials Found:      employee_3@company.com:password
[+] Exact Domain Credentials Found:      employee_4@company.com:password
```

## Future Construction 

1. Make a GUI 
2. Add output flag (will obviously be easy but I'm lazy)   
3. Optimize the suggest flag. Right now it's a simple `if <foo> in <bar>` and I'd like to make it 90% accurate for stronger returns.
