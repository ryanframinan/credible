  class LinkedIn:

    def __init__(self, email):
        self.email = email

    def linkedin(self, email):
        self.email = email
        allMatches = []
        i = 1

        while(i <= 37):
            with open(r'FULLPATH\modules\files\linkedin\{}.txt'.format(i)) as f:
                for num, line in enumerate(f, 1):
                    if email in line:
                        line = line.replace("\n", "")
                        allMatches.append(line)

            i+=1
            f.close()
        if len(allMatches) != 0:
            j = 0
            while j < len(allMatches):
                print("[+] LinkedIn Credentials Found:\t", allMatches[j])
                j+=1
        else: print('\033[1;91m[-]\033[0m Credentials are not in LinkedIn Databreach.')

if __name__ == "__main__":
    l = LinkedIn(email)
    l.linkedin()
