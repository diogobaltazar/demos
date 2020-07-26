+ crt repo with master branching to collaboration branch (`develop`) branching to a feature branch (`feature`)
+ sync ADF to the `repo` and specify the collaboration branch `develop` and the current branch `feature`
+ go to `manage / connections / linked services`
+ crt linked service to key vault (`KLS`) specifying the ssubscription and the keyvault
+ databricks workspace / user settings / `TOKEN` = crt new token
+ save `TOKEN` as `token` to key vault
+ edit keyvault `Access Policies` and create a new one for the data factory `appid` with all Key and Secret permissions. The `appid` can also be found by testing the connection (`test connection`) from data factory to databricks. The `appid` will be in the err message: `Caller was not found on any access policy in this key vault`.
+ crt linked service to databricks specifying
    + subscription
    + databricks workspace
    + authentication through keyvault:
        + `KLS`
        + `token`
    + `existing interactive cluster / cluster id` = `0703-060921-emery775`
    + `test connection`
    + `save`