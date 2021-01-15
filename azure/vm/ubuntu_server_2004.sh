###############################################################################
#
#   Basics
#
###############################################################################
subscription=$SUBSCRIPTION
resource_group=$DEV_RG
name='ubuntu2004'
region='East US'
availability_options='No infrastructure redundancy required'
image='Ubuntu Server 20.04 LTS Gen1'
size='Standard D2s v3 (2 vcpus, 8 GiB memory)'
authentication_type='SSH public key'
username=$UBUNTU2004_USR
keypair_name=$UBUNTU2004_KEYPAIR
public_inbound_ports='SSH'
azure_spot='No Disks'
os_disk_type='Standard SSD'
use_managed_disks='Yes'
encryption_type='Encryption at-rest with a platform-managed key'
use_ephemeral_os_disk='No'
###############################################################################
#
#   Virtual Network
#
###############################################################################
virtual_network=$DEV_VNET
subnet='10.0.0.0/24'
public_ip='ubuntu2004-ip'
ip=$UBUNTU2004_IP
accelerated_networking='Off'
nic_network_security_group='Basic'
public_inbound_ports='Allow selected ports'
selected_inbound_ports='SSH (22)'
accelerated_network='Off'
load_balancing='No'
###############################################################################
#
#   Management
#
###############################################################################
diagnostics_storage_account='devrgdiag185'
###############################################################################
#
#   SSH
#
#   Save private key to cred/ and `$ chmod 400 cred/ubuntu2004_key.pem`.
#   Update user password (ui)
#   Connect with ssh -i cred/ubuntu2004_key.pem $UBUNTU2004_USR@IP
#   and login with the updated password. 
#
#   Nodejs Server Network Protocol and DNS
#
#   https://docs.microsoft.com/en-us/azure-stack/user/azure-stack-dev-start-howto-deploy-linux?view=azs-2002
###############################################################################


