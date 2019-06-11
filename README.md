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

- Put margin at top of first post
- have all posts fully open instead of having continue reading button
- make about page look different from blogs - eg no "posted on" line
- make the blog pages look like on the wireframe
- add ground symbol in top right and a cooler-looking dropdown menu
- get opinions and refine
  - use bootstrap for eg sidebar/icons, to get better auto resizing and get an
    RA icon
