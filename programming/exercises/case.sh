# . for.sh
for file in *; do
    echo 'shell scripts:'
    case "$file" in
        *.sh)
            echo -e "\t$file"
            ;;
        *)
            # default
            ;;

    esac
done