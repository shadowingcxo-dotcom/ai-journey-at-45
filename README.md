# AI Journey at 45 — Road to OpenAI

《45岁学AI》重启版 · 2026-11-27。第一目标是 OpenAI 全栈软件工程及企业内部应用工程，第二目标是 Anthropic Software Engineer, Business Technology。内部编号用 R2-EP001 至 R2-EP100，公开视频标题使用新版英文系列名加 EP 编号。

## 从哪里开始

[100集课程目录](ROADMAP.md) · [进度与作品登记](PROGRESS.md) · [EP001 动手课](episodes/ep001/README.md)

主线项目是内部请求工作台。一个人提交业务请求，另一人处理请求并留下可审计的记录。数据使用虚构样例。后续加入 AI 建议、权限和工具集成，另做一个可以独立使用的小产品。用真实用户需求校正设计，公开材料用匿名概括和合成数据。

## 招聘要求如何落实

| 岗位依据（2026-11-27 核对） | 需要练习的工作 | 应能展示的证据 |
|---|---|---|
| [OpenAI · Full Stack Software Engineer, Sales Platform](https://openai.com/careers/full-stack-software-engineer-sales-platform-san-francisco/) | 构建内部 Web 应用、集成和共享平台能力，处理敏感信息、数据完整性与可靠性 | 一条前后端贯通的真实流程、权限测试、失败恢复记录、架构取舍 |
| [OpenAI · Capacity Systems Software Engineer](https://openai.com/careers/capacity-systems-software-engineer-san-francisco/) | 将跨部门表格流程变成可靠的软件，与实际使用者核对需求 | 流程图、用户验收、性能或时间指标与可复现实测 |
| [Anthropic · Software Engineer, Business Technology](https://job-boards.greenhouse.io/anthropic/jobs/5400153008) | 用 Python、TypeScript、React 端到端交付内部产品，理解使用者需求并验证效果 | 从访谈到原型、部署、反馈、迭代的案例，以及本人可以现场解释和修改的实现 |

课程产出可作为应聘证据。到 EP100 逐项评价能力、经验与缺口，招聘要求届时复核。

## 每集工作方式

1. 先说明一个用户问题、一个可观察的成功条件。学习者先预测并动手；遇到阻碍时，导师依次给定位问题、线索、局部示例。
2. 在 episodes/epNNN/ 保存英文 notes.md 和相关源码，跨集复用的源码可用相对路径及 Git 提交定位。笔记写预测、实际结果、调试过程、本人工作与 AI 协助。测试集也保留对应测试代码或重现案例。
3. 学习者亲自运行、观察、解释，再独立完成一个小变式。将证据、作品和下一步填入进度表。完成课程准备、录完视频和掌握技能分别登记。
4. 每十集做一次陌生任务：独立实现、复现并修复一个问题、解释一个设计选择；每项记“独立完成 / 提示后完成 / 待补”。写英文复盘，记录最薄弱项和重测任务。只有独立演示后才记为掌握。
5. GitHub 作品集仅从本独立仓库发布。提交前查看暂存差异与 Git 作者邮箱，使用公开身份或 GitHub noreply 邮箱。API 密钥通过环境变量注入；使用合成资料，检查日志、测试夹具、截图与 Git 历史。OBS 只捕获课程窗口，录后查画面、声音、通知和身份信息，发现泄露先撤换素材；实际外泄的密钥立即轮换。
6. 新版 GitHub 远端和 YouTube 系列入口在进度页登记，发布成功后补公开链接。上传核对新版系列名、集数、哈希及已有视频，旧版上传队列独立运行。

## 旧成果索引

旧版路线 AI-Learning-100-Episode-Roadmap.md 与 state.json 保存在原 youtube-ai-series 本地档案；NextWordLab（model.py、server.py、index.html）和 TinyTransformer（predict.py）保存在原 Documents/Codex 目录。可用作已有作品与能力参照。新版从零登记学习证据。
