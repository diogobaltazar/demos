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

Clone the repo locally: