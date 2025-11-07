# GOOGLE FORMS BOT
 CLI Bot that automatically fills out a specified number responses to a designated Google Form.


 Note 1: Only applicable for short forms with mainly multiple choice and at most one short response question.
 
 Note 2: If not directly specified, the program will input nothing into typed answer questions, which causes it to fail if those questions are required.
 
 Note 3: Follows human (or bot) trends via results sheet. 
    
 - Note 3a: You will need to make the results sheet viewable to all.

# HOW TO USE
 Pip install all required libraries (re, requests, demjson3, sys, random, pandas)
 
 Run the following command in your terminal, substituting variables in:
    
 - python3 main.py (url of form) (number of responses) (ID of results sheet made from the form) (name of the tab in the sheet [by default, "Form responses 1"])
 

 Then just wait.

# TODO
- ~~Random choice from scraped values~~
- ~~Actually check the radio value for randomly selected choice~~
- ~~Do the same for all~~
- ~~Put " " for short answer/long response unless otherwise specified~~
- ~~Submit form~~
- ~~Repeat x times~~

- ~~Make form url and responses sys available~~

- ~~Follow Google Sheet results, identify human trends and weight options accordingly instead of being purely random~~

- Create Github Action to run a personal form
    - Create workflow.yml
    - Create requirements.txt (then also update HOW TO USE)
