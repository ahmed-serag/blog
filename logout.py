from handler import Handler

class LogOut(Handler):
    '''
    this class is responsible for logging user out
    '''
    def get(self):
       
        if self.read_secure_cookie('user_id'):
            self.logout()
            self.redirect('/')
        else:
            self.redirect('/')