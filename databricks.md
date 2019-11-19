**dbutils.notebook**  
executing notebook 
```sql
%run "/Users/admdpm021@crb.apmoller.net/idd/logic/raw/testing-notebook-run"
```
[**notebook workflows**](https://docs.databricks.com/notebooks/notebook-workflows.html)  
You implement notebook workflows with dbutils.notebook methods. These methods, like all of the dbutils APIs, are available only in Scala and Python. Long-running notebook workflow jobs that take **more than 48 hours** to complete are not supported.

**api.notebook.dbutils**  
Run exit to terminate the notebook successfuly. If you want to cause the job to fail, throw an exception.
```python
dbutils.notebook.exit("\<return-value>")  
```
```python
res = dbutils.notebook.run('\<notebook-rel-path>', 60, {'\<arg-1>': '\<arg-value-1>'})  
```
**Run multiple notebooks concurrently**  
You can run multiple notebooks at the same time by using standard Scala and Python constructs such as Threads (Scala, Python) and Futures (Scala, Python). The advanced notebook workflow notebooks demonstrate how to use these constructs. The notebooks are in Scala but you could easily write the equivalent in Python.
------
[d1](https://www.youtube.com/watch?v=17ozSeGw-fY&list=RDEMsud_-7pX82wtQUsO_FrP9A&index=2)  
[d2](https://www.youtube.com/watch?v=6ACl8s_tBzE&list=RDEMsud_-7pX82wtQUsO_FrP9A&index=11)
[d3](https://www.youtube.com/watch?v=8FOBxcluXdk&list=RDEMsud_-7pX82wtQUsO_FrP9A&index=13)
[d4](https://www.youtube.com/watch?v=X930_IyhGfo)
[d5](https://www.youtube.com/watch?v=8FOBxcluXdk&list=RDEMsud_-7pX82wtQUsO_FrP9A&index=11)
[d6](https://www.youtube.com/watch?v=0-7IHOXkiV8)