import os
import requests

git_add_result_code = os.system("git add .")
print('Changes added with exit code: ' + str(git_add_result_code))

git_commit_result_code = os.system("git commit -m 'Save changes by cron job'")
print('Changes committed with exit code: ' + str(git_commit_result_code))

git_push_result_code = os.system("git push origin master")
print('Changes committed with exit code: ' + str(git_push_result_code))
