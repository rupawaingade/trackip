from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in,sender=User)
def login_sucess(sender,request,user,**kwargs):
    # print("-----------------------")
    # print("Logged_in_signal run intro..")
    ip=request.META.get('REMOTE_ADDR')
    #print("client ip:",ip)
    request.session['ip']=ip
   