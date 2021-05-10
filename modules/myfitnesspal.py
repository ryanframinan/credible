class MyFitnessPal:

    def __init__(self, email):
        self.email = email

    def myfitnesspal(self, email="cmcdoug2@gmu.edu"):
        self.email = email
        success = False
        i = 1

        while(i <= 20):
            with open(r'\modules\files\myfitnesspal/{}.txt'.format(i)) as f:
                for num, line in enumerate(f, 1):
                    if email in line:
                        line = line.replace('"', '')
                        line = line.replace(",", ":")
                        print("[+] MyFitnessPal Credentials Found:\t", line)
                        success = True
                    if success == True: break
            i+=1
            f.close()
        if success == False:
            print('\033[1;91m[-]\033[0m Credentials are not in MyFitnessPal Databreach.')

if __name__ == "__main__":
    m = MyFitnessPal(email)
    m.myfitnesspal()


