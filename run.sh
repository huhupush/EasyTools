#!/bin/bash

# 设置虚拟环境目录
VENV_DIR="venv"
PYTHON_VERSION="3.8"  # 指定 Python 版本

# 检查 Python 环境
if ! command -v python${PYTHON_VERSION} &> /dev/null; then
    echo "错误: 未找到 Python ${PYTHON_VERSION}"
    echo "请安装 Python ${PYTHON_VERSION} 后重试"
    exit 1
fi

# 检查并创建虚拟环境
if [ ! -d "$VENV_DIR" ]; then
    echo "创建虚拟环境..."
    python${PYTHON_VERSION} -m venv $VENV_DIR || {
        echo "创建虚拟环境失败"
        exit 1
    }
fi

# 激活虚拟环境
if [ -f "$VENV_DIR/bin/activate" ]; then
    source $VENV_DIR/bin/activate
else
    echo "错误: 虚拟环境激活脚本不存在"
    exit 1
fi

# 检查并安装依赖
echo "检查依赖..."
pip install -r requirements.txt || {
    echo "安装依赖失败"
    exit 1
}

# 启动应用
echo "启动二进制文件查看器..."
streamlit run app.py
