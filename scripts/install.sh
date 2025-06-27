#!/bin/bash

echo "🔧 Installing WorldLang OS dependencies..."

# Detect OS
OS=$(uname)
if [[ "$OS" == "Linux" ]]; then
    echo "🟢 Linux detected"
    sudo apt update
    sudo apt install -y tesseract-ocr python3 python3-pip libasound2-dev
    pip3 install -r engines/requirements.txt
elif [[ "$OS" == "Darwin" ]]; then
    echo "🟣 macOS detected"
    brew install tesseract
    pip3 install -r engines/requirements.txt
else
    echo "🔴 Unsupported OS. Try Linux or macOS."
    exit 1
fi

echo "✅ Installation complete."
