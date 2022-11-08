Reddit Scraper

This works with python version 3.9 and only python 3.9. You can view the download versions for Python at https://www.python.org/downloads/. 

Next thing is to install dependencies. Run these commands after navigating to your development folder:

```
pip install pipenv

pipenv shell

pipenv install --dev
```

You're not ready to run the program yet. There's a few more steps.

Create a keys.py file. This stores all of your important account information. If this gets compromised by a bad actor, your reddit account is at steak. I've created a git ignore exception so it will not be uploaded, but that can only do so much.

The general template is this:

```
username = "" # Reddit Username
password = "" # Reddit Password
client_id = "" # Reddit application Client ID
client_secret = "" # Reddit application Client Secret
```

Follow [this guide](https://www.geeksforgeeks.org/how-to-get-client_id-and-client_secret-for-python-reddit-api-registration/) for a quick tutorial on how to find your client ID and client secret.

----

# Running the Application

I've split the application up into 3 distinct parts. 

1) The Initializer: This gets the up to 1000 posts made in the last month. This is the part that requires that client ID and secret

2) The Runner: This uses Selenium (A brower automation tool) to scour the new.reddit links and get the information. This is required because Reddit is a jerk and hasn't updated their API information anywhere with things exclusive to new reddit. This is why 3rd party applications *literally cannot* use new reddit and why a huge protest from the dev community even exists.

3) The Output: This converts the CSV that results from the runner into an excel file.

In order to run these applications, there's 3 commands you can do. The order listed corresponds to which step needs to be done in which order.

`pipenv run init`

`pipenv run start` <-- This part takes a few hours

`pipenv run out`

To make things simple, I've created another with `pipenv run all` which runs them all in the order they need to be run. Just know that if it fails, it's a little bit like losing a needle in a heystack. You will never know where it will be and it will be hard to find. I highly recommend running them one at a time and checking on the middle step every 10 or so minutes to ensure there's little wasted time.