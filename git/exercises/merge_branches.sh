echo "> merge b to master"
echo "> commiting from b"
git commit -a -m "b commit"

echo "> checking out to master"
git checkout master

echo "> checking out to master"
git merge b

echo "> commiting from master"
git commit -a -m "master commit"
git push

