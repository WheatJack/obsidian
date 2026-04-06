---
title: surge-server 项目
date: 2025-04-06
tags: [project, java, spring-boot, microservices]
category: 项目
status: active
---

# surge-server

> 项目路径: `/Users/jackgao/IdeaProjects/surge-server/`
> 分支: `V1.9`

## 项目概述

`surge-server` 是一个基于 Spring Boot 的微服务架构后端项目。

## 模块文档

- [[问卷调查模块]] - 问卷创建、分享、填写、统计完整流程

## 技术栈

- Java
- Spring Boot
- Spring Cloud
- MyBatis
- MySQL
- Redis
- Docker
- Kubernetes

## 服务架构

```
surge-server/
├── blade-auth/          # 认证服务
├── blade-common/        # 公共组件
├── blade-gateway/       # 网关服务
├── blade-service/       # 业务服务
├── blade-service-api/   # API 接口
├── surge-auth/          # Surge 认证
├── surge-common/        # Surge 公共组件
├── surge-component/     # Surge 组件
├── surge-flyway/        # 数据库迁移
├── surge-gateway/       # Surge 网关
└── surge-mvp/           # MVP 业务服务
```

## 相关链接

- [[待办事项]]
- [[会议纪要]]
- [[技术决策记录]]
