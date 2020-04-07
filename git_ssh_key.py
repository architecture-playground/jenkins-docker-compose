import os
import requests
import json

print(os.system("whoami"))
print(os.system("pwd"))
os.system("mkdir .ssh")
os.system("ssh-keygen -t rsa -f ./.ssh/sshkey -q -N ''")
ssh_key = open('.ssh/sshkey.pub'.strip(), 'r').read()

message = json.dumps({
    "title": "ssh_request",
    "key": ssh_key
})

headers = {'Authorization': 'Basic QnVsZ2Frb3ZBbnRvbjpBa2FtZWdha2lsbDkw'}
response = requests.post("https://api.github.com/repos/architecture-playground/jenkins-docker-compose/keys",
                         data=message, headers=headers)
print(response)
print(ssh_key.strip())
