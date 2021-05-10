class LinkedIn:

    def __init__(self, email):
        self.email = email

    def linkedin(self, email):
        self.email = email
        success = False
        i = 1

        while(i <= 37):
            with open(r'\modules\files\linkedin\{}.txt'.format(i)) as f:
                for num, line in enumerate(f, 1):
                    if email in line:
                        print("[+] LinkedIn Credentials Found:\t", line)
                        success = True
                    if success == True: break
            i+=1
            f.close()
        if success == False:
            print('\033[1;91m[-]\033[0m Credentials are not in LinkedIn Databreach.')

if __name__ == "__main__":
    l = LinkedIn(email)
    l.linkedin()
