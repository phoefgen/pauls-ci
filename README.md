# pauls-ci

### A reusable, portable Continous Integration enviornment.
[![Build Status](https://travis-ci.org/phoefgen/pauls-ci.svg?branch=master)](https://travis-ci.org/phoefgen/pauls-ci)


A platform for mindfully generating modern, scalable, supportable code 
(probably in python). 

The overall goal of this project is to enable a method that allows 
developers to quickly start a project, and apply current best practise.
The template will evolve with best practise over time, however the goal
is to create a structure that only works with great code. 

This project is designed to encourage the following concepts:

#### Currently Supports:
- Automated Testing and TDD.
- Continuous, Automated code Integration.
- PEP-8 enforcement and coding standards.
- A portable and repeatable test, staging and deployment environment 
through Docker.
- Code management and versioning through git-flow.
- Agile development practise through Kanban task tracking.
- Scheduling local and testing deployment with docker-compose.
 
#### On Roadmap:
- Continuous deployment.
- Multi-Vendor deployment through containers 
(GoogleCloud/AWS/local/Custom)
- Automated Blue/Green release management.
- Multiple CI vendor integration (TravisCI supported, Jenkins support 
planned)
- Out of the box ELK Log monitoring (deployed to local ELK stack)
- Out of the box Metrics (graphite)
- Out of the box Monitoring (Sensu)


## Using pauls-ci:

### Setup 

1. Fork and clone the repo. 
3. Configure TravisCI to monitor the deploy and master branches

### Building new stuff! (Feature development)

3. Use git-flow to create a feature branch: 
`git flow feature start $feature_name`
4. Write tests that define  the new feature branch in
 `test/test_$file.py` (one file per python file) 
5. Run `make all`, it will fail if your tests are written correctly.
6. Modify `$file` in the app folder until the `make all` tests pass.
7. __(Optional)__ push the feature branch to github: 
`git push origin feature/$feature_name`
8. Complete feature development, merge into `develop` branch with:
 `git flow feature finish feature/$feature_name`
9. Remove remote __(Optional)__ feature branch with 
`git push origin --delete feature/$feature_name`
10. Check the automated testing in TravisCI is still passing. Rollback 
or Roll Forward as appropriate to clear the TravisCI checks. 

### Launching new stuff! (Releases!)

1. Move all the new features into staging with 
`git flow release start $ver`
2. Make any modifications required (setting version string etc)
3. Finish release with `git flow release finish $ver`

This pulls the repo, and pushes the code from the release branch into 
both the develop and master branches. It also tags the commit to master
with the release `$ver` name. This also triggers a final CI check on 
Travis. 

### Whoopsfix (HotFix releases)

1. On report of a new issue, create a minor break-fix change with:
`git flow hotfix start $issue_id-$issue_description`
1. Write a new test for the missed edge case.
2. Fix the code on the hotfix branch, run local tests with `make all`
1. Change version strings where appropriate. 
1. Once test is passing:
 `git flow hotfix finish $issue_id-$issue_description`
 
This will trigger a re-run of the TravisCI checks, and tag the new 
release in github. 