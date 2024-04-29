#base image
FROM python:3.9

#menentukan working directory
WORKDIR /app

#copy semua file dan folder
COPY . /app

#install dependencies
RUN pip install -r requirements.txt 

#jalankan aplikasi python
CMD ["python", "app.py"]

