from flask import Flask, render_template, request, jsonify
import datetime
import os

# 获取当前文件所在目录
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# 配置模板目录
app.template_folder = os.path.join(basedir, 'templates')

@app.route('/')
def index():
    return render_template('countdown.html')

@app.route('/api/countdown')
def countdown_api():
    # 默认下班时间是18:00
    now = datetime.datetime.now()
    off_time = datetime.datetime(now.year, now.month, now.day, 18, 0, 0)
    
    # 如果当前时间已经超过18:00，则设置为明天的18:00
    if now.hour >= 18:
        off_time += datetime.timedelta(days=1)
    
    # 计算剩余时间
    diff = off_time - now
    total_seconds = int(diff.total_seconds())
    
    if total_seconds <= 0:
        return jsonify({
            'finished': True,
            'message': '下班时间到了!'
        })
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return jsonify({
        'finished': False,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'formatted': f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    })

@app.route('/api/set_off_time', methods=['POST'])
def set_off_time():
    data = request.get_json()
    hour = int(data.get('hour', 18))
    minute = int(data.get('minute', 0))
    
    # 获取当前时间并设置下班时间
    now = datetime.datetime.now()
    off_time = datetime.datetime(now.year, now.month, now.day, hour, minute, 0)
    
    # 如果设定时间早于当前时间，则设置为明天
    if off_time <= now:
        off_time += datetime.timedelta(days=1)
    
    # 计算剩余时间
    diff = off_time - now
    total_seconds = int(diff.total_seconds())
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return jsonify({
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'formatted': f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    })

if __name__ == '__main__':
    # 在容器中运行时，绑定到0.0.0.0
    app.run(host='0.0.0.0', port=5000, debug=False)