## test

./watch.rb . localhost &
./develop_server start 8000

## deploy

The deploy script builds the site into the output/ folder, and then copies the
contents of this folder to the gh-pages branch. This is the branch which the
site is served from.

./deploy.sh
