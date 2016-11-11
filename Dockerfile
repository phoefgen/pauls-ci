# Creates a container that turns lights on and off!

FROM python
ENV project_root /home/root/undarked

# Install OS packages.
RUN  \
    apt-get update &&\
    apt-get install virtualenv bash -y

# Create venv
RUN \
    mkdir -p $project_root &&\
    mkdir $project_root/app &&\
    virtualenv $project_root/venv &&\
    chmod +x $project_root/venv/bin/* &&\
    . $project_root/venv/bin/activate &&\
    pip install beautifulhue


CMD ["/bin/bash", "-c", "source $project_root/venv/bin/activate && $project_root/app/start.py "]
