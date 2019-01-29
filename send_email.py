import time as TIME 
from email_class import *
from account import *
      
def main():
    g=G_email()
    g.mail_content=write_email()
    g.receive_account=get_account()
    g.clocking_send()
    g.everyday_send()

def write_email(email_dict={}):#读取email.txt文件的内容

    email_dict['subject']='my first email'
    content_form=input('输入文本格式t/h：')
    if content_form=='t':#邮件内容为txt格式
        with open('email.txt') as email_file:
            email_dict['content_text']=email_file.read()
    if content_form=='h':#邮件内容为html格式
        with open('hello.html') as content_file:
           email_dict ['content_html']=content_file.read()
    s=input('是否添加附件y/n：')
    if s == 'y':#添加附件
        s=input('请输入附件名(逗号隔开)：')
        attachments=s.split(',')
        email_dict['attachments']=attachments
    if s == 'n':
        pass
    return email_dict

if __name__ == '__main__':                
    main()
