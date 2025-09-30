from flask import Flask, render_template, request, jsonify
import datetime
import os
import json

# 获取当前文件所在目录
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# 配置模板目录
app.template_folder = os.path.join(basedir, 'templates')

# 配置文件路径
CONFIG_FILE = os.path.join(basedir, 'config.json')

# 默认配置
DEFAULT_CONFIG = {
    "work_start_hour": 9,
    "work_start_minute": 0,
    "work_end_hour": 18,
    "work_end_minute": 0
}

# 加载配置
def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return DEFAULT_CONFIG
    return DEFAULT_CONFIG

# 保存配置
def save_config(config):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

# 获取当前配置
config = load_config()

@app.route('/')
def index():
    return render_template('countdown.html')

@app.route('/api/countdown')
def countdown_api():
    now = datetime.datetime.now()
    
    # 获取配置的上下班时间
    work_start_hour = config.get("work_start_hour", 9)
    work_start_minute = config.get("work_start_minute", 0)
    work_end_hour = config.get("work_end_hour", 18)
    work_end_minute = config.get("work_end_minute", 0)
    
    # 设置今天的上班时间和下班时间
    work_start = datetime.datetime(now.year, now.month, now.day, work_start_hour, work_start_minute, 0)
    work_end = datetime.datetime(now.year, now.month, now.day, work_end_hour, work_end_minute, 0)
    
    # 判断当前是上班前、上班中还是下班后
    if now < work_start:
        # 上班前，倒计时到上班时间
        target_time = work_start
        message = "距离上班还有:"
    elif now <= work_end:
        # 上班中，倒计时到下班时间
        target_time = work_end
        message = "距离下班还有:"
    else:
        # 下班后，倒计时到明天上班时间
        target_time = work_start + datetime.timedelta(days=1)
        message = "距离明天上班还有:"
    
    # 计算剩余时间
    diff = target_time - now
    total_seconds = int(diff.total_seconds())
    
    if total_seconds <= 0:
        return jsonify({
            'finished': True,
            'message': '时间到了!'
        })
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return jsonify({
        'finished': False,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'formatted': f'{hours:02d}:{minutes:02d}:{seconds:02d}',
        'message': message
    })

@app.route('/api/set_work_time', methods=['POST'])
def set_work_time():
    global config
    data = request.get_json()
    
    # 更新配置
    config["work_start_hour"] = int(data.get('start_hour', 9))
    config["work_start_minute"] = int(data.get('start_minute', 0))
    config["work_end_hour"] = int(data.get('end_hour', 18))
    config["work_end_minute"] = int(data.get('end_minute', 0))
    
    # 保存配置
    save_config(config)
    
    return jsonify({
        'status': 'success',
        'message': '工作时间设置成功'
    })

@app.route('/api/get_config')
def get_config():
    return jsonify(config)

if __name__ == '__main__':
    # 在容器中运行时，绑定到0.0.0.0
    app.run(host='0.0.0.0', port=5000, debug=False)