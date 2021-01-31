## test

./watch.rb . localhost &
./develop_server start 8000

## deploy

The deploy script builds and deploys the site without changing branch. The
gh-pages branch is where the built and deployed site resides.

The script below builds the site into the ./output folder, pushes the contents
of the ./output folder to the gh-pages branch, and then pushes the gh-pages
branch to github. On github, the site is setup to be served from the gh-pages
branch.

./deploy.sh

## todos

- get opinions and refine
- "keep updated" newsletter form
- Do desktop version, including making the blog pages look like on the wireframe
