# Git Kurulumu

https://git-scm.com/

# git config (Kullanıcı adı ve mailinin ayarlanması)

Kullanıcı adı ve mail adresinin tanımlanması:
git config --global user.name "mvahit"
git config --global user.email "m.vahitkeskin@gmail.com"

# git init

git init (git repository'si oluşturmak)

# git status

# git add 

# git commit 

# git log

# git show

# git reset --soft commit_id 


git branch -d new_feature2
git checkout -b new_feature

soft: belirtilen committen sonraki commitleri siler. Dosyalardaki değişiklikler bozulmaz. Düzenlenmiş dosyalar git'e eklenir.

mixed: belirtilen comitten sonraki commitleri siler. Dosyalardaki değişiklikler bozulmaz. Dosyalar git'e eklenmeyecek. (untracked hale gelecek)

hard: belirtilen committen sonraki commitleri siler. Dosyalarda yapılan değişiklikler geri alınır. Yapılan her şey uçar.
