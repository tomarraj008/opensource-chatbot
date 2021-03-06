FROM python:3.6-slim

ENV RASA_NLU_DOCKER="YES" \
    RASA_NLU_HOME=/app \
    RASA_NLU_PYTHON_PACKAGES=/usr/local/lib/python3.6/dist-packages

# Run updates, install basics and cleanup
# - build-essential: Compile specific dependencies
# - git-core: Checkout git repos
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends build-essential git-core openssl libssl-dev libffi6 libffi-dev curl  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR ${RASA_NLU_HOME}

# use bash always
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

COPY . ${RASA_NLU_HOME}

RUN pip install -r alt_requirements/requirements_full.txt

RUN pip install -e .

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends wget \
    && wget -P data/ https://s3-eu-west-1.amazonaws.com/mitie/total_word_feature_extractor.dat \
    && apt-get remove -y wget \
    && apt-get autoremove -y

COPY sample_configs/config_spacy_duckling.yml ${RASA_NLU_HOME}/config.yml

#VOLUME ["/app/projects", "/app/logs", "/app/data"]

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]
CMD ["start", "--path", "app/models/nlu", "-c", "app/config/config_tensorflow.yml"]
