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
