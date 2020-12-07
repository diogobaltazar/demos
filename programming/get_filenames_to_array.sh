# The nullglob option causes the array to be empty if there are no matches
shopt -s nullglob

files=(*)
length="${#files[@]}"
for ((index = 0; index < "$length"; index++ )); do
    echo -e "\t${files[index]}"
done