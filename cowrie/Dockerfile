FROM debian:bullseye-slim as builder

WORKDIR /

# This is a temporary workaround, see https://github.com/cowrie/docker-cowrie/issues/26
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
ENV COWRIE_GROUP=cowrie \
    COWRIE_USER=cowrie \
    COWRIE_HOME=/cowrie

# Set locale to UTF-8
ENV LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

RUN groupadd -r ${COWRIE_GROUP} && \
    useradd -r -d ${COWRIE_HOME} -m -g ${COWRIE_GROUP} ${COWRIE_USER}

# Set up Debian prereqs and install bash
RUN export DEBIAN_FRONTEND=noninteractive; \
    apt-get update && \
    apt-get install -y \
        -o APT::Install-Suggests=false \
        -o APT::Install-Recommends=false \
      python3-pip \
      ca-certificates \
      libffi-dev \
      libssl-dev \
      python3-dev \
      python3-venv \
      python3 \
      rustc \
      cargo \
      git \
      build-essential \
      python3-virtualenv \
      libsnappy-dev \
      iputils-ping \
      nano \
      bash && \
    rm -rf /var/lib/apt/lists/*

USER ${COWRIE_USER}
WORKDIR ${COWRIE_HOME}

# Copy requirements first for efficient caching
RUN mkdir -p ${COWRIE_HOME}/cowrie-git
COPY --chown=${COWRIE_USER}:${COWRIE_GROUP} requirements.txt requirements-output.txt ${COWRIE_HOME}/cowrie-git/

RUN python3 -m venv cowrie-env && \
    . cowrie-env/bin/activate && \
    pip install --no-cache-dir --upgrade pip wheel setuptools && \
    pip install --no-cache-dir --upgrade cffi && \
    pip install --no-cache-dir --upgrade -r ${COWRIE_HOME}/cowrie-git/requirements.txt && \
    pip install --no-cache-dir --upgrade -r ${COWRIE_HOME}/cowrie-git/requirements-output.txt

COPY --chown=${COWRIE_USER}:${COWRIE_GROUP} . ${COWRIE_HOME}/cowrie-git

# Define the volume, user, workdir, path, etc.
VOLUME [ "/cowrie/cowrie-git/var", "/cowrie/cowrie-git/etc" ]
USER ${COWRIE_USER}
WORKDIR ${COWRIE_HOME}/cowrie-git
ENV PATH=${COWRIE_HOME}/cowrie-env/bin:${PATH}
ENV PYTHONPATH=${COWRIE_HOME}/cowrie-git/src
ENV PYTHONUNBUFFERED=1


ENTRYPOINT [ "/cowrie/cowrie-env/bin/python3" ]
CMD [ "/cowrie/cowrie-env/bin/twistd", "-n", "--umask=0022", "--pidfile=", "cowrie" ]

EXPOSE 2222 2223
