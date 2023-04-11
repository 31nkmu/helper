ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

ssh-keygen -o
git config --global user.name "username"
git config --global user.email "email"
git config --global init.defaultBranch main
git config --list

cd ~/.ssh/
cat id_rsa.pub
copy ssh_key
github -> settings -> ssh keys 
paste ssh_key

git init
git remote add origin
git add .
git commit -m 'comment'
git status
git push origin master
git pull
git branch
git checkout
git branch -d
git reset --hard
git clone
git log

