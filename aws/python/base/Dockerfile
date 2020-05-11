FROM amazonlinux:2

# Install build libraries
COPY ./packages.txt packages.txt
RUN yum update -y && \
    yum install -y $(cat packages.txt) && \
    yum clean all && \
    rm packages.txt

# Add non-root user.
RUN adduser cuta
USER cuta

# Set current working directory.
ENV HOME /home/cuta
WORKDIR $HOME

# Install pyenv (used to install/manage python versions)
RUN git clone git://github.com/yyuu/pyenv.git .pyenv
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Label as cuta image.
LABEL io.cuta.name="aws-python"
