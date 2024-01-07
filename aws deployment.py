Carte
4227960022878486

# je vais pusher dans le github
reponame="Projet7_final"
git init
git add .
git commit -m "Projet Final"
git remote remove origin 
git remote add origin https://github.com/bouramayaya/$reponame.git
git push -u origin master


api    :   http://212.47.246.218:8001/
dashboard: http://212.47.246.218:8080/

git config --global user.name "Bourama FANE"
git config --global user.email "bouramayaya@gmail.com"

git config --global --get user.name
git config --global --get user.email

sudo apt-get update
sudo apt install python3 python3-pip
sudo apt install git

# Creation de l'environement virtuel et activation.
sudo apt install python3.10-venv
# sudo python3 -m venv env; source env/bin/activate
sudo python3 -m pip install --upgrade pip


sudo git clone https://github.com/bouramayaya/Projet7_final.git
ls
cd Projet7_final/
sudo pip3 install -r requirements.txt

# deploiement
screen -S api
screen -ls
screen -r api
python3 -m uvicorn api:app --host 0.0.0.0 --port 8000
python3 -m uvicorn api:app --host 127.0.0.1 --port 8001
# ctrl A D pour quitter le screen sans arreter. 

screen -S dashboard
# Pour le Dashboard
gunicorn dashboard7_deployed:server --bind=127.0.0.1:8080
gunicorn dashboard7_deployed:server --bind=0.0.0.0:8080







000-default-le-ssl


api_url:   http://54.172.177.114:8000/
dash_url: http://107.23.194.67:8080/



# Pythonanywhere
------------------------------------------------------------------------------
https://www.youtube.com/watch?v=6p7GBfHgJq8
https://www.youtube.com/watch?v=JiA-8oVgPIM
https://www.youtube.com/watch?v=chHyH3cCM7k
apifane: Fanepythonanywhere1





# User Data Script (EC2 Instance Setup):

#!/bin/bash
apt-get update -y
sudo apt install -y python3 python3-pip
apt-get install -y apache2

# Il faut attendre au minimum 5 min (2 Checks passed)
# After Connecting to EC2:

# Creer un record dans Route 53 avec un nom de domaine
# puis, 
# Add the public IP (ici: 18.207.167.40) to your DNS (test record)

# Ensuite, tu reviens dans la console:
sudo sudo
clear


# Install Certbot and configure SSL:

sudo apt install certbot python3-certbot-apache
sudo certbot --apache -d fane-api.com
(Note: Ensure your domain has an A-record in DNS to avoid errors.)

Modify the Apache configuration:

Navigate to the sites available directory:

cd /etc/apache2/sites-available/
Edit the SSL configuration file:

vi 000-default-le-ssl.conf
Add these lines to enable proxying:

ProxyPass / http://127.0.0.1:8000/
ProxyPassReverse / http://127.0.0.1:8000/

Enable Proxy Modules:
sudo a2enmod proxy
sudo a2enmod proxy_http

Restart Apache:
sudo systemctl restart apache2


Running FastAPI in the Background:

Install FastAPI and Uvicorn:

pip3 install fastapi uvicorn["standard"]
pip3 install shap==0.43.0  requests==2.31.0 joblib==1.3.2 lightgbm==4.1.0 
pip3 install scikit-learn==1.3.1 scipy==1.11.3 seaborn==0.13.0 matplotlib==3.8.0 numpy==1.24.4 pandas==2.1.1 
pip3 install pickle io


sudo pip3 install dash pandas==2.1.1
sudo pip3 install pandas==2.1.1

# sudo apt remove python3-fastapi python3-uvicorn  python3-joblib python3-lightgbm
# sudo apt remove python3-matplotlib python3-numpy python3-pandas python3-requests
# sudo apt remove scikit-learn scipy seaborn shap guvicorn

# Run FastAPI in the background:
nohup uvicorn api:app --host 127.0.0.1 --port 8000 
nohup uvicorn api:app --host 0.0.0.0 --port 8000 

Sample FastAPI Code:

python

from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

    
Get ready to elevate your FastAPI application with unparalleled performance and security! Subscribe for more insightful tech tutorials and stay ahead in the game.
