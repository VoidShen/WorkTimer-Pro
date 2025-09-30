# 使用官方Python运行时作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制requirements.txt文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制当前目录内容到容器的/app目录中
COPY . /app

# 暴露端口5000
EXPOSE 5000

# 设置环境变量
ENV FLASK_APP=app.py

# 容器启动时运行的命令
CMD ["python", "app.py"]