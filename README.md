# **HCI - Quiz 2 (Backend)**

## Members :

- Kenneth Sebastian	        - 1313621004
- Krisna Humanis            - 1313621015	
- Muhammad Faris Heruputra  - 1313621014
- Roland Roman Topuh        - 1313621026

## **Documentation**

Preview of each Data Type in the Database<br>
![alt text](https://user-images.githubusercontent.com/71580615/203736983-4aa22967-88fb-4765-b2e5-f60050d76be7.jpg)  

[POST] Pond Registration
<http://127.0.0.1:5000/api/v1/registrasi>
![alt text](https://user-images.githubusercontent.com/71580615/203738014-0e72440f-593a-41fd-a4a6-e008fc580b04.jpg)  

[GET] Get the List of All Ponds
http://127.0.0.1:5000/api/v1/pondinfo/<pondname>  
![alt text](https://user-images.githubusercontent.com/71580615/203737948-0c5534ef-30f6-468b-b688-62d4a729583e.jpg)
  
[PUT] Update Pond Data
http://127.0.0.1:5000/api/v1/pondinfo/<pondname>  
![alt text](https://user-images.githubusercontent.com/71580615/203737970-21010e81-1360-4062-842a-58515ab8d699.jpeg)

[GET] Get Pond Info Based on its Name
http://127.0.0.1:5000/api/v1/pondinfo/<pondname>  
![alt text](https://user-images.githubusercontent.com/71580615/203740106-f0d3a410-6570-4391-90a1-b09368eeff00.jpg)

## Setup Guide

Create a python virtual environment using:
```
python -m venv <virtual environment name>
```

then activate the virtual environment<br>
Windows:
```
<virtual environment name>\Scripts\activate
```
Linux:
```
./<virtual environment name>/bin/activate
```

After that you could install the required modules from file named `requirements.txt`
```
pip install -r "requirements.txt"
```
