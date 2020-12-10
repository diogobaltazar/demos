echo -e "> install 3.7 python version without overriding the last python"
echo -e "version under the symlink python3"
echo -e "> update the packages list and installing the prerequisites"
sudo apt install software-properties-common

echo -e "> add the deadsnakes PPA to the sources list"
sudo add-apt-repository ppa:deadsnakes/ppa

echo -e "> install python 3.7.8"
sudo apt-get install python3.7

echo -e "> get installed interpreter path"
which python3.7

echo -e "> navigate to your project's folder"
echo -e "> create environment with the installed interpreter"
virtualenv -v $PATH_TO_INTERPRETER $ENV_NAME

echo -e "> ignore env folder"
cat $VIRTUAL_ENV_NAME >> .gitignore

echo -e "> activate env"
source ${ENV_NAME}/bin/activate

echo -e "> check env's python interpreter"
python -V
which python3.7

echo -e "> deactivate env"
deactivate