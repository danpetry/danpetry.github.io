rm -r ./output
pelican content -o output -s pelicanconf.py
cp CNAME output/
ghp-import output -b gh-pages
git push origin gh-pages
