# Python-Mailing-SMTP
### Setup & Installation
--------------------------
[**Keyring**](https://pypi.org/project/keyring/#what-is-python-keyring-lib) -> to save our Email Credentials Inside Credentials Manager Instead of placing it directly into our code
```
pip3 install keyring
```
[**yagmail**](https://github.com/kootenpv/yagmail) -> Library that I use to help me Sending Email
```
pip3 install yagmail
```
----------------------------
### Set Credential Using **KeyRing**
----------------------------
```
keyring.set_password('yagmail', 'gmailUserWithout@', 'password')
```
Run This Code Once, before using ``` yagmail.send() ```
##### For Windows user, you can edit your Credential in Credential Manager -> Windows Credentials -> Generic Credential
