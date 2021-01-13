```
cd parent_repo/path
git add submodule child_repo_url
```

adding to parent_repo/.gitmodules

```
[submodule "parent_repo/path"]
        path = parent_repo/path
        url = child_repo_url
```

commiting changes on parent_repo:

`git add .; git commit -m "add submodule"; git push`

perform changes on child_repo, commit them on child_repo, and then commit it also on parent_repo