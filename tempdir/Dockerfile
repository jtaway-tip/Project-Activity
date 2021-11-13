FROM python
RUN pip install flask
RUN pip install requests
COPY  ./static /home/myapp/static/
COPY  ./templates /home/myapp/templates/
COPY  ip_api.py /home/myapp/
EXPOSE 5000
CMD python3 /home/myapp/ip_api.py
