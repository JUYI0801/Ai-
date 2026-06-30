#!/usr/bin/env python3
"""
自动更新数据脚本
用于更新index.html中的日期和内容
"""
import re
from datetime import datetime

def update_date_in_html(file_path):
    """更新HTML文件中的日期"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 获取当前日期
        today = datetime.now()
        date_str = today.strftime('%Y-%m-%d')
        
        # 更新标题中的日期
        content = re.sub(
            r'<title>2026 AI 大模型全景对比 · \d{4}-\d{2}-\d{2} 更新</title>',
            f'<title>2026 AI 大模型全景对比 · {date_str} 更新</title>',
            content
        )
        
        # 更新页面中的日期标签
        content = re.sub(
            r'<div class="tag">Updated · \d{4}-\d{2}-\d{2}</div>',
            f'<div class="tag">Updated · {date_str}</div>',
            content
        )
        
        # 写入更新后的内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ 已更新日期为: {date_str}")
        return True
        
    except Exception as e:
        print(f"✗ 更新失败: {e}")
        return False

if __name__ == '__main__':
    update_date_in_html('index.html')
