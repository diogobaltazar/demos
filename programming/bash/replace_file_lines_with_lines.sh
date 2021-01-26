# replacing spaces with new lines on a private key
sed -i 's/ /\n/g' .ssh/key.pem
