# Description

Credible sorts through the LinkedIn and MyFitnessPal data breaches (or any you like) and returns any matches in user:pass format. This program will spit out all matches it finds within the database. *The dumps will not be included in this repository*.

In some cases, the password will be returned as plaintext. If the password returns as hashed, it is SHA1. 

When searching for emails, you can use key words. If you're looking for somebody with a unique last name, for example, you can simply replace an email address with the last name and credible will spit out all users with the same last name.

## Finding and Using the Databases within Credible

Finding the databases is easy if you but your mind into it. I downloaded mine off a not-so-safe looking website - to give you an idea. 

Once downloaded, it is wise to break them up into smaller .txt files so python can read through them more efficently. In my case, the LinkedIn and MyFitnessPal were cut into 37 and 20 .txt files, respectively.

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
If you take one look at this program, it is clearly far from complete. 

1. I need to implement the --path variable as well as more data breach's for a more in-depth scan of an email address.
2. I will add a SHA1 decoder at some point to save you the headache of cracking the password yourself.
3. I plan on adding more breach compilations to credible for stronger results.
