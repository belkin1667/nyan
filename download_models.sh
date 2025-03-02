#!/bin/bash

# Check if models directory exists and contains required files
if [ -d "models" ] && [ -f "models/lid.176.bin" ] && [ -f "models/multilingual_e5_base_cat_detect.joblib" ]; then
    echo "Required model files already exist. Skipping download."
    exit 0
fi

mkdir -p models
wget https://github.com/NyanNyanovich/nyan/releases/download/v0.3/nyan_models.tar.gz -O models/nyan_models.tar.gz
cd models && tar -xzvf nyan_models.tar.gz && rm nyan_models.tar.gz
