

for arg in "$@"; do

    KEY=$(echo $ARGUMENT | cut -f1 -d=)
    VALUE=$(echo $ARGUMENT | cut -f2 -d=)   

    case "$KEY" in
        datalake)
            arg1=${VALUE}
            ;;
        arg2)
            arg2=${VALUE}
            ;;     
        *) ;;
    esac    


done

echo "arg1 = $arg1"
echo "arg2 = $arg2"