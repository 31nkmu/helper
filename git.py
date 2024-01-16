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

git branch -d
git reset --hard


delete file from all commits
  git filter-branch --tree-filter 'rm -f path/to/your/file' -- --all
