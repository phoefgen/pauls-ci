# pauls-ci - DevOps in a Repo. 

### A reusable, portable Continous Integration enviornment.
[![Build Status](https://travis-ci.org/phoefgen/pauls-ci.svg?branch=master)](https://travis-ci.org/phoefgen/pauls-ci) [Latest Build Logs](https://travis-ci.org/phoefgen/pauls-ci) 

A platform for mindfully generating modern, scalable, supportable open 
source code projects. 

The goal of this project is to enable a method that allows 
developers to quickly start a project, and apply current best practise.

The template will evolve with best practise over time, however the goal
is to create a structure that _only_ works with high quality code 
practise.  

This project is designed to encourage the following concepts:

#### Currently Supports:
- Automated Testing and TDD.
- Continuous, Automated code Integration.
- [PEP-8 coding standards.](https://www.python.org/dev/peps/pep-0008/) checks.
- A portable and repeatable test, staging and deployment environment 
through [Docker](https://www.docker.com)
- Code management and versioning through [git-flow](http://nvie.com/posts/a-successful-git-branching-model/).
- Agile development practise through [Kanban](https://www.atlassian.com/agile/kanban) task tracking.
- Scheduling local and testing deployment with [docker-compose](https://docs.docker.com/compose/).
 
#### On Roadmap:
- Continuous deployment via automated Blue/Green releases.
- Multi-Vendor deployment through containers 
(GoogleCloud/AWS/local/Custom)
- Multiple CI vendor integration (TravisCI supported, Jenkins support
 planned)
- Support for Scrum Agile workflows.
- Supporting structures to aid local development:
    - ELK Log monitoring (deployed to local containerized ELK stack)
    - Metrics (Deployed to local container: Graphite)
    - Monitoring (Deployed to local conatiner: Sensu)
    - Automated transformation from local dev endpoints to production 
    endpoints. 

- Fail builds based on lowscore in pylint, excessive duplication in 
code, etc.

## Using pauls-ci:

### Requirements
The following is required to support the testing environment.

1. A working [docker installation](https://www.docker.com/products/overview#/install_the_platform), including docker-compose.
 
Thats it! Docker installs all the other dependencies automatically. 

### Workflow

Build out your project in the `./app/` directory. Write corresponding 
tests in the `./test/` directory.

`docker-compose run` will start the docker container and (by Default) 
run `start.py`

TODO: Add configuration injection architecture. 

### Setup 

1. Fork and clone the repo. 
3. Configure [TravisCI](https://docs.travis-ci.com/user/getting-started/) to monitor the deploy and master branches

### Feature development

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

### Releases

1. Move all the new features into staging with 
`git flow release start $ver`
2. Make any modifications required (setting version string etc)
3. Finish release with `git flow release finish $ver`

This pulls the repo, and pushes the code from the release branch into 
both the develop and master branches. It also tags the commit to master
with the release `$ver` name. This also triggers a final CI check on 
Travis. 

### HotFix releases

1. On report of a new issue, create a minor break-fix change with:
`git flow hotfix start $issue_id-$issue_description`
1. Write a new test for the missed edge case.
2. Fix the code on the hotfix branch, run local tests with `make all`
1. Change version strings where appropriate. 
1. Once test is passing:
 `git flow hotfix finish $issue_id-$issue_description`
 
This will trigger a re-run of the TravisCI checks, and tag the new 
release in github. 