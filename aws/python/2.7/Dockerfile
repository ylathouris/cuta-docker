FROM ylathouris/cuta:aws-python

# Install Python 2.7
RUN pyenv install 2.7.18
RUN pyenv global 2.7.18
RUN pyenv rehash

# Install pip (package installer)
RUN curl https://bootstrap.pypa.io/get-pip.py | python

# Install poetry (used for package management)
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV POETRY_ROOT $HOME/.poetry
ENV PATH $POETRY_ROOT/bin:$PATH

# Set command prompt
ENV PS1='🐳 \[\033[1;36m\](cuta@\h\[\033[1;36m\]) \[\033[0m\]'
