FROM python
COPY work.py /
ENTRYPOINT ["/usr/bin/python3", "/work.py"]