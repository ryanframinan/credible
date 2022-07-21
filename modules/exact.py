class Exact():
    def __init__(self, user, file):
        self.user = user
        self.file = file

    def username(self):
        with open(self.file) as f:
            for num, line in enumerate(f, 1):
                if self.user == line.split('@')[0]:
                    line = line.replace("\n", "")
                    print("[+] Exact User Credentials Found:\t", line)
        f.close()
        if len(line) == 0:
            print('\033[1;91m[-]\033[0m Credentials are not in Exact Databreach.')
    
    def domain(self):
        with open(self.file) as f:
            for num, line in enumerate(f, 1):
                temp = line.split(':')[0]
                if self.user == temp.split('@')[1]:
                    line = line.replace("\n", "")
                    print("[+] Exact Domain Credentials Found:\t", line)
        f.close()
        if len(line) == 0:
            print('\033[1;91m[-]\033[0m Credentials are not in Exact Databreach.')
    def both(self):
        with open(self.file) as f:
            for num, line in enumerate(f, 1): 
                if self.user in line.split(":")[0]:
                    line = line.replace("\n", "")
                    print("[+] Exact Credentials Found:\t", line)
        f.close()
        if len(line) == 0:
            print('\033[1;91m[-]\033[0m Credentials are not in Exact Databreach.')


if __name__ == "__main__":
    l = Exact()
    l.username()
