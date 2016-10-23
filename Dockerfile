FROM python:3-onbuild
ENV FLASK_APP /usr/src/app/run.py
CMD [ "python", "./run.py" ]
