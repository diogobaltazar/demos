install  
`$ pip3 install databricks-cli`

login (lead to a browser for the login)  
`$ az login`

databricks version  
`$ databricks --version`

configure databricks  
+ generate databricks token (databricks/user settings) `<token.databricks>`
```bash
$ databricks configure --token
Databricks Host (should begin with https://):<az-databricks-host>
Token: <token.databricks>
```


list workspace directories  
`databricks workspace list /Users/<user-name>`

list dbfs directories  
`databricks fs ls /path-here`

list cluster libraries  
`$ databricks libraries list --cluster-id <id.spark-cluster>`

-----

sources  
[medium](https://medium.com/@willvelida/installing-configuring-and-using-the-azure-databricks-cli-5d0381e662a1)