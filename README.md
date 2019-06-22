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

- get opinions and refine
- "keep updated" newsletter form
- Do desktop version, including making the blog pages look like on the wireframe
