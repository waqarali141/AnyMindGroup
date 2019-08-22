# AnyMind Group Home Assignment 

A coding exercise to evaluate my technical skills

## Getting Started

This project is built using "Python 3.6.5". It uses twitter api to query data from the twitter and uses Twitter APP's Consumer Key and Secret to work. So make sure you've your secrete keys before you jump into running this code.
Flask is used to create EndPoints to access the twitter data.

### Installing/Instruction to SetUp the Enviroment
* Clone the Repo to your local system
* Make sure you've python 3 or any version of python 3x installed
* jump inside the cloned directory.
* All the requirements and dependencies to run this project are listed in requirements.txt
* Before you install the dependencies it is preffered to create a VirtualEnviroment to keep the dependencies clean.
* Once you've created and activated the virtualenv, run this command.
*  ```**pip install -r requirements.txt**```
*  It should setup all the dependencies and requirememts to run this code

### Pre-requisites:
Before running the application make sure you've added your Twitter Cosnumer Key and Consumer Secret to the [**twitterwrapper.py**](https://github.com/waqarali141/AnyMindGroup/blob/master/twitterwrapper.py) 
```
14. # Add your credentials from twitter developer account to make API calls to Twitter API
15. CONSUMER_KEY = "Your's App Consumer Key"
16. CONSUMER_SECRET = "Your's App Consumer Secret"
```

### Running the Flask APP:
Once you've installed the requirements and completed all the pre-requisites. Make sure you're in the Project directory. 
Run the following command to start the Flask WebAPI.

```
python app.py
```

It'll start a local server on the port 8080

Navigate to [Swagger-ui](http://localhost:8080/ui/) you'll find the API documentation there.

You can also check and test the EndPoints using this UI.

