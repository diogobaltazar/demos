# . get_all_args_as_array.sh print 1 2 three 4
print() {
    for arg in "$@"; do
        echo -e "\t$arg"
    done

    args=( "$@" )
    length="${#args[@]}"
    for ((index = 0; index < "$length"; index++ )); do
        echo -e "\t${args[index]}"
    done
}

"$@"