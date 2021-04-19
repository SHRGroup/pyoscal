git config --global user.email "${GITLAB_USER_EMAIL}"
git config --global user.name "${GITLAB_USER_ID}"

pushd OSCAL
git fetch --tags
latestTag=$(git describe --tags `git rev-list --tags --max-count=1`)
git checkout $latestTag
popd 

git add OSCAL 
git commit -m 'Updated to latest NIST OSCAL TAG'
# git push