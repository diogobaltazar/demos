see system
```bash
/ $ cat /etc/os-release
NAME="Red Hat Enterprise Linux Server"
VERSION="7.5 (Maipo)"
ID="rhel"
ID_LIKE="fedora"
VARIANT="Server"
VARIANT_ID="server"
VERSION_ID="7.5"
PRETTY_NAME="Red Hat Enterprise Linux Server 7.5 (Maipo)"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:redhat:enterprise_linux:7.5:GA:server"
HOME_URL="https://www.redhat.com/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
```
```bash
/ $ uname -a
Linux <name> 3.10.0-862.6.3.el7.x86_64 #1 SMP Fri Jun 15 17:57:37 EDT 2018 x86_64 x86_64 x86_64 GNU/Linux
```
get params
```bash
usage {
    echo "run: ./sc.sh -v <v> -j <j> -h <h>"
}

while getopts v:j:h:name; do
        case $name in
                v) export Vertical=$OPTARG;
                ;; 
                j) export JobName=$OPTARG;
                ;;
                h) export HostName=$OPTARG;
                ;;
                \?) usage
                return 1
                ;;
        esac
done
```
get pid/ppid
```bash
echo $$
```