from handler import Handler

class LogOut(Handler):
    def get(self):
        self.logout()
        self.redirect('/')