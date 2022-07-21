class Suggest:
    def __init__(self, user, file):
        self.user = user
        self.file = file
    
    def username(self):
        with open(self.file) as f:
            for num, line in enumerate(f, 1):
                temp = line.split(":")[0]
                if self.user in temp.split("@")[0]:
                    line = line.replace("\n", "")
                    print("[+] Suggested User Credentials Found:\t", line)
        f.close()
        if len(line) == 0:
            print('\033[1;91m[-]\033[0m Credentials are not in Exact Databreach.')
    def domain(self):
        with open(self.file) as f:
            for num, line in enumerate(f, 1):
                temp = line.split(":")[0]
                if self.user in temp.split("@")[1]:
                    line = line.replace("\n", "")
                    print("[+] Suggested Domain Credentials Found:\t", line)
        f.close()
        if len(line) == 0:
            print('\033[1;91m[-]\033[0m Credentials are not in Exact Databreach.')
