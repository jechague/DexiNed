#!/bin/bash

if [ ! -f "./weights/DexiNed23_model.h5" ]; then
    echo "Downloading model weights from Google Drive..."
    fileid="19Gwa6egqzNolvX4eUoXn-SjRKzxB68AA"
    filename="weights.zip"
    curl -c ./.cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
    curl -Lb ./.cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./.cookie`&id=${fileid}" -o ${filename}
    rm -rf weights
    mkdir weights
    unzip $filename -d weights
    rm -rf $filename
    rm -rf ./.cookie
else
    echo "Model weights already downloaded."
fi