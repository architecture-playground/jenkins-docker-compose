**Install ngrok**
=================
At first you need to download ngrok:

`$ wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip`

After that unzip downloaded archive:

`$ unzip /path/to/ngrok.zip`

Connect to your account. Visit the dashboard to <https://dashboard.ngrok.com/auth>

`$ ./ngrok authtoken <YOUR_AUTH_TOKEN>`

To run jenkins-docker-compose write the following command:

`docker-compose up -d --build`

Jenkins will start at <http://localhost:8080>

To start a HTTP tunnel on port 8080, run the following:

`./ngrok http 8080`
 
 As a result you will see 2 links *http* and *https*
 
 
