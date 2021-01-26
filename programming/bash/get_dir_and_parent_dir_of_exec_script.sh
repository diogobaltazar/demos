CURR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
CURR_DIR_PARENT_DIR="$(echo $CURR_DIR | awk 'BEGIN{FS=OFS="/"}{NF--; print}')"
