#!/usr/bin/env python3
"""
Automated Chinese to English translation script for main.py
This script will replace all Chinese text with English translations
"""

import re

# Translation mapping - Chinese to English
TRANSLATIONS = {
    # Section headers
    "SMTP邮件配置": "SMTP Email Configuration",
    "配置管理": "Configuration Management",
    "工具函数": "Utility Functions",
    "数据获取": "Data Fetching",
    "数据处理": "Data Processing",
    "推送记录管理": "Push Record Management",
    
    # Function docstrings
    "加载配置文件": "Load configuration file",
    "获取北京时间": "Get Beijing time",
    "格式化日期文件夹": "Format date folder",
    "格式化时间文件名": "Format time filename",
    "清理标题中的特殊字符": "Clean special characters from title",
    "确保目录存在": "Ensure directory exists",
    "获取输出路径": "Get output path",
    "检查版本更新": "Check version update",
    "检测是否是当天第一次爬取": "Detect if this is the first crawl of the day",
    "HTML转义": "HTML escape",
    "推送记录管理器": "Push record manager",
    "确保记录目录存在": "Ensure record directory exists",
    "获取今天的记录文件路径": "Get today's record file path",
    "清理过期的推送记录": "Clean up expired push records",
    "检查今天是否已经推送过": "Check if pushed today",
    "记录推送": "Record push",
    "检查当前时间是否在指定时间范围内": "Check if current time is within specified time range",
    "将时间字符串标准化为 HH:MM 格式": "Normalize time string to HH:MM format",
    "获取指定ID数据，支持重试": "Fetch data for specified ID, with retry support",
    "爬取多个网站数据": "Crawl multiple websites data",
    "保存标题到文件": "Save titles to file",
    "加载频率词配置": "Load frequency word configuration",
    "发送到Bark（支持分批发送，使用 markdown 格式）": "Send to Bark (supports batch sending, using markdown format)",
    "分析流程执行出错": "Analysis process execution error",
    "执行分析流程": "Execute analysis process",
    
    # Email provider comments
    "Gmail（使用 STARTTLS）": "Gmail (using STARTTLS)",
    "QQ邮箱（使用 SSL，更稳定）": "QQ Mail (using SSL, more stable)",
    "Outlook（使用 STARTTLS）": "Outlook (using STARTTLS)",
    "网易邮箱（使用 SSL，更稳定）": "NetEase Mail (using SSL, more stable)",
    "新浪邮箱（使用 SSL）": "Sina Mail (using SSL)",
    "搜狐邮箱（使用 SSL）": "Sohu Mail (using SSL)",
    "天翼邮箱（使用 SSL）": "China Telecom Mail (using SSL)",
    "阿里云邮箱（使用 TLS）": "Aliyun Mail (using TLS)",
    
    # Error and status messages
    "配置文件 {config_path} 不存在": "Configuration file {config_path} does not exist",
    "配置文件加载成功": "Configuration file loaded successfully",
    "构建配置": "Build configuration",
    "通知渠道配置（环境变量优先）": "Notification channel configuration (environment variables take precedence)",
    "环境变量": "environment variable",
    "配置文件": "configuration file",
    "飞书": "Feishu",
    "钉钉": "DingTalk",
    "企业微信": "WeCom",
    "正在加载配置...": "Loading configuration...",
    "配置加载完成": "configuration loaded",
    "监控平台数量": "Number of monitored platforms",
    "当前版本": "Current version",
    "远程版本": "remote version",
    "版本号格式不正确": "Version number format is incorrect",
    "版本检查失败": "Version check failed",
    "清理过期推送记录": "Cleanup expired push record",
    "清理记录文件失败": "Failed to clean record file",
    "读取推送记录失败": "Failed to read push record",
    "推送记录已保存": "Push record saved",
    "保存推送记录失败": "Failed to save push record",
    "时间格式错误": "Time format error",
    "时间范围错误": "Time range error",
    "时间格式化错误": "Time formatting error",
    "时间窗口判断：当前": "Time window check: current",
    "窗口": "window",
    "获取": "Fetch",
    "成功（最新数据）": "success (latest data)",
    "成功（缓存数据）": "success (cached data)",
    "成功": "success",
    "失败": "failed",
    "未知": "unknown",
    "响应状态异常": "Response status error",
    "最新数据": "latest data",
    "缓存数据": "cached data",
    "请求": "Request",
    "秒后重试...": "seconds, retrying...",
    "解析": "Parse",
    "响应失败": "response failed",
    "处理": "Process",
    "数据出错": "data error",
    "跳过无效标题（None、float、空字符串）": "Skip invalid titles (None, float, empty string)",
    
    # HTML report strings
    "热点新闻分析": "Trending News Analysis",
    "保存为图片": "Save as Image",
    "分段保存": "Save in Segments",
    "报告类型": "Report Type",
    "当前榜单": "Current Ranking",
    "增量模式": "Incremental Mode",
    "当日汇总": "Daily Summary",
    "实时分析": "Real-time Analysis",
    "新闻总数": "Total News",
    "热点新闻": "Hot News",
    "生成时间": "Generation Time",
    "请求失败的平台": "Failed Platforms",
    "由": "Generated by",
    "生成": "Generated",
    "GitHub 开源项目": "GitHub Open Source Project",
    "生成中...": "Generating...",
    "等待页面稳定": "Waiting for page to stabilize",
    "截图前隐藏按钮": "Hide buttons before screenshot",
    "再次等待确保按钮完全隐藏": "Wait again to ensure buttons are fully hidden",
    "触发下载": "Trigger download",
    "保存成功!": "Save successful!",
    "保存失败": "Save failed",
    "分析中...": "Analyzing...",
    "获取所有可能的分割元素": "Get all possible split elements",
    "TrendRadar_热点新闻分析": "TrendRadar_Trending_News_Analysis",
    
    # Notification related
    "热点词汇统计": "Hot Word Statistics",
    "本次新增热点新闻": "Newly Added Hot News This Time",
    "数据获取失败的平台": "Platforms with Data Fetch Failure",
    "更新时间": "Update Time",
    "发现新版本": "New version found",
    "全部新闻": "All News",
    
    # Mode names
    "实时增量": "Real-time Incremental",
    "实时当前榜单": "Real-time Current Ranking",
    
    # Console messages
    "正在打开": "Opening",
    "报告已生成": "report generated",
    "HTML报告已生成": "HTML report generated",
    "汇总报告已生成": "Summary report generated",
    "Docker环境": "Docker environment",
    "程序运行错误": "Program execution error",
    "请确保以下文件存在": "Please ensure the following files exist",
    "参考项目文档进行正确配置": "Refer to project documentation for proper configuration",
    
    # Frequency word file
    "频率词文件": "Frequency word file",
    "不存在": "does not exist",
    
    # Batch sending
    "消息分为": "message split into",
    "批次发送": "batches",
    "发送": "Sending",
    "批次": "batch",
    "大小：": "size:",
    "字节": "bytes",
    "批次发送成功": "batch sent successfully",
    "批次发送失败": "batch send failed",
    "所有": "All",
    "批次发送完成": "batches sent",
    "部分发送成功": "Partial send success",
    "发送完全失败": "Send completely failed",
    "警告：": "Warning:",
    "批次消息过大": "batch message too large",
    "可能被拒绝": "may be rejected",
    "速率限制": "rate limited",
    "等待后重试": "waiting to retry",
    "重试成功": "retry successful",
    "重试失败，状态码：": "retry failed, status code:",
    "消息过大被拒绝": "message rejected (too large)",
    "消息大小：": "message size:",
    "连接超时": "connection timeout",
    "读取超时": "read timeout",
    "连接错误": "connection error",
    "发送异常": "send exception",
    "错误详情：": "Error details:",
    
    # Push window control
    "推送窗口控制：当前时间": "Push window control: current time",
    "不在推送时间窗口": "not in push time window",
    "内，跳过推送": "skipping push",
    "今天已推送过，跳过本次推送": "Already pushed today, skipping this push",
    "今天首次推送": "First push today",
    
    # Other
    "如果没有配置词组，则匹配所有标题（支持显示全部新闻）": "If no word groups configured, match all titles (supports showing all news)",
    "条": "items",
}

def translate_file():
    """Main translation function"""
    input_file = "/Users/wind-tamim/wokstation/NewsHawk/main.py"
    output_file = "/Users/wind-tamim/wokstation/NewsHawk/main_english.py"
    
    print("Reading main.py...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_size = len(content)
    replacements_made = 0
    
    print(f"Original file size: {original_size} characters")
    print(f"Starting translation with {len(TRANSLATIONS)} translation rules...")
    
    # Apply translations
    for chinese, english in TRANSLATIONS.items():
        if chinese in content:
            count = content.count(chinese)
            content = content.replace(chinese, english)
            replacements_made += count
            print(f"  ✓ Replaced '{chinese[:30]}...' → '{english[:30]}...' ({count} times)")
    
    print(f"\n✅ Translation complete!")
    print(f"   - Total replacements: {replacements_made}")
    print(f"   - New file size: {len(content)} characters")
    
    # Save translated version
    print(f"\nSaving translated file to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n🎉 Done! Check the translated file at: {output_file}")
    print("\nNext steps:")
    print("  1. Review the translated file: main_english.py")
    print("  2. If everything looks good, replace main.py:")
    print("     mv main_english.py main.py")

if __name__ == "__main__":
    translate_file()
