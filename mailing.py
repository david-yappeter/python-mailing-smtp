# https://pypi.org/project/keyring/#what-is-python-keyring-lib
import keyring
# https://github.com/kootenpv/yagmail
import yagmail

# # Set Email Credentials to System Instead Of Code, NB: USER WITHOUT @GMAIL.COM
# keyring.set_password('yagmail', 'gmailUser', 'password')

# # Another Way To Save Credentials, But This One Fail , NB: USER WITHOUT @GMAIL.COM
# yagmail.register('gmailUser', 'password')

# Sender Email , NB: USER WITH @GMAIL.COM
yag = yagmail.SMTP('senderEmail@gmail.com')

# Receiver Email, Subject and Email Body
to = 'receiver@gmail.com'
subject = 'This is obviously the subject'
body = 'This is obviously the body'
html = '<img src="https://drive.google.com/uc?export=view&id=11d8qop_7ENjyyvZsTq3ALzhUsW0jFNRX">Click me!'

# Sending Email
# yag.send(to = to, subject = subject, contents = body)
yag.send(to = to, subject = subject, contents = [body, html])
# yag.send(contents = [body, img])