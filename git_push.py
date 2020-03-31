import os
import requests
import json


# headers = {'Authorization': 'Basic QnVsZ2Frb3ZBbnRvbjpBa2FtZWdha2lsbDkw'}
#
# os.system("ssh-keygen -t rsa -f ./sshkey -q -N ''")
# ssh_key = open('sshkey.pub'.strip(), 'r').read()
#
# message = json.dumps({
#     "title": "ssh_request",
#     "key": ssh_key
# })
#
# response = requests.post("https://api.github.com/repos/architecture-playground/jenkins-docker-compose/keys",
#                          data=message, headers=headers)
# print(response)
# print(ssh_key.strip())

#os.system("rm -rf sshkey*")

git_add_result_code = os.system("git add .")
print('Changes added with exit code: ' + str(git_add_result_code))

git_commit_result_code = os.system("git commit -m 'Save changes by cron job'")
print('Changes committed with exit code: ' + str(git_commit_result_code))

git_push_result_code = os.system("git push origin master")
print('Changes pushed with exit code: ' + str(git_push_result_code))
