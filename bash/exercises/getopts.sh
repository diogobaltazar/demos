# nested: https://sookocheff.com/post/bash/parsing-bash-script-arguments-with-shopts/

# OPTIND: the number of options parsed by the last call to getopts
# OPTARG: argument to an option


# reset after each prog call
unset opt OPTARG OPTIND
# f will not be invalid but no routine is associated
# unmapped params are assigned the value '?'
# ^':' disables the default error handling of invalid options
# ':'$ defines that the option has a parameter
while getopts ":a:b:c:dfs" opt; do
  case $opt in
    a)
      echo "-a: $OPTARG" >&2
      ;;
    b)
      echo "-b: $OPTARG" >&2
      ;;
    c) # requires arg
      echo "-c: $OPTARG" >&2
      ;;
    d)
      echo "-d" >&2
      ;;
    s)
      #. getopts_subprocess.sh
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