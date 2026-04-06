---
name: obsidian
description: 用于与 Obsidian 知识库交互的技能，支持读取、编辑、创建笔记，搜索知识库内容，以及同步代码项目文档到 Obsidian。当用户需要操作 Obsidian 笔记、查询知识库、将代码文档同步到 Obsidian 时使用此技能。
---

# Obsidian 知识库操作技能

此技能用于与本地 Obsidian Vault 进行交互，支持文件系统级别的笔记操作。

## 配置信息

- **Vault 路径**: `/Users/jackgao/IdeaProjects/obsidian/`
- **操作方式**: 直接文件系统操作（无需 REST API 插件）

## 核心功能

### 1. 读取笔记

读取 Obsidian 笔记内容，支持解析 YAML frontmatter 和正文。

**工作流程**:
1. 构建完整的文件路径（支持子目录）
2. 读取 `.md` 文件内容
3. 解析 YAML frontmatter（如果有）
4. 返回笔记内容

**文件路径规则**:
- 笔记名不包含 `.md` 后缀时自动添加
- 支持子目录路径，如 `Projects/我的项目`
- 如果文件不存在，询问用户是否创建

### 2. 创建/编辑笔记

创建新笔记或编辑现有笔记，支持 YAML frontmatter。

**工作流程**:
1. 确定文件路径（基于 vault 根目录）
2. 如需要，构建 YAML frontmatter
3. 写入文件内容
4. 确认写入成功

**YAML Frontmatter 模板**:
```yaml
---
title: 笔记标题
date: 2024-01-15
tags: [tag1, tag2]
category: 分类
---
```

### 3. 搜索知识库

在 Obsidian vault 中搜索笔记。

**搜索方式**:
1. **按文件名搜索**: 使用通配符匹配文件名
2. **按内容搜索**: 搜索文件内容中的关键词
3. **按标签搜索**: 查找包含特定标签的笔记

**工具使用**:
- 使用 `search_file` 工具搜索文件名
- 使用 `search_content` 工具搜索文件内容

### 4. 同步代码项目文档

将代码项目的文档同步到 Obsidian，便于知识管理。

**常见同步场景**:
1. **README 同步**: 将项目 README 同步到 Obsidian 项目笔记
2. **API 文档同步**: 将代码注释生成的文档同步到 Obsidian
3. **架构文档同步**: 将项目架构设计文档同步到 Obsidian
4. **会议笔记/日报**: 在 Obsidian 中创建与项目相关的笔记

**同步工作流程**:
1. 确定源文件（代码项目中的文档）
2. 确定目标路径（Obsidian 中的位置）
3. 读取源文件内容
4. 转换格式（如需要，添加 Obsidian 链接、标签等）
5. 写入 Obsidian

### 5. Daily Notes 操作

在 Daily Notes 中添加内容。

**Daily Notes 路径格式**: `Daily/YYYY-MM-DD.md`

**工作流程**:
1. 根据当前日期构建文件路径
2. 如文件不存在，创建文件并添加 frontmatter
3. 追加内容到文件末尾

## 最佳实践

### 文件组织建议

```
/Users/jackgao/IdeaProjects/obsidian/
├── Daily/                    # 日记
├── Projects/                 # 项目笔记
├── Areas/                    # 领域知识
├── Resources/                # 资源/参考资料
├── Archive/                  # 归档
└── Templates/                # 模板
```

### 笔记链接

- 使用 Obsidian 维基链接格式：`[[笔记名称]]`
- 支持链接到标题：`[[笔记名称#标题]]`
- 支持别名链接：`[[笔记名称|显示文本]]`

### 标签使用

- 行内标签：`#tag`
-  frontmatter 标签：`tags: [tag1, tag2]`

## 使用示例

### 示例 1: 读取笔记
```
用户：帮我读取 Obsidian 中 "微服务架构" 笔记
操作：
1. 在 vault 中搜索 "微服务架构.md"
2. 读取文件内容
3. 返回给用户
```

### 示例 2: 创建项目笔记
```
用户：帮我在 Obsidian 的 Projects 目录下创建一个关于 surge-server 的笔记
操作：
1. 检查 /Users/jackgao/IdeaProjects/surge-server/README.md
2. 读取项目信息
3. 在 /Users/jackgao/IdeaProjects/obsidian/Projects/surge-server.md 创建笔记
4. 包含项目描述、技术栈、架构概述
```

### 示例 3: 搜索知识库
```
用户：查找 Obsidian 中所有关于 "Spring Boot" 的笔记
操作：
1. 使用 search_content 在 vault 中搜索 "Spring Boot"
2. 返回匹配的笔记列表和内容片段
```

### 示例 4: 添加到 Daily Notes
```
用户：帮我在今天的 Daily Note 中记录当前代码修改
操作：
1. 获取当前日期，构建路径 Daily/YYYY-MM-DD.md
2. 如文件不存在，创建文件
3. 追加内容："## 代码修改\n- surge-server 项目：添加了 Obsidian skill\n"
```

### 示例 5: 同步当前项目文档
```
用户：把当前项目的问卷模块文档同步到 Obsidian
操作：
1. 读取 /Users/jackgao/IdeaProjects/surge-server/surge-mvp/doc/questionnaire-module.md
2. 在 /Users/jackgao/IdeaProjects/obsidian/Projects/surge-server/ 目录下创建或更新 questionnaire-module.md
3. 添加 frontmatter 和项目关联信息
```

## 注意事项

1. **文件编码**: 所有文件使用 UTF-8 编码
2. **换行符**: 使用 Unix 换行符 (`\n`)
3. **路径安全**: 确保路径在 vault 目录内，防止目录遍历
4. **文件覆盖**: 编辑前确认文件是否存在，避免意外覆盖
5. **格式兼容性**: 保持 Obsidian Markdown 兼容性，支持：
   - 维基链接 `[[...]]`
   - 标签 `#tag`
   - YAML frontmatter
   - 代码块
   - LaTeX 数学公式
