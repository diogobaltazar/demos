# . if_then.sh 0
if [ "$1" != "" ]; then
    echo 'not empty str'
    if [ "$1" -ne 0 ]; then
        echo 'not 0'
    fi
fi