# Photo Addresser

## 💭 Overview

This project is a simple way to pull the address for any photo that contains the original metadata. 

## 🚀 Features

- Clean CLI interface to provide a simple image selection process.

- Utilizes reverse geocoding to provide the address from the image provided.

## 📦 Installation & Setup & Use

```bash
# Clone the repository
git clone https://github.com/TitoBlackspire/PhotoAddresser.git

# Navigate into the directory
cd PhotoAddresser

# Setup the virtual environment with pip packages
python3.11 -m venv .ve
source .ve/bin/activate
pip install -r requirements.txt

# Start the script
python main.py
```

## Testing

You can find images to test with using [ianare/exif-samples](https://github.com/ianare/exif-samples) repo.

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
