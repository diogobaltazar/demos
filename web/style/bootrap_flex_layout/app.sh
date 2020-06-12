case $1 in

  install)

    echo "> installing server dependencies"
    npm install
    ;;

  start)

    echo "> compiling less"
    lessc public/css/src/main.less public/css/dist/main.css

    echo "> starting server"
    nodemon --watch app --watch less-watch-compiler
    ;;

  stop)

    echo "> terminating server"
    kill -SIGTERM $(ps -ef | grep nodemon | awk {'print $2'})

    echo "> terminating less-watch-compiler: TODO"
    ;;

  *)
    echo "> run 'start' to start server, 'stop' to stop server"
    ;;
esac
