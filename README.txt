# Predictive Maintenance System (MLOps Pipeline)

An end-to-end machine learning system to predict equipment failures using MLflow, FastAPI, and Docker.

## 🚀 Features
- ML model training using Scikit-learn
- Experiment tracking with MLflow
- Real-time inference using FastAPI
- Containerized deployment using Docker

## 🏗️ Architecture
Data → MLflow → Model → FastAPI → Docker

## ⚡ API Usage

Run API:
uvicorn app.main:app --reload

Endpoint:
POST /predict

Example:
{
  "temperature": 85,
  "vibration": 0.8,
  "pressure": 40
}

## 🐳 Docker

Build:
docker build -t predictive-maintenance .

Run:
docker run -p 8000:8000 predictive-maintenance
