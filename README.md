**Install ngrok**
=================
At first you need download ngrok:

`$ wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip`

Then Unzip to install:

`$ unzip /path/to/ngrok.zip`

Connect your account. Visit the dashboard to <https://dashboard.ngrok.com/auth>

`$ ./ngrok authtoken <YOUR_AUTH_TOKEN>`

To run jenkins-docker-compose write comand:

`docker-compose up -d --build`

Jenkins will start at <http://localhost:8080>

To start a HTTP tunnel on port 8080, run this next:

`./ngrok http 8080`
 
 Then we will see 2 link *http* and *https*
 
 
