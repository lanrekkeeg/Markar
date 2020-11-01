FROM python

WORKDIR usr/src/autograder
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x ./entrypoint.sh
RUN chmod +x wsgi.py
RUN ls
ENTRYPOINT ["/usr/src/autograder/entrypoint.sh"]
CMD []