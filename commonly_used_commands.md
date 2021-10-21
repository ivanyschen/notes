# Commonly Used Commands

Delete all branches in local except for `master`
```
git branch | grep -v "master" | xargs git branch -D
```
