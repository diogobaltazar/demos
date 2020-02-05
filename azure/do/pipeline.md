**pipeline**
+ create pipeline associating with:
    + `<ado-repo-name>-ADB`
    + initializing a new `<ado-pipeline-build-df> = azure-pipelines.yml`
+ run build by clicking *Queue*, which will build the last repo commit
+ the build progress can be tracked in
    + logs
    + summary
    + tests
**custom-build-variable**
**secret-variable**
**environment-variable**

**build-agent**
select settings from the `<ado-organization>` and go to `<ado-build-agent-pools>`
build triggers call build-agents from the build-agents-pool.  

following [src](https://azuredevopslabs.com//labs/azuredevops/yaml/)

create web app + sql:
+ `<web-app-sql> = webappsqldpm`
+ `<subscription> = TODO`
+ `<resource-group> = TODO`
+ `<app-service-group> = TODO`
+ `<sql-database> = dbwebappsqldpm`
+ `<server.sql-database> = serverdbwebappsqldpm`
+ `<usr.server.sql-database> = dba`
+ `<pwd.server.sql-database> = P4ssw.rd`
+ `<region.server.sql-database> = West Europe`
+ `<pricing-tier.sql-database> = TODO`  
Pause existing pipeline and create new pipeline:
+ `<code-repo.ado-pipeline> = Azure Repos Git YAML`
+ `<yaml.ado-pipeline> = Azure Repos Git YAML`
```yaml
# ASP.NET
# Build and test ASP.NET projects.
# Add steps that publish symbols, save build artifacts, deploy, and more:
# https://docs.microsoft.com/azure/devops/pipelines/apps/aspnet/build-aspnet-4

trigger:
- master

pool:
  vmImage: 'windows-latest'

variables:
  solution: '**/*.sln'
  buildPlatform: 'Any CPU'
  buildConfiguration: 'Release'

steps:
- task: NuGetToolInstaller@1

- task: NuGetCommand@2
  inputs:
    restoreSolution: '$(solution)'

- task: VSBuild@1
  inputs:
    solution: '$(solution)'
    msbuildArgs: '/p:DeployOnBuild=true /p:WebPublishMethod=Package /p:PackageAsSingleFile=true /p:SkipInvalidConfigurations=true /p:PackageLocation="$(build.artifactStagingDirectory)"'
    platform: '$(buildPlatform)'
    configuration: '$(buildConfiguration)'

- task: VSTest@2
  inputs:
    platform: '$(buildPlatform)'
    configuration: '$(buildConfiguration)'

```
