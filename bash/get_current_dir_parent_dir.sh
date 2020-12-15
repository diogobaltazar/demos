# add NF--; to go up the hierarchy
CURR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
CURR_DIR_PARENT_DIR_PATH="$(echo $CURR_DIR | awk 'BEGIN{FS=OFS="/"}{NF--; print}')"
echo $CURR_DIR_PARENT_DIR_PATH

# execute from wherever:
# $ . wherever/get_current_dir_parent_dir.sh
# path/demos