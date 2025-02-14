# 二进制文件查看器

一个简单的基于 Streamlit 的二进制文件查看器，支持以下功能：

- 文件上传和基本信息显示
- 多种查看模式（十六进制、ASCII、二进制）
- 可调节的查看范围和偏移量

## 环境要求

- Python 3.8 或更高版本
- 虚拟环境支持 (venv)

## 安装和运行

### 方式一：一键启动（推荐）

```bash
# 为启动脚本添加执行权限
chmod +x run.sh
# 运行启动脚本
./run.sh
```

启动脚本会自动：
- 检查 Python 环境
- 创建并激活虚拟环境
- 安装所需依赖
- 启动应用程序

### 方式二：手动安装和运行

1. 创建并激活虚拟环境：
```bash
python3.8 -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行应用：
```bash
streamlit run app.py
```

## 使用说明

1. 打开浏览器访问显示的地址（默认为 http://localhost:8501）
2. 点击"选择二进制文件"上传要查看的文件
3. 选择查看模式（十六进制/ASCII/二进制）
4. 调整显示的字节数和起始偏移量
