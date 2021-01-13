# https://stackoverflow.com/questions/59895/how-to-get-the-source-directory-of-a-bash-script-from-within-the-script-itself
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo $DIR

# execute from wherever:
# $ . wherever/get_absolute_path_of_dir_of_script.sh
# path/demos/bash