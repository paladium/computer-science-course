# Git version control system
Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. So ideally, we can place any file in the computer on version control.


A Version Control System (VCS) allows you to revert files back to a previous state, revert the entire project back to a previous state, review changes made over time, see who last modified something that might be causing a problem, who introduced an issue and when, and more. Using a VCS also means that if you screw things up or lose files, you can generally recover easily.

Git is a version-control system for tracking changes in computer files and coordinating work on those files among multiple people. Git is a Distributed Version Control System. So Git does not necessarily rely on a central server to store all the versions of a project’s files. Instead, every user “clones” a copy of a repository (a collection of files) and has the full history of the project on their own hard drive. This clone has all of the metadata of the original while the original itself is stored on a self-hosted server or a third party hosting service like GitHub.

Git also helps you synchronise code between multiple people. So imagine you and your friend are collaborating on a project. You both are working on the same project files. Now Git takes those changes you and your friend made independently and merges them to a single “Master” repository. So by using Git you can ensure you both are working on the most recent version of the repository

## Git commands

First you need to set your credentials:
```bash
git config --global user.name "YOUR_USERNAME"
git config --global user.email "im_satoshi@musk.com"
```

Then we can make a new folder:
```bash
mkdir test-project
cd test-project
```
Let's now open the directory in the VsCode and add some files to it. After we have done so, we can now run the command:
```bash
git init
```
Which will initialise the git system in the current directory.
Next, we should add all our changes:
```bash
git add .
git status
git commit -m "Init"
```
We first add all the files, then we check the status of our files and then we commit or add all these changes to our main branch - master.

Now, if we want to push those changes to Github:
```bash
git remote add origin https://github.com/your_username/repo
git push -u origin master
```
This will push your changes to Github, so that other people can see it as well.
