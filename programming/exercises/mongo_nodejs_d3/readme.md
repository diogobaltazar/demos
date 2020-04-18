## requires
`npm` and npm packages (see `package.json`)

mongodb user:
```json
db.createUser({
  user: "root",
  pwd: "root",
  roles: ['readWrite', 'dbAdmin']
})
```

## node
install dependencies with `npm install`
launch server listenning on `localhost:3000` with `/ > node app` or `/ > nodemon app`