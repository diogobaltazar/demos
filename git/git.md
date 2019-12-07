+ ``my-proj-dir\.gitignore``  
Don't stage:  
    + Log files
    + Files with API keys/secrets, credentials, or sensitive information
    + Useless system files like .DS_Store on macOS
    + Generated files like dist folders
    + Dependencies which can be downloaded from a package manager
    + And there might be other reasons (maybe you make little todo.md files)
    
list config
```bash
git config --list
```
revert to previous commit
```bash
git checkout <commit-hash>
git reset <commit-hash>
git checkout <working-branch>
```
