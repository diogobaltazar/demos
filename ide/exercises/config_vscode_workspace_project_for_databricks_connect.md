vs code extensions (Ctrl+P):
+ ext install paiqo.databricks-vscode
+ ext install ms-python.python

Create conda environment with python versio nmatching the cluster runtime version:

```conda create --name databricks_connect.python_env python=3.5```

crt `workspace/project/.vscode/settings.json` with:

```json
{
    "python.linting.enabled": false,
    "python.pythonPath": "/home/diogo/anaconda3/envs/databricks_connect.python_env/bin/python"
}
```
thus associating the created environment to the project. 

Edit visual studio config file `~/.config/Code/User/settings.json` with:

```json
{
    "editor.fontSize": 12,
    "editor.detectIndentation": false,
    "window.zoomLevel": 0,
    "git.autofetch": true,
    "git.confirmSync": false,
    "python.linting.enabled": false,
    "python.venvPath": "/usr/local/lib/python2.7/dist-packages/pyspark/jars"
}
```
where `python.venvPath = /usr/local/lib/python2.7/dist-packages/pyspark/jars` was obtained with `$ databricks-connect get-jar-dir`.