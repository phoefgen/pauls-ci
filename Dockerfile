# Creates a container that turns lights on and off!
# This container is used to provide a consistent and portable development
# environment.

FROM python
ENV project_root /home/root/pauls-ci
WORKDIR $project_root

# Install OS packages.
RUN  \
    apt-get update &&\
    apt-get install virtualenv bash -y

# Install base code.
ADD . /$project_root

# Create venv
RUN \
    virtualenv $project_root/venv &&\
    chmod +x $project_root/venv/bin/*
# Install requirements to venv
RUN . $project_root/venv/bin/activate &&\
    pip install -r $project_root/app/requirements.txt


# Start the docker container with an active virtualenv - Protecting the OS
# Python implementation from the project.

CMD ["/bin/bash", "-c", \
        "source $project_root/venv/bin/activate && $project_root/app/start.py "]
