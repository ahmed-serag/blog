from handler import Handler
import hashlib
import logging




def hash_str(s):
    arr = s.split(' ')

    logging.info('print')
    logging.info(s)
    if(' ' in s):
        if(arr[1] == hashlib.sha256(str(arr[0]))):
            return False, int(arr[0])
        else:
            return True, 0
    else:
        return True, 0
class Cookie(Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        visit = self.request.cookies.get('visits', '0')
        logging.info('print2222222')
        logging.info(visit)
        cheat, visits = hash_str(visit)
        visits += 1
        hasa = hashlib.sha256(str(visits)).hexdigest()
        a="EF2D127DE37B942BAAD06145E54B0C619A1F22327B2EBBCFBEC78F5564AFE39D"
        self.response.headers.add_header('Set-Cookie',"visits=5,EF2D127DE37B942BAAD06145E54B0C619A1F22327B2EBBCFBEC78F5564AFE39D")
        #self.response.headers.add_header('Set-Cookie',"visits=%(value) %(has)" % {'value': visits, 'has':hash })   
        if(cheat):
            self.write('you are a cheater!!!')
        else:
            self.write('you visited us %s', visits)   
