# Creating an Azure Key Vault-backed secret scope is supported only in
# the Azure Databricks UI. You cannot create a scope using the Secrets
# CLI or API.

# RESUME: crt secret in keyvault with blob acces key, link the keyvault
# to a databricks backed scope, mount by retrieving the secret value by
# # specifiny the backed svope and the secret name 

# crt blob storage account
# NAME_BLOB_STORAGE_ACCOUNT = name.blob.storage_account
# NAME_CONTAINER_BLOB_STORAGE_ACCOUNT =
# name.container.blob.storage_account

# crt key vault service
# KEY_VAULT_NAME = name.kv
# DATABRICKS_PRODUCT_SCOPE = NAME_PRODUCT.intermodal.adbazewtcommbi
# KEY_VAULT_DNS = 'https://%s.vault.azure.net/' %(KEY_VAULT_NAME)
# KEY_VAULT_SUBSCRIPTION_ID = subscription_id.kv
# KEY_VAULT_RESOURCE_GROUP = rg.kv
# KEY_VAULT_RESOURCE_ID = '/subscriptions/%s/resourceGroups/%s/
# providers/Microsoft.KeyVault/vaults/%s' %(KEY_VAULT_SUBSCRIPTION_ID,
# KEY_VAULT_RESOURCE_GROUP, KEY_VAULT_NAME)
# create a secret in the keyvault to mount the blob to the databricks
# file system, the value of the secret key is the access key of the blob
# found on blob/Access Keys/key1

# create databricks secret scope: https://<region>.azuredatabricks.net/
# ?o=<id.organization>#secrets/createScope#secrets/createScope
# DATABRICKS_BACKED_SCOPE_NAME = <product>.backed_scope.databricks
# DATABRICKS_BACKED_SCOPE_KEY_VAULT_DNS = KEY_VAULT_DNS
# DATABRICKS_BACKED_SCOPE_KEY_VAULT_ID = KEY_VAULT_RESOURCE_ID
# SECRET_BACKED_SCOPE_DATABRICKS =
# SECRET_BACKED_SCOPE_DATABRICKS_KEY_VAULT

# create databricks token, copy the token and save it as a secret in the
# keyvault
# SECRET_BACKED_SCOPE_DATABRICKS_KEY_VAULT = secret.backed_scope.db

scope = DATABRICKS_BACKED_SCOPE_NAME

source = 'wasbs://%s@%s.blob.core.windows.net/%s' %(
  NAME_CONTAINER_BLOB_STORAGE_ACCOUNT,
  NAME_BLOB_STORAGE_ACCOUNT,
  NAME_PRODUCT
)
mount_point = '/mnt/commbi_intermodal/%s' % (NAME_PRODUCT)
key = SECRET_BACKED_SCOPE_DATABRICKS

print(
  '  source:\t%s\n  mnt point:\t%s\n  backed scope:\t%s\n  secret key:\t%s\n'
  %(source, mount_point, scope, key)
)

dbutils.fs.mount(
  source = source,
  mount_point = mount_point,
  extra_configs = {
    'fs.azure.account.key.%s.blob.core.windows.net' %(NAME_BLOB_STORAGE_ACCOUNT): dbutils.secrets.get(
      scope = scope,
      key = key
    )
  }
)
