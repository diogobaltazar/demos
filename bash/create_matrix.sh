M=("C1" "C2" "C3")
C1=("1.1" "1.2" "1.3")
C2=("2.1" "2.2" "2.3")
C3=("3.1" "3.2" "3.3" )

for i in ${Matrix[@]}; do
    echo $(eval echo "\${$i[0]}")
    echo $(eval echo "\${$i[1]}")
    echo $(eval echo "\${$i[2]}")
done