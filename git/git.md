+ git concepts
   + distributed version control:
      + **tracking** the versioning of a file
      + **documenting the versioning** of a file. The versioning can be:
         + paralell (branches)
         + sequential (commits)
      + **reverting between versions**
      + **backup** in a server
      +  team **contribution**
   + branches
      + paralell developping of the 
      + remote
      + local
   + spaces:
      + local workspace: `LW`
      + index/stage `STAGE`
      + local repo: ``LR`` `pull` from ``CR``
      + staging: LR `commit` to staging
      + central repo: staging `push` to CR
We may want to commit different versions from different files in the same commit, *e.g.:* when the changes in those files belong to a single feature. For this purpose, there exists the `STAGE` area, which contains 1 or more file versions.
+ ``my-proj-dir\.gitignore``  
Don't stage:  
    + Log files
    + Files with API keys/secrets, credentials, or sensitive information
    + Useless system files like .DS_Store on macOS
    + Generated files like dist folders
    + Dependencies which can be downloaded from a package manager
    + And there might be other reasons (maybe you make little todo.md files)
create ``LR``
```bash
git init
```
copy/clone `CR`
```bash
git clone <cr-url>
```
associate `LR` to `CR`
```bash
git add origin <cr-url>
```
pull/fetch contents of `CR`
```bash
git pull
```
associate new `LR` to `CR`
```bash
$ mkdir git-demo
$ cd git-demo
git-demo $ git remote add origin <cr-url>
git-demo $ git pull
git-demo $ ls
total 0
git-demo $ git pull
remote: Enumerating objects: <TODO>
remote: Counting objects: <TODO>
remote: Compressing objects: <TODO>
remote: <TODO>
Receiving objects: <TODO>
Resolving deltas: <TODO>
From https://github.com/<git-usr>/<cr>
 * [new branch]        master     -> origin/master
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> master
git-demo $ git pull origin master
From https://github.com/<git-usr>/<cr>
 * branch              master     -> FETCH_HEAD
total 1
<TODO> 1 <usr> <TODO>     <TODO>   <TODO> a/
```
list branches
```bash
$ git branch -a
```
send/commit all staged changes to `LR`
```bash
git commit -m "<commit-msg-for-files-versions>"
```
see commits list
```bash
git log
git log --oneline
```
```bash
```
list config
```bash
git config --list
```
revert to previous commit
```bash
TODO
```
create new branch
```bash
git branch
```
get rid of changes made locally
```bash
git checkout <file-name>
```
multiple .gitignore: the following too are equivalent
```bash
/.gitignore
   a/b 
```
cancel STAGING/changes for file
```bash
git checkout <file-name>
```
add/edit variables of git config
```bash
> git config --global <var-name-1>[.<var-name-1>] <var-value>
```
list variables of git config
```bash
> git config --list
```
fork  
create a new repository `A` from the head of a repository `B`
```bash
git fork <repository-url>
```
hooks  
events triggered in the git server  
[src1](https://www.atlassian.com/git/tutorials/git-hooks)  
+ roadmap
   + branches
   + revert
+ exercises
    1. branch master with `dev`, change ``git.md`` as to cause a merge conflict when merging back the changes to ``master``. Fix the merging, discard `dev` and push to CR.
    1. branch master with `dev`, affect changes, check to master and delete `dev`
    1. change `git.md` from LW2 and push to CR as to provoke a conflict with LR1
    1. what would happen if changes to a file were made in dev, uncommited, and the branch was switched back to master?
        + Nothing. The changes are *made in dev* only if they are committed to dev.