# to send email
import smtplib, ssl

s = smtplib.SMTP(host='smtp.gmail.com', port=587)  # connecting with smpt
s.starttls()
s.login('youremailidgmail.com', '**********')
try:
    s.sendmail('yourmailid@gmail.com', 'topersonmailid@gmail.com', 'subject: testing ....\n\n Dear x,\n ...\n\n')
    print("Message sent successfully")
except:
    print("Failed to send message")
s.quit()  # close the connection
