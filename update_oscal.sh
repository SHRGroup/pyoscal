pushd OSCAL
git fetch --tags
latestTag=$(git describe --tags `git rev-list --tags --max-count=1`)
git checkout $latestTag
popd 
git add OSCAL 
git commit -m 'Updated to latest NIST OSCAL TAG'
# git push