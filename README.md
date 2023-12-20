# flask_e2e_project
504 Final Project

## Overview 
Welcome to the Pregnancy-Associated Mortality Web App Repository! The product created and documented in this repository is a Flask web application designed to visualize and explore data related to pregnancy-associated mortality rates in New York City from 2016 to 2020. The dataset used in this project encompasses pregnancy mortality data, providing insights into the number of deaths based on various factors such as the year, related conditions, underlying causes, race/ethnicity, and borough.

## Web Service Functionality
Users can access the web service to explore and understand the pregnancy mortality rates.

## Technologies Used
- Github (Version Control)
- Flask (Python; Frotend & Backend)
- MySQL (Azure)
- Tailwind (Frontend Styling)
- .ENV (Environment Variables)
- API Service (Flask Backend)
- Azure (Deployment)
- Logger and or Sentry.io (Debugging & Logging)
- Docker (Containerization)
## Steps to Running the Web-Service

The Flask web application can be deployed in three different ways: locally, using Docker, and cloud deployment with Azure. 

### Deploying Locally

1. **Clone the Repository:**
   - Clone this repository to your local machine using the following command:
     ```bash
     git clone https://github.com/Jannath19/flask_e2e_project.git
     ```

2. **Change Directory to App Folder:**
   - Navigate to the `app` directory:
     ```bash
     cd flask_e2e_project/app
     ```

3. **Run the Application:**
   - In the terminal, run the application using the following command:
     ```bash
     python app.py
     ```
   - The terminal will create and display connection addresses. Open one of these addresses in your web browser to access the web application.

### Deploying with Docker

1. **Build the Docker Image:**
   - Navigate to the project's root directory:
     ```bash
     cd flask_e2e_project
     ```
   - Build the Docker image using the following command:
     ```bash
     docker build -t flask-e2e-project .
     ```

2. **Run the Docker Container:**
   - Start a Docker container using the built image:
     ```bash
     docker run -p 5000:5000 flask-e2e-project
     ```
   - Access the web application in your browser using [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### Deploying on Azure

1. **Install Azure CLI:**
   - Install Azure CLI in Azure Cloud Shell or locally:
     ```bash
     curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
     ```

2. **Log in to Azure:**
   - Authenticate with your Azure account:
     ```bash
     az login --use-device-code
     ```

3. **Create Resource Group:**
   - Create a resource group:
     ```bash
     az group create --name <resource-group-name> --location eastus
     ```

4. **Deploy Application:**
   - Deploy the Flask app:
     ```bash
     az webapp up --resource-group <resource-group-name> --name <app-name> --runtime "PYTHON|3.9" --sku F1
     ```
     Replace placeholders with your names.

### Troubleshooting and Known Issues

#### Google OAuth Error
- **Issue:** Encountered an error while setting up OAuth consent screen. The consent screen in the Google Cloud Console wasn't loading on my end; tried refreshing as well.
