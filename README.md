1) Install Docker on your PC or Mac

2) On your PC or Mac, make a local folder 'app'

3) Run command 'cd app'

4) Clone the files in folder 'app'

5) Edit 'app.py' and replace the 'YOUR-OPENAI-API-KEY' with your api key from openai.com

6) Run command 'docker build -t localgpt:v1 .'

7) Run command 'docker run -d -p 8080:5000 localgpt:v1'

8) Open 'http://localhost:8080/chat' in browser
