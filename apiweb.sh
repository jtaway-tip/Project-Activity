#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp ip_api.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile

echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install requests" >> tempdir/Dockerfile
echo "COPY  ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY  ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY  ip_api.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5000" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/ip_api.py" >> tempdir/Dockerfile

cd tempdir

docker build -t apiweb .

docker run -t -d -p 5000:5000 --name apiwebrunning apiweb
docker ps -a
