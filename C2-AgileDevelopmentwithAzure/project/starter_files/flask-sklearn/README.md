[![Python application test with Github Actions](https://github.com/WMaximusW/nd082-Azure-Cloud-DevOps-Starter-Code/actions/workflows/pythonappflasksklearn.yml/badge.svg)](https://github.com/WMaximusW/nd082-Azure-Cloud-DevOps-Starter-Code/actions/workflows/pythonappflasksklearn.yml)

# Overview

<TODO: complete this with an overview of your project>

This project is a "Flask-based web application" that "predicts housing prices based on various input features using a pre-trained machine learning model.".

The application is deployed on Azure App Service and utilizes a continuous integration and continuous deployment (CI/CD) pipeline powered by GitHub Actions and Azure Pipelines. The CI/CD pipeline ensures that any changes pushed to the repository are automatically tested, built, and deployed.

## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project
https://trello.com/b/5xWLnU2R/udacity-project-2
* A link to a spreadsheet that includes the original and final project plan>
https://docs.google.com/spreadsheets/d/1u9QLL-piIKXY_sCHM8Fao3HFqIfKvcNvLcPr0PVZOPA/edit?gid=1348135932#gid=1348135932

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service
![alt text](<Screenshot 2024-08-11 094933.png>)

* Project cloned into Azure Cloud Shell

![alt text](<Screenshot 2024-08-09 202135-clone-github.png>)

* Passing tests that are displayed after running the `make all` command from the `Makefile`

![alt text](<Screenshot 2024-08-09 202135-make-pass-test.png>)

* Output of a test run

![alt text](<Screenshot 2024-08-09 202135-git-hub-action.png>)

![alt text](<Screenshot 2024-08-11 094959.png>)

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

![alt text](<Screenshot 2024-08-11 095155.png>)

* Running Azure App Service from Azure Pipelines automatic deployment

![alt text](<Screenshot 2024-08-11 095138.png>)

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

![alt text](<Screenshot 2024-08-11 101423.png>)

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application
![alt text](<Screenshot 2024-08-11 101820.png>)
> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

- **Add More Features**: Implement additional endpoints for more complex operations.
- **Improve Testing**: Expand test coverage to include edge cases and use more advanced testing tools.
- **Optimize Performance**: Focus on optimizing database queries and caching responses for better performance.
- **Extend CI/CD**: Integrate security scanning tools and automate monitoring setups.

## Demo 

<TODO: Add link Screencast on YouTube>
https://youtu.be/5WH2PfEL6zc


