sudo echo '
. /home/$(whoami)/core.cmc/core $@
' > /usr/local/bin/nnc
sudo chmod 655 /usr/local/bin/nnc
