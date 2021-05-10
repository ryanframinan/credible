# Description

Credible sorts through the LinkedIn and MyFitnessPal data breaches (or any you like) and returns any matches in user:pass format. The dumps will not be included in this repository.

In some cases, the password will be returned as plaintext; however, expect to use hashcat if you get a hit. 


## 

```
                  ___________________ ______
________________________  /__(_)__  /____  /____            _____________  __
_  ___/_  ___/  _ \  __  /__  /__  __ \_  /_  _ \           ___  __ \_  / / /
/ /__ _  /   /  __/ /_/ / _  / _  /_/ /  / /  __/  ___      __  /_/ /  /_/ / 
\___/ /_/    \___/\__,_/  /_/  /_.___//_/  \___/   _(_)     _  .___/_\__, /  
                                                            /_/     /____/   
Credible: fram, wannabe pentester
OSINT tool, use responsibly
usage: credible.py [-h] [--proxy <proxy>] [--email <email>] [--path <path>]       
```
## Usage
```
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
If you take one look at this program, it is clearly far from complete. I need to implement the --path variable as well as more data breach's for a more in-depth scan of an email address.

Hopefully, I will be able to add an MD5 and/or bcrypt decoder at some point to save you the headache of cracking the password yourself.
