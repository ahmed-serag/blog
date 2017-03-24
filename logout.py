from handler import Handler

class LogOut(Handler):
    '''
    this class is responsible for logging user out
    '''
    def get(self):
        self.logout()
        self.redirect('/')