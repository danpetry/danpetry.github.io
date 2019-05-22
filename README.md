## test

./develop_server start 8000

## deploy

pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages
git checkout master
git merge gh-pages --allow-unrelated-histories --strategy-option=theirs

## todos

- continue stripping down the theme
- have all posts fully open instead of having continue reading button
- make about page look different from blogs - eg no "posted on" line
- sort out white bit when you scoll down
- upload mixes to mixcloud and add that
- contact details
- make the blog pages look like on the wireframe
- add ground symbol in top right and a cooler-looking dropdown menu
- Deploying/pull to master: Commit /output and add blank index.html pointing to
  /output? Best way to do this? Last commit of branch?
- get an RA icon working
- get opinions and refine
  - use bootstrap for eg sidebar/icons, to get better auto resizing and get an
    RA icon
