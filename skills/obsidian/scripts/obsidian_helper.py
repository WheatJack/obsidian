#!/usr/bin/env python3
"""
Obsidian Vault 操作辅助脚本
提供常用的 Obsidian 文件操作功能
"""

import os
import sys
import re
import yaml
from datetime import datetime
from pathlib import Path

VAULT_PATH = "/Users/jackgao/IdeaProjects/obsidian"


def ensure_vault_path():
    """确保 Vault 路径存在"""
    if not os.path.exists(VAULT_PATH):
        print(f"Error: Vault path does not exist: {VAULT_PATH}")
        sys.exit(1)


def get_note_path(note_name: str, subdir: str = "") -> str:
    """
    构建笔记的完整路径
    
    Args:
        note_name: 笔记名称（可包含或不包含 .md 后缀）
        subdir: 子目录（可选）
    
    Returns:
        完整的文件路径
    """
    if not note_name.endswith('.md'):
        note_name += '.md'
    
    if subdir:
        full_path = os.path.join(VAULT_PATH, subdir, note_name)
    else:
        full_path = os.path.join(VAULT_PATH, note_name)
    
    return full_path


def read_note(note_path: str) -> dict:
    """
    读取笔记内容，解析 YAML frontmatter
    
    Args:
        note_path: 笔记的完整路径
    
    Returns:
        包含 frontmatter 和 content 的字典
    """
    if not os.path.exists(note_path):
        return None
    
    with open(note_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 解析 YAML frontmatter
    frontmatter = {}
    body = content
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1])
                body = parts[2].strip()
            except yaml.YAMLError:
                pass
    
    return {
        'frontmatter': frontmatter,
        'content': body,
        'full_content': content
    }


def write_note(note_path: str, content: str, frontmatter: dict = None) -> bool:
    """
    写入笔记内容
    
    Args:
        note_path: 笔记的完整路径
        content: 笔记正文
        frontmatter: YAML frontmatter 字典（可选）
    
    Returns:
        是否写入成功
    """
    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(note_path), exist_ok=True)
        
        # 构建完整内容
        if frontmatter:
            yaml_content = yaml.dump(frontmatter, allow_unicode=True, sort_keys=False)
            full_content = f"---\n{yaml_content}---\n\n{content}"
        else:
            full_content = content
        
        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        return True
    except Exception as e:
        print(f"Error writing note: {e}")
        return False


def append_to_note(note_path: str, content: str) -> bool:
    """
    追加内容到笔记末尾
    
    Args:
        note_path: 笔记的完整路径
        content: 要追加的内容
    
    Returns:
        是否追加成功
    """
    try:
        # 如果文件不存在，先创建
        if not os.path.exists(note_path):
            os.makedirs(os.path.dirname(note_path), exist_ok=True)
            with open(note_path, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            with open(note_path, 'a', encoding='utf-8') as f:
                f.write('\n' + content)
        
        return True
    except Exception as e:
        print(f"Error appending to note: {e}")
        return False


def get_daily_note_path(date: datetime = None) -> str:
    """
    获取 Daily Note 的路径
    
    Args:
        date: 日期（默认为今天）
    
    Returns:
        Daily Note 的完整路径
    """
    if date is None:
        date = datetime.now()
    
    date_str = date.strftime('%Y-%m-%d')
    return os.path.join(VAULT_PATH, 'Daily', f'{date_str}.md')


def create_daily_note(content: str = "", date: datetime = None) -> str:
    """
    创建 Daily Note
    
    Args:
        content: 笔记内容
        date: 日期（默认为今天）
    
    Returns:
        创建的笔记路径
    """
    if date is None:
        date = datetime.now()
    
    note_path = get_daily_note_path(date)
    
    if not os.path.exists(note_path):
        frontmatter = {
            'title': date.strftime('%Y-%m-%d'),
            'date': date.strftime('%Y-%m-%d'),
            'tags': ['daily']
        }
        
        default_content = f"# {date.strftime('%Y年%m月%d日')}\n\n"
        if content:
            default_content += content
        
        write_note(note_path, default_content, frontmatter)
    else:
        append_to_note(note_path, content)
    
    return note_path


def search_notes_by_tag(tag: str) -> list:
    """
    搜索包含特定标签的笔记
    
    Args:
        tag: 标签名称（不包含 #）
    
    Returns:
        匹配的笔记路径列表
    """
    matching_notes = []
    
    for root, dirs, files in os.walk(VAULT_PATH):
        # 跳过隐藏目录
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 检查 frontmatter 中的 tags
                    if content.startswith('---'):
                        parts = content.split('---', 2)
                        if len(parts) >= 3:
                            try:
                                frontmatter = yaml.safe_load(parts[1])
                                if frontmatter and 'tags' in frontmatter:
                                    if tag in frontmatter['tags']:
                                        matching_notes.append(file_path)
                                        continue
                            except yaml.YAMLError:
                                pass
                    
                    # 检查行内标签
                    if f'#{tag}' in content:
                        matching_notes.append(file_path)
                
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    
    return matching_notes


def list_notes(subdir: str = "") -> list:
    """
    列出指定目录下的所有笔记
    
    Args:
        subdir: 子目录（可选）
    
    Returns:
        笔记路径列表
    """
    if subdir:
        target_dir = os.path.join(VAULT_PATH, subdir)
    else:
        target_dir = VAULT_PATH
    
    notes = []
    
    if os.path.exists(target_dir):
        for root, dirs, files in os.walk(target_dir):
            # 跳过隐藏目录
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for file in files:
                if file.endswith('.md'):
                    notes.append(os.path.join(root, file))
    
    return notes


if __name__ == '__main__':
    ensure_vault_path()
    
    # 测试代码
    print(f"Vault path: {VAULT_PATH}")
    print(f"Daily note path: {get_daily_note_path()}")
