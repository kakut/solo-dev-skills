# Solo Dev Skills

**一个开发者，六个技能。从想清楚，到做出来，再到下次接着做。**

[English](README.en.md) · [使用指南](docs/guide.zh-CN.md) · [验证状态](VALIDATION.md) · [MIT](LICENSE)

`0.1.0-alpha.1`：可安装的实验初版。已做发布前结构检查，尚未经过真实项目、多 Agent 团队或长期记忆恢复验证。欢迎用真实案例改进，当前不承诺省 token、自动唤醒或不会丢失上下文。

## 六个技能

| 技能 | 中文名 | 用途 |
| --- | --- | --- |
| [solo-ask](skills/solo-ask/SKILL.md) | 问清楚 | 有限追问，确定目标、范围、关键取舍和验收 |
| [solo-plan](skills/solo-plan/SKILL.md) | 拆计划 | 拆成可验证的小任务，明确依赖、归属和实施顺序 |
| [solo-build](skills/solo-build/SKILL.md) | 做实现 | 持续完成约定功能，以实际检查证明行为 |
| [solo-debug](skills/solo-debug/SKILL.md) | 查故障 | 复现、收集证据、定位原因、修复与回归 |
| [solo-review](skills/solo-review/SKILL.md) | 验成果 | 对照需求审查真实改动，区分报告、验收和集成 |
| [solo-memory](skills/solo-memory/SKILL.md) | 续上下文 | 保存、恢复、整合项目进度、决策和未完成事项 |

技能可以单独安装。每个文件夹包含所需参考资料，无需安装其他五个技能。一个 Agent 可以使用全部技能，多个角色也可以共用同一技能。

## 安装

仓库采用普通 `SKILL.md` 文件夹结构，运行技能不需要额外 API key、Python 或后台服务。代理宿主本身仍需正常配置。

下载仓库或克隆：

```bash
git clone https://github.com/kakut/solo-dev-skills.git
```

将 `skills/` 下需要的**完整文件夹**复制到宿主支持的技能目录。以 Codex 为例，项目级目录为 `<项目>/.agents/skills/`，个人级目录为 `~/.agents/skills/`。已有同名技能时先比较，不要直接覆盖。安装路径依据 [Codex 官方技能说明](https://learn.chatgpt.com/docs/build-skills)。

例如复制 `skills/solo-ask/` 后，保留其中的 `SKILL.md`、`references/`、`agents/`。开始新会话，确认技能已被发现。其他宿主需采用其支持的安装位置和调用方式，本项目尚未实测跨宿主兼容性。

## 怎么用

```text
用 $solo-ask 帮我想清楚这个付费功能，只问影响当前交付的问题。
用 $solo-plan 把需求拆成可逐步交付的任务，判断哪里适合并行。
用 $solo-build 完成第一项，持续做到相关检查通过。
用 $solo-debug 查清重复通知的原因，并用原场景验证修复。
用 $solo-review 审查本次改动，重点找漏做、做错和实际风险。
用 $solo-memory 保存当前进度，记录未提交改动和下一步。
用 $solo-memory 恢复项目上下文，然后继续已授权的下一项任务。
```

`save / resume / reconcile` 是 memory 的操作意图，可用自然语言表达，并非本仓库提供的 shell 命令。

小改动直接 build；模糊功能先 ask，再按需 plan；故障直接 debug；现有 PR 可以直接 review。阶段切换不自动增加审批。技能遵守用户指令、项目规则和宿主权限，沿用已有授权。

## 单人与团队

支持的设计包括单 Agent、原生子代理、独立任务会话以及已有图编排器的派单。真实可用范围取决于宿主工具；本仓库提供工作约定，未提供消息服务器或图运行时。

团队工作采用明确任务、执行批次、输入版本、文件归属和可检查结果。复用已有协调者；执行者处理分配范围。旧批次回报不会自动覆盖新进度。局部完成、报告送达、验收通过、集成完成分别核对。

工程要求、团队人数与模型选择分别决定。长期自用不代表需要复杂架构；角色名单也不代表每个角色都要启动。

## 项目记忆

优先复用已有文档和任务系统。必要时建立 `.agent-memory/`，用短状态、重要决策和增量检查点延续工作。团队成员写自己的检查点，由指定汇总者维护共享状态。不同 worktree 不假定共享文件。

可迁移项目知识与本机私有会话绑定分开。恢复时核对真实代码、任务批次和证据。技能不会自动读取所有聊天，也不能恢复从未保存的信息；关键阶段主动保存比等到 token 耗尽可靠。

## 开发与验证

维护工具需要 Python 3.10+，只用标准库：

```bash
python3 scripts/sync_references.py --check
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

修改 `shared/` 后运行 `python3 scripts/sync_references.py` 更新各技能携带的副本。结构检查不证明 Agent 行为正确；参见 [行为案例](tests/behavioral-cases.json) 和 [评估方法](tests/behavioral-evaluation.md)。

## 来源

吸收 Matt Pocock 的工程技能思想与 Codex Commander 的团队协作经验，针对个人开发者重写并组织为六个入口。详细说明见 [NOTICE](NOTICE.md)。本项目非 OpenAI 官方产品，也不代表参考作者认可本实现。
