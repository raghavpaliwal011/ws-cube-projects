# sending multiple emails using python 
import smtplib as s
ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('raghavpaliwal1109@gmail.com',785575875)
sub = ("test python")
body = "raghav is the god of gta5"
message = "subject:{}\n\n{}".format(sub,body)
listadd = ['deepti1230paliwal@gmail.com']
ob.send('',listadd,message)
print("send mail")
ob.quit()