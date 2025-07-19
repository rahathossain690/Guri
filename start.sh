#!/bin/bash

startup(){
  if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
  fi

  source ./.venv/bin/activate

  if ! pip3 freeze | grep -q -F -f requirements.txt; then
    echo "Installing required packages..."
    pip3 install -r requirements.txt
  fi

  if [ ! -f .env ]; then
    echo ".env file not found. Please create a .env file with the required environment variables."
    exit 1
  fi

  source ./.env

  uvicorn app.server:app --host "$APP_HOST" --port "$APP_PORT" --reload
}

cleanup(){
  deactivate
  pkill -f "uvicorn app.server:app"
}

startup
trap cleanup EXIT