# Obsidian Vault 结构参考

## Vault 根目录

```
/Users/jackgao/IdeaProjects/obsidian/
```

## 标准目录组织（PARA 方法）

### Projects（项目）
存放有明确目标和截止日期的项目笔记。

示例：
- `Projects/surge-server.md` - surge-server 项目笔记
- `Projects/个人网站重构.md` - 个人项目

### Areas（领域）
存放需要长期维护的责任领域。

示例：
- `Areas/后端开发.md`
- `Areas/微服务架构.md`
- `Areas/Java 技术栈.md`

### Resources（资源）
存放参考材料和学习资源。

示例：
- `Resources/Spring Boot 最佳实践.md`
- `Resources/Docker 命令速查.md`

### Archive（归档）
存放已完成或不再活跃的项目和领域。

### Daily（日记）
存放每日笔记，格式为 `Daily/YYYY-MM-DD.md`。

## 文件命名规范

1. **使用中文或英文**：根据内容选择合适的语言
2. **避免特殊字符**：不要使用 `/ \ : * ? " < > |`
3. **空格处理**：可以使用空格或 `-` 连接单词
4. **大小写**：保持一致，建议使用首字母大写

## 常用 Frontmatter 字段

```yaml
---
title: 笔记标题
date: 2024-01-15  # 创建日期
updated: 2024-01-15  # 更新日期
tags: [tag1, tag2]  # 标签
category: 分类  # 分类
status: active  # 状态: active, archived, draft
source: 来源  # 来源链接或参考
---
```

## 常用链接格式

### 内部链接
```markdown
[[笔记名称]]
[[笔记名称|显示文本]]
[[笔记名称#标题]]
[[笔记名称#^块ID]]
```

### 嵌入内容
```markdown
![[笔记名称]]
![[笔记名称#标题]]
```

### 外部链接
```markdown
[链接文本](URL)
```

## 常用标签

### 技术标签
- `#java`
- `#spring-boot`
- `#microservices`
- `#database`
- `#docker`
- `#kubernetes`

### 状态标签
- `#todo`
- `#in-progress`
- `#completed`
- `#archived`
- `#important`

### 类型标签
- `#meeting` - 会议记录
- `#learning` - 学习笔记
- `#idea` - 想法
- `#summary` - 总结
