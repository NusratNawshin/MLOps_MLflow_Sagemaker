# MLOps using MLFlow and AWS Sagemaker

# Cloud Computing - Group 7 - Final Project

---

## Deploying Simple Xgboost Model to Production with MLflow and AWS Sagemaker

---

This repository introduces how to prepare ML model for production in AWS Sagemaker with the help of MLflow and AWS CLI.

---

## Setup Environment

- AWS Account
- AWS Command Line Interface
- Docker installed on the local machine.
- Python 3.8 with mlflow>=1.0.0 installed.
- Boto3
- Anaconda software to create Conda virtual environment

### Step 1:
- Create dedicated virtual environment to perform the whole example in this repo
- Create a new conda virtual environment in the working directory and activate with the following command in the terminal:

 - conda create --name deploy_ml python=3.8
 - conda activate deploy_ml

### Step 2:
- Install mlflow package into our virtual environment with the following command:

 - pip install -q mlflow==1.18.0.

Install following modules and packages to the virtual environment:
 - Pandas: pip install pandas
 - Scikit-learn: pip install -U scikit-learn
 - AWS Command Line Interface (AWS CLI): pip install awscli --upgrade --user
 - Boto3: pip install boto3
 
 ### Step 3: Setup AWS IAM User and AWS CLI configuration
 
Create a new AWS AIM User
- Open Identity and Access management (IAM) dashboard
- Click on Users
- Click Add users on the right side of the screenshot
- Set the User name and mark Programmatic access tick below
- Click on Create group as the part of Add user to group option
- Type a group name you want to assign to your IAM User
- From the list below select following policies:
  - AmazonSageMakerFullAccess
  - AmazonEC2ContainerRegistryFullAccess
- Click on Create group, then the current Policies window will be closed
- Click on Next: Tags
- Click on Next: Review
- Click on Create user

Setup AWS CLI configuration

- Be sure you have installed AWS CLI and type command in your terminal: aws configure.
- Then you will have to enter the credentials as follows:
   - AWS Access Key ID: go to IAM, then Users, and click on your user just created. Select Security credentials tab and copy the value of AWS Access Key ID
  - AWS Secret Access Key: paste this code from your own notes. You have seen this code originally from Security credentials of your user.
  - Default region name: go to main AWS interface, click on your region, and check which region is activated for you (us-east-1, eu-west-1, and so on).
  - Default output format: set it as json.

## Prepare Machine Learning model for mlflow
- Run train.py file
With the we can track the model and generate some run artifacts in mlflow dashboard

## Deploy the model to AWS

### Step 1: Build a Docker Image and push it to AWS ECR
### Step 2. Deploy image to Sagemaker (deploy.py)

## Use the model with the new data

Once the model is running in AWS, boto3 library is used for new prediction for a new given data. Follow the following steps to do it.

- Open the terminal with activated virtual environment deploy_ml.
- Run predicting with the prediction.py file using command python predict.py

## Store the final model and results.json file in AWS S3 Bucket



### Reference Code and Instructions
[Code and Instructions](https://github.com/vb100/deploy-ml-mlflow-aws/blob/4087b67e67b27af01d0aabe68b785247cfa46779/README.md)
