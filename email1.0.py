import zmail

class G_email(server):

    def __init__(self):
        self.__mail_content={}
        self.__receive_account=[]


    @property 
    def mail_content(self):
        '''getter'''
        return self.__mail_content

    @mail_content.setter  
    def mail_content(self,email_dict):
        '''setter'''
        self.__mail_content=email_dict   

    @property
    def receive_account(self):
        '''getter'''
        return self.__receive_account

    @receive_account.setter
    def receive_account(self,account_list):
        '''setter'''
        self.__receive_account=account_list

    def send__email(self):
        server.send_mail(self.__receive_account,self.__mail_content)
    
    def clocking_send(self):
        while True:
            s=input('是否即时发送y/n:')
            if s == 'y':
                self.send__email()
                return
            elif s == 'n':
                clock_time=input('请设置发送的时间,时-分-秒：')
                c=clock_time.split('-') 
                n=TIME.localtime()[3:5]
                TIME.sleep((int(c[3])-n[3])*3600+(int(c[4])-n[4])*60+(int(c[5])-n[5]))
                self.send__email()
                return
            else:
                continue

    def everyday_send(self):
        while True:
            s=input('是否每天发送y/n:')
            if s == 'y':
                TIME.sleep(86400)
                self.send__email()
                return
            elif s == 'n':
                return
            else:
                continue