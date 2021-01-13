move data from teradata to adls  
create new pipeline
+ `<name.pipeline.adf> = inlandDailyDriver_InlandUSD`
+ `<branch.vc.pipeline.adf> = dev`
+ `<name.adls.connection.adf> = TODO`
+ `<integration-runtime.adls.connection.adf> = TODO` \*
+ `<integration-runtime.adls.connection.adf> = TODO`
+ `<account-uri.adls.connection.adf> = adl://dlsazewsmlitdatalake001.azuredatalakestore.net/`
+ `<subscription-id.adls.connection.adf> = TODO`
+ `<resource-group.adls.connection.adf> = rgpazewpmlitdatalakes001`
+ `<tenant.adls.connection.adf> = TODO`
+ `<authentication-type.adls.connection.adf> = Service Principal`
+ `<sp-id.adls.connection.adf> = TODO`
+ `<akv-linked-service.adls.connection.adf> = inlandDailyDriverKV`
+ `<sp-secret-key.adls.connection.adf> = sp-inland-daily-driver-TODO`
+ `<name.td.connection.adf> = ls_inlandDailyDriver_td`
+ `<integration-runtime.td.connection.adf> = TODO`
+ `<integration-runtime.td.connection.adf> = TODO`
+ `<account-uri.td.connection.adf> = adl://dlsazewsmlitdatalake001.azuredatalakestore.net/`
+ `<subscription-id.td.connection.adf> = TODO`
+ `<resource-group.td.connection.adf> = rgpazewpmlitdatalakes001`
+ `<tenant.td.connection.adf> = TODO`
+ `<authentication-type.td.connection.adf> = Service Principal`
+ `<sp-id.td.connection.adf> = TODO`
+ `<akv-linked-service.td.connection.adf> = inlandDailyDriverKV`
+ `<sp-secret-key.td.connection.adf> = sp-inland-daily-driver-TODO`
+ `<src.dataset.adf> = TODO`
+ `<dest.dataset.adf> = TODO`


\* request engineering integration runtime creation to infrastructure team

