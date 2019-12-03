[Install Azure CLI on Windows](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest)  
[Get started with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/get-started-with-azure-cli?view=azure-cli-latest)  

install az-cli on dos and run `az login` on a dos shell. You are lead to a browser for the login.

### [account]()
list
```bash
az account list --output table
```

### [subscription]()
list
```bash
az group list --output table
```

set active subscription
```bash
az account set --subscription <id.subscription> | <name.subscription>
```

### [dls](https://docs.microsoft.com/en-us/cli/azure/dls/fs?view=azure-cli-latest)
list
```bash
az dls fs list --path
               [--<account>]
               [--<ids>]
               [--<subscription>]
```