import os
import requests


os.system("ssh-keygen -t rsa -f ./sshkey -q -N ''")
ssh_key = open('sshkey.pub', 'r').read()


try_request = requests.post("https://api.github.com/repos/architecture-playground/jenkins-docker-compose/keys")
print(try_request)


type_ssh_post = {
         "title": "ssh_request",
         "key": "ssh_key",
}

git_add_result_code = os.system("git add .")
print('Changes added with exit code: ' + str(git_add_result_code))

git_commit_result_code = os.system("git commit -m 'Save changes by cron job'")
print('Changes committed with exit code: ' + str(git_commit_result_code))

git_push_result_code = os.system("git push origin master")
print('Changes pushed with exit code: ' + str(git_push_result_code))
