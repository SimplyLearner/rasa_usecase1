# rasa_usecase1
```python

# Launch Anaconda Prompt
conda activate rasa
cd rasa-usecase
rasa train

# Initiate the chatbot
rasa shell  #make sure to launch action server in paralell

# Launch Action server
# Launch a new paralell session of anaconda prompt
conda activate rasa
cd rasa-usecase
rasa run actions

# Docker
docker build -t manifoldailearning/rasa-demo .
docker run -it -p 8080:8080 manifoldailearning/rasa-demo

docker run -it manifoldailearning/rasa-demo shell
docker push manifoldailearning/rasa-demo