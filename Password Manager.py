class BasePasswordManager:
    def __init__(self):
        self.old_passwords = []
        
    def get_passwords(self):
        return self.old_passwords[-1]
        
    def is_correct(self,passw):
        if passw == self.old_passwords[-1]:
            return True
        else:
            return False
        
class PasswordManager(BasePasswordManager):
    def get_level(self,password=None):
        if password is None:
            password = self.old_passwords[-1]
        count = -1
        if password.isalpha() or password.isdigit():
            count = 0
        if any(i.isalpha() for i in password) and any(i.isdigit() for i in password):
            count = 1
        for i in password:
            if i in "!@#$%^&*()-_+=[]{}|;':,.<>?/~" and count==1:
                count = 2
        return count
            
    def set_password(self,new_pass):
        if(self.get_level(new_pass)>self.get_level(self.old_passwords[-1]) and len(new_pass)>=6):
            self.old_passwords.append(new_pass)
            return True
        elif(self.get_level(new_pass)==self.get_level(self.old_passwords[-1]) and len(new_pass)>=6 and self.get_level(self.old_passwords[-1])==2):
            self.old_passwords.append(new_pass)
            return True
        else:
            return False
            
def Dashboard():
        print('1: Get password 2: Compare password 3: Set password 4: Get level')
        
        ch = input("Enter choice ")
        if ch == "1":
            print("Your curr password is", p.get_passwords())
        elif ch == "2":
            passw = input("Enter comparative password ")
            print("Password checked status : ",p.is_correct(passw))
        elif ch == "3":
            passw = input("Enter new password ")
            if p.set_password(passw):
                print("Password changed succesfully")
            else:
                print("Password failed")
                print("Possible reasons are Security level lower or Same level password but not in highest security level")
        elif ch == "4":
            passw = input("Enter new password leave blank for old password ")
            if not passw:
                print("Old password sec level:", p.get_level(None))
            else:
                print("New password sec level:", p.get_level(passw))
        else:
            print("Wrong option choosen")
        print("Would you like to do anything more?")
        cho = input("1: YES 2: NO ")
        if cho == "1":
            Dashboard()
        else:
            print("Thank You")
            
        
p = PasswordManager()
p.old_passwords = ['Holahe']
curr = p.get_passwords()
Dashboard()