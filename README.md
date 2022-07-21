# Description

Credible sorts through the inputed data breaches and returns any matches in username@email.com:password format. This program will spit out all matches it finds within the database. *A collection of breaches will be linked below*.

```
                  ___________________ ______
________________________  /__(_)__  /____  /____            _____________  __
_  ___/_  ___/  _ \  __  /__  /__  __ \_  /_  _ \           ___  __ \_  / / /
/ /__ _  /   /  __/ /_/ / _  / _  /_/ /  / /  __/  ___      __  /_/ /  /_/ / 
\___/ /_/    \___/\__,_/  /_/  /_.___//_/  \___/   _(_)     _  .___/_\__, /  
                                                            /_/     /____/   
Credible: fram, wannabe pentester
OSINT tool, use responsibly      
```
## Usage
```
usage: credible.py [-h] [--proxy <proxy>] [--email <email>] [--path <path>] 
optional arguments:
  -h, --help       show this help message and exit
  --proxy <proxy>  Proxy type: l = LinkedIn, m = MyFitnessPal, r = Random, a = all
  --email <email>  Pass a single email to scan. TIP: Can scan for username.       
  --path <path>    Pass a file containing emails one per line to scan.
```
Example: Finding an email in the LinkedIn Data Breach
```
$ python credible.py --proxy l --email EXAMPLE@yahoo.com
                  ___________________ ______
________________________  /__(_)__  /____  /____            _____________  __
_  ___/_  ___/  _ \  __  /__  /__  __ \_  /_  _ \           ___  __ \_  / / /
/ /__ _  /   /  __/ /_/ / _  / _  /_/ /  / /  __/  ___      __  /_/ /  /_/ /
\___/ /_/    \___/\__,_/  /_/  /_.___//_/  \___/   _(_)     _  .___/_\__, /
                                                            /_/     /____/
Credible: fram, wannabe pentester
OSINT tool, use responsibly
[-] Seaching for breached LinkedIn Credentials
[+] LinkedIn Credentials Found: EXAMPLE@yahoo.com:1a79a4d60de6718e8e5b326e338ae533
```

## Future Construction 

1. Addition of a SHA1 decoder to save you the headache of cracking the password yourself.
2. Addition of more breach compilations for stronger results.
