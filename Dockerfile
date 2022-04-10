FROM python:3.7-slim

RUN python -m pip install rasa
RUN pip3 install rasa[spacy] --user
RUN python3 -m spacy download en_core_web_md

WORKDIR /app
COPY . .

RUN rasa train
#Set the user to run, and not as root
USER 1001


# enterpoint for interactive shell
ENTRYPOINT [ "rasa" ]

# command to run when container is called to run
CMD [ "run", "--enable-api", "--port", "8080" ]