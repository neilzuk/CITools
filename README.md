# CI Tools
This repository is a collection of simple tools to help with continuous integration
 build processes such as with GitLab's CI pipelines.  

 ## checkwebsite.py
 Used as the last step to deploying a web application through CI to verify the
 website returns the expected status code e.g. 200 - working as expected! Any status
 other than the one expected can cause the task in CI to fail and then alert the team
 depending on your setup.

Command  
```checkwebsite.py http://www.example.com 200```  
Result  
```http://www.example.com returned the expected 200```
