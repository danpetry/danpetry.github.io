## test

./watch.rb . localhost & \
./develop_server start 8000

## deploy

The deploy script builds the site into the output/ folder, and then copies the
contents of this folder to the gh-pages branch. This is the branch which the
site is served from.

./deploy.sh

## write articles

If an article is in the /content/pages folder, and has a "category" field,
there will be a link at the bottom "Diary". This will link to the blog entries
formed by the articles in the content/ folder with that category. If there is
no "category" field, there won't be a "Diary" link. Note that the "category"
field in the /content/pages articles need to be all lowercase.

To add new items in the dropdown menu, add them in the dropdown-item list in
my-theme/templates/base.html. Articles in the content/pages folder will end up
in {SITE_URL}/pages/{article title}.html.

Filenames of the articles don't affect deployed content, just the metadata.
