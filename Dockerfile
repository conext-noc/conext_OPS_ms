FROM python:3.10
RUN mkdir -p /home/ms_app
COPY . /home/ms_app
RUN pip install --upgrade pip
RUN echo "net.ipv4.tcp_keepalive_time=3000" >> /etc/sysctl.conf
RUN echo "net.ipv4.tcp_keepalive_intvl=3000" >> /etc/sysctl.conf
RUN echo "net.ipv4.tcp_keepalive_probes=5" >> /etc/sysctl.conf
RUN pip install -r /home/ms_app/requirements.txt
EXPOSE 8000
CMD ["python", "/home/ms_app/manage.py", "runserver", "0.0.0.0:8000"]
