# WorkTimer Pro

![WorkTimer Pro](https://img.shields.io/badge/WorkTimer-Pro-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)
![Python Version](https://img.shields.io/badge/python-3.9-blue)
![Flask Version](https://img.shields.io/badge/flask-2.3.2-red)

WorkTimer Pro 是一个基于 Flask 的智能上下班倒计时应用，可以显示距离上班或下班的剩余时间。它具有现代化的用户界面和可配置的工作时间设置。

## 功能特点

- 🕐 实时倒计时显示距离上班或下班的时间
- ⚙️ 可自定义工作时间（上班时间和下班时间）
- 🎨 现代化、响应式的用户界面，带有动画效果
- 🐳 支持 Docker 容器化部署
- 📱 响应式设计，适配不同设备屏幕
- 💾 配置持久化，设置会保存在本地文件中

## 技术栈

- Python 3.9
- Flask 2.3.2
- HTML5/CSS3/JavaScript
- Docker & Docker Compose

## 快速开始

### 使用 Docker Compose（推荐）

```bash
# 克隆项目
git clone <repository-url>
cd worktimer-pro

# 启动应用
docker-compose up -d

# 访问应用
# 打开浏览器访问 http://localhost:5000
```

### 直接运行

```bash
# 克隆项目
git clone <repository-url>
cd worktimer-pro

# 安装依赖
pip install -r requirements.txt

# 启动应用
python app.py

# 访问应用
# 打开浏览器访问 http://localhost:5000
```

## 使用说明

1. 打开浏览器访问 `http://localhost:5000`
2. 页面将自动显示距离上班或下班的倒计时
3. 点击右上角的齿轮图标 ⚙️ 可以打开设置面板
4. 在设置面板中可以修改上班时间和下班时间
5. 点击"保存设置"按钮保存配置

## 配置

默认工作时间配置保存在 [config.json](config.json) 文件中：

```json
{
  "work_start_hour": 9,
  "work_start_minute": 0,
  "work_end_hour": 18,
  "work_end_minute": 0
}
```

## API 接口

- `GET /` - 返回主页面
- `GET /api/countdown` - 返回倒计时数据
- `GET /api/get_config` - 返回当前配置
- `POST /api/set_work_time` - 设置工作时间

## Docker 支持

项目包含 [Dockerfile](Dockerfile) 和 [docker-compose.yml](docker-compose.yml) 文件，支持容器化部署。

构建镜像：
```bash
docker build -t worktimer-pro .
```

运行容器：
```bash
docker run -p 5000:5000 worktimer-pro
```

## 项目结构

```
worktimer-pro/
├── app.py              # Flask 应用主文件
├── config.json         # 配置文件
├── requirements.txt    # Python 依赖
├── Dockerfile          # Docker 配置文件
├── docker-compose.yml  # Docker Compose 配置文件
├── templates/
│   └── countdown.html  # 前端页面模板
└── README.md           # 项目说明文件
```

## 许可证

本项目采用 MIT 许可证，详情请见 [LICENSE](LICENSE) 文件。