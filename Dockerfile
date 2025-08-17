# Dockerfile

# 使用官方的 Python 基础镜像
FROM python:3.10-slim

# 设置环境变量，防止 Python 生成 .pyc 文件，设置 UTF-8 locale
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 并安装依赖
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目的所有文件到容器
COPY . .

RUN mkdir -p logs

EXPOSE 7860

# 设置容器入口
CMD ["python", "src/main.py"]
