FROM ubuntu:16.04
RUN apt-get update
RUN apt-get -y upgrade

#RUN apt-get install python3-setuptools -y
RUN apt-get install python-pip -y
#RUN pip3 -V
#pip 9.0.1 from /usr/local/lib/python3.5/dist-packages/pip-9.0.1-py3.5.egg (python 3.5)

#RUN chown -R username:username ~/.local/
# add to ./*shrc

RUN pip install --upgrade --user awsebcli
ENV PATH="~/.local/bin/:${PATH}"
#RUN eb --version
#EB CLI 3.10.1 (Python 2.7.1)
RUN pip install awscli
RUN apt-get install nano wget -y
WORKDIR /tmp
