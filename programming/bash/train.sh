curr_dir=${pwd##*/}

if [[ $curr_dir = "demos" ]]; then
   echo ''
else
    echo 'please run script from ~/your-sys-path/demos'
fi

for proj in `ls`; do

    # if the proj is a directory and has a subdirectory
    # /exercises, execute them all
    cd $proj/exercises 2>&1
    if [ $? -eq 0 ]; then
        echo $proj 
        for exercise in `ls`; do
            echo -ne "> practice \e[32m$exercise\e[0m [yes = 0] ########################################################" 

            read ans
            if [ $ans -eq 0 ]; then
                echo -ne "> see solution? [yes = 0]" 

                read ans
                if [ $ans -eq 0 ]; then
                    echo -e "> solution:\n\e[32m`cat $exercise`\e[0m" 
                    #echo -e "> result: `eval $content`"
                fi
            fi
        done
        cd ../..
    fi

done