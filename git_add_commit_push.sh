#bin/bash

git add .
echo 'added new files'
git commit -m 'Save changes by cron job'
echo 'add to commit'
git push origin master
echo 'i push in master'