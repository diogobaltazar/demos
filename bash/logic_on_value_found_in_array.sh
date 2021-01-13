D=('a' 'b')
args=("$@")

for d in "${D[@]}"; do
    if [[ " ${args[@]} " =~ " ${d} " ]]; then
        echo OK # whatever you want to do when array contains value
    fi
    echo $d
done

# run: 
# . logic_on_value_found_in_array.sh a