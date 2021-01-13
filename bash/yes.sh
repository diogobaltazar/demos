# yes
yes

# no 
yes n

# value
yes value

# example
echo 'rm -ri tmp' > remove
mkdir tmp
touch tmp/tmp
yes | . remove
# output:
# rm: descend into directory 'tmp'? rm: remove regular empty file 'tmp/tmp'? rm: remove directory 'tmp'?