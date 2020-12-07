unset opt OPTARG OPTIND
while getopts ":a:" opt; do
  case $opt in
    a)
      echo "-a: $OPTARG" >&2
      ;;
    \?)
      echo "invalid: -$OPTARG" >&2
      ;;
    :)
      # if no argument is provided getopts will set opt to :
      echo "invalid: $OPTARG requires an argument" >&2
      ;;
  esac
done

# remove options that have already been handled from $@
shift $((OPTIND -1))