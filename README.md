## test

./develop_server start

## deploy

The deploy script builds the site into the output/ folder, and then copies the
contents of this folder to the gh-pages branch. This is the branch which the
site is served from.

./deploy.sh

## write articles

To add new projects in the dropdown menu, add the project page URL in the
dropdown-item list in my-theme/templates/base.html.

If an article is in the /content/pages folder, it will end up in
{SITE_URL}/pages/{article title}.html. If it has a "category" field, there will
be a link at the bottom "Diary". This will link to the blog entries formed by
the articles in the content/ folder with that category. If there is no
"category" field, there won't be a "Diary" link. Note that the "category" field
in the /content/pages articles need to be all lowercase.

Filenames of the articles don't affect deployed content, just the metadata.
