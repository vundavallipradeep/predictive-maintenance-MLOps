# Predictive Maintenance System

This project started as an attempt to understand how machine learning models can be taken beyond notebooks and used in a real system. The goal is to predict equipment failure based on sensor data and expose the model as a usable service.

## What I built

- Trained a classification model using sensor data (temperature, vibration, pressure)
- Tracked experiments and compared runs using MLflow
- Exposed the trained model through a FastAPI endpoint
- Containerized the service using Docker so it can run anywhere

## How it works

The workflow looks like this:

Data → Model Training → MLflow Tracking → API → Docker

I first trained the model in a notebook and logged metrics and parameters using MLflow.  
Once I was satisfied with the model, I saved it and built an API around it using FastAPI.  
Finally, I used Docker to make sure the whole setup runs consistently across environments.

## Running the project

### Start the API

```bash
python -m uvicorn app.main:app --reload
