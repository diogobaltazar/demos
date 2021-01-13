# When you run a command like python or pip, your operating
# system searches through a list of directories to find an
# executable file with that name in those directories. This
# list of directories lives in an environment variable
# called PATH, with each directory in the list separated by
# a colon. Directories in PATH are searched from left to
# right, so a matching executable in a directory at the
# beginning of the list takes precedence over another one
# at the end.
echo $PATH