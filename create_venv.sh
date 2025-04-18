#!/bin/bash

PROJECT_DIR="demo_bash"


# Tạo thư mục

mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR" || exit

# Tạo môi trường ảo
python3 -m venv demo_venv


# Kiểm tra thành công
if [ -d "demo_venv" ]; then
    echo " tạo thành công ở: $(pwd)/venv"
else
    echo "Tạo thất bại."
fi

