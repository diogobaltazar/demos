# build
+ create organization `<ado-organization>`
+ create organization project `<ado-project>`
+ create code repository `<ado-repo-name>-ADB`
+ sync databricks notebook `<databricks-workspace-path>/<databricks-project-path>/<databricks-notebook>`:
    + repository url: `<ado-repo-url> = https://dev.azure.com/<ado-organization>/<ado-project>/_git/<ado-repo-name>-ADB`
    + branch: `<az-notebook-sync-branch>` (either `master` or `crt-new-branch`)
    + path in git: `<databricks-project-path>/<databricks-notebook>`
+ In the azure portal, **commit** by:
    + clicking on the notebook *Revision history*
    + *Save now* on the latest staged changes, adding a commit message

Given:
+ the organization `<organization.ado> = org-diogopereiramarques`
+ the project `<project.org.ado>`
+ the repo `<repo.org.ado>`
+ the branch `<dev.branch.repo.org.ado>` branched from `<master.branch.repo.org.ado>`

Clone the repo locally and change to the branch `<dev.branch.repo.org.ado>`. Upload files:
+ ``template.json``
+ ``parameters.json``
+ ``azure-pipeline.yml``
+ ``notebook-run.json.tmp``
+ ``logic/helloworld.py``

where ``azure-pipeline.yml``:
```yml
pool:
  vmImage: 'Ubuntu-16.04'

variables:
- name: NotebookName
  value: helloworld

steps:
- bash: |
    mkdir -p "$(Build.ArtifactStagingDirectory)/arm_template"
    cp parameters.json template.json "$(Build.ArtifactStagingDirectory)/arm_template/"
  displayName: 'Include Azure Resource Manager templates into Build Artifacts'
- bash: |
    mkdir -p "$(Build.ArtifactStagingDirectory)/logic"
    ls -l logic
    cp logic/$(NotebookName).py "$(Build.ArtifactStagingDirectory)/logic/$(NotebookName)-$(Build.SourceVersion).py"
    cp notebook-run.json.tmpl "$(Build.ArtifactStagingDirectory)/logic/notebook-run.json.tmpl"
  displayName: 'Prepare Notebook Build Artifacts'
- task: PublishBuildArtifacts@1
  displayName: Publish ARM Template Build Artifacts
  inputs:
    pathtoPublish: '$(Build.ArtifactStagingDirectory)/arm_template'
    artifactName: arm_template
- task: PublishBuildArtifacts@1
  displayName: Publish Notebook Build Artifacts
  inputs:
    pathtoPublish: '$(Build.ArtifactStagingDirectory)/logic'
    artifactName: notebook
```

Create the build pipeline with:
+ `<build-pipeline.org.ado> = build-pipeline.org.ado` (rename after creation) 
+ `<repo.build-pipeline.org.ado> = <repo.org.ado>` 
+ `<branch.build-pipeline.org.ado> = <dev.branch.repo.org.ado>`
+ `<yml.build-pipeline.org.ado> = /azure-pipeline.yml`   
Choose the branch `<branch.build-pipeline.org.ado>` before running.

Selecting Pipelines/Pipelines, there's a list with the available pipelines. Each item on the list presents the status of the last run of the pipeline and the branch/commit of the pipeline. A pipeline is defined by it's configuration file, *i.e.*, the definition for the sequence of the pipeline steps. Since the file is versioned, running the pipeline is equivalent to running the selected branch and commit for the file. Running a pipeline always takes choosing the branch.

Selecting a pipeline gives access to a historic of the pipeline runs. Selecting a particular run, gives access to the jobs of the run. 

Commiting to the branch will trigger the pipeline automatically (if not specified). Specify the branch that triggers with:
```yml
trigger:
- <branch-name>
```

Check the artifacts created on `ArtifactStagingDirectory` by clicking on `Artifacts`. The directories:
+ `logic`
+ `arm_template`
The artifacts published by each version will be available for deployment in release pipelines. The latest successful build of `<build-pipeline.org.ado>` published the following artifacts: `arm_template`, `logic`.

Create environment variables for all pipelines under `Library`.  

# release
Create the release pipeline `<release-pipeline.org.ado> = release-pipeline.org.ado` and select `Empty job`.
+ `<dev.stage.release-pipeline.org.ado> = dev`
Link the release pipeline to a variable group in the pipeline library by selecting `Variables/Variable groups`, choosing `<dev.stage.release-pipeline.org.ado>` as the group's scope.
Create new `<task.release-pipeline.org.ado>` by clicking `Tasks`:
+ ``<agent-job.task.release-pipeline.org.ado> = agent-job.release-pipeline.org.ado``
Add:
+ ``<az-rg-deployment.task.release-pipeline.org.ado> = Azure resource group deployment``