class MyFitnessPal:

    def __init__(self, email):
        self.email = email

    def myfitnesspal(self, email):
        self.email = email
        allMatches = []
        i = 1

        while(i <= 20):
            with open(r'FULLPATH\modules\files\myfitnesspal/{}.txt'.format(i)) as f:
                for num, line in enumerate(f, 1):
                    if email in line:
                        line = line.replace('"', '')
                        line = line.replace(",", ":")
                        allMatches.append(line)
            i+=1
            f.close()
        if len(allMatches) != 0:
            j = 0
            while j < len(allMatches):
                print("[+] MyFitnessPal Credentials Found:\t", allMatches[j])
                j+=1
        else: print('\033[1;91m[-]\033[0m Credentials are not in MyFitnessPal Databreach.')

if __name__ == "__main__":
    m = MyFitnessPal(email)
    m.myfitnesspal()
