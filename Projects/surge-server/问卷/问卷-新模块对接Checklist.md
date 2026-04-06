---
tags:
  - surge
  - questionnaire
  - checklist
  - template
date: 2026-04-06
parent: "[[问卷调查模块]]"
---

# 新模块对接 Checklist

如果后续要新增类似模块（如投票、签到等），按以下清单操作：

## 后端

- [ ] `MaterialConstant` 新增类型常量
- [ ] `ConsultationArticleServiceImpl.checkMaterialExists` 增加类型判断
- [ ] `ConsultationArticleServiceImpl` 4处消息构建增加类型分支
- [ ] 新增 `SurgeXxxMapper`（blade-instrument内，同库直查）
- [ ] 新增 `fillXxxInfo` 方法（填充标题+封面到消息JSON）
- [ ] `MessageEnum` 新增消息枚举（如有参与消息需求）

## 前端 surge-app

- [ ] `msgItem.vue` - `aroundText` computed 增加新flag的文案
- [ ] `interactionMsgItem.vue` - 增加新类型的消息卡片展示+跳转
- [ ] 消息头像区域的flag列表加上新类型

## 前端 surge-wechat

- [ ] 参照 `survey/index.vue` 的 `initHandle` 模式
- [ ] 调 `trackingMaterial` 时 `materialType` 用新类型
- [ ] 用 `customerType`（1=代理人，2=客户）判断身份

> [!warning] 不要用readerType
> `TrackingMaterialDto` 返回的是 `customerType`，不是 `readerType`。
> `readerType` 是活动详情接口里活动数据自带的字段。

## Nacos配置

- [ ] 分享链接域名：`xxx.share.baseUrl`（测试/生产不同）

## 数据库

- [ ] Flyway migration 建表
- [ ] 注意雪花ID → 前端JS精度问题 → Controller返回String
