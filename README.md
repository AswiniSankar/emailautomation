# emailautomation
By using python email can be automated


## p1.py - simple email automation
  1. import smtp,ssl package
  2. get smtp connection 
  3. start tls
  4. login with your email id and password
  5. using connection object and sendmail() function  send the mail to the respective person by giving reciever mail id and subject along with body content.
  6. once the mail is send close the connection 

## p2.py - sending links in mail 

  1. follow the same procedure above in addition to that import MIME text and multipart package.
  2. store the text in html format.
  3. using mimetext convert plane text into mimetext.
  4. add mimetext with the message and send it to the reciever.
