## test

./watch.rb . localhost &
./develop_server start 8000

## deploy

pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages
git checkout master
git merge gh-pages --allow-unrelated-histories --strategy-option=theirs
git push

## todos

- add ground symbol in top right and a cooler-looking dropdown menu
- get opinions and refine
- Do desktop version, including making the blog pages look like on the wireframe
