class Node :
    def __init__(self,data = None) -> None:
        self.data = data
        self.next = None
        
class PasswordManager:
    def __init__(self) -> None:
        self.old_pass = None
        
    def append (self,data) :
        node = Node (data)
        
        if self.old_pass is None :
            self.old_pass = node
            return 
        else :
            current = self.old_pass
            
            while current.next :
                current = current.next
            current.next = node
            
    def get_password (self) :
        current = self.old_pass
        
        while current.next :
            current = current.next
        return current.data
    
    def set_password (self,data):
        passwd = [password for password in pass_manager.iter()]
        for x in passwd :
            if data == x :
                pass
        else :
            self.append(data)
        
    def is_correct (self,data):
        return data == self.get_password()
    
    def iter (self) :
        current = self.old_pass
        
        while current :
            val = current.data
            current = current.next
            yield val
    

if __name__ == '__main__' :
    def validate_pass (pass_manager) :
        passwords = ['kassim2001','#Azz%m@l%2__1','kassimali2001','ubuntu2020','20401054Ka']
        [pass_manager.append(password) for password in passwords]

        print(pass_manager.get_password())
        pass_input = input('Enter your password:')

        if pass_manager.is_correct(pass_input):
            print("Logged in successfully")
            
        else :
            pass_manager.set_password(pass_input)
            print("Password is reset successfully ")
            print([password for password in pass_manager.iter()])
        
    pass_manager = PasswordManager ()
    validate_pass(pass_manager)