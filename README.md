# Description

Credible sorts through the LinkedIn and MyFitnessPal data breaches (or any you like) and returns any matches in username:password format. This program will spit out all matches it finds within the database. *The dumps will not be included in this repository*.

In some cases, the password will be returned as plaintext, null, or xxx. If the password returns as hashed, it is SHA1. 

When searching for emails, you can use key words. If you're looking for somebody with a unique last name, for example, you can simply replace an email address with the last name and credible will spit out all users with the same last name.

## Finding, Using, and Optimizing the Databases within Credible

Finding the databases is easy if you but your mind into it. I downloaded mine off a not-so-safe looking website - to give you an idea. 

Once downloaded, it is wise to break them up into smaller .txt files so python can read through them more efficently. In my case, the LinkedIn and MyFitnessPal were cut into 37 and 20 .txt files, respectively.

If you'd like, alphabetizing the .txt files can make the program run more efficiently. Meaning, if the email you are looking for starts with an 'r', instead of searching for 37 .txt files, it will only search through the file deemed with strings starting with 'r'. This will save time if you need tons of results fast.

Here is the script you would use to start this process:
```
sort 1.txt > 1.txt.sorted && mv 1.txt.sorted 1.txt
```

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
