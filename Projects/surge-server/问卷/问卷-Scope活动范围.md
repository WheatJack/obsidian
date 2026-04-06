---
tags:
  - surge
  - questionnaire
  - scope
date: 2026-04-06
parent: "[[问卷调查模块]]"
---

# Scope 活动范围

## 三种范围

| scope | 说明 | App用户 | 微信客户 |
|-------|------|---------|--------|
| 1 | 仅客户 | 只能分享，不展示填写按钮 | 可以填写 |
| 2 | 客户和用户 | 可分享 + 可填写 | 可以填写 |
| 3 | 仅用户 | 可填写 | 不可访问(restricted页) |

## 后端处理

- 保存时自动用 `SecureUtil.getTenantId()` 填入 `target_tenants`
- 前端不需要传 tenantId 和 target_tenants
- App列表查询按 `tenant_id` 精确匹配

## App端展示逻辑

- scope=1：只展示"分享给客户"按钮
- scope=2：展示"分享给客户" + "立即填写"
- scope=3：只展示"立即填写"
- 已填写：按钮变灰显示"已填写"

## 微信端权限检查

```
加载问卷 → 调trackingMaterial → 获取customerType
├── scope=3 + customerType=2(客户) → /survey/restricted
├── scope=1 + customerType=1/2 → 允许填写
└── scope=2 + customerType=1/2 → 允许填写
```
