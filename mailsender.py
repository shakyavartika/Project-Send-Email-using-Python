import smtplib as s
ob= s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("shakyavartika@gmail.com","vartika@97")
subject="This email using python"
body="this is sending email using python script."
message="Subject:{}\n\n{}".format(subject,body)
#print (message)
listOfAddress=["vshakya_be19@thapar.edu"]
ob.sendmail("shakyavartika",listOfAddress,message)
print("sent")
ob.quit