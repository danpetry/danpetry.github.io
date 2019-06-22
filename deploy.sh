pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages
git checkout master
git merge gh-pages --allow-unrelated-histories --strategy-option=theirs
git push
