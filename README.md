# Hello Skills

<a name="about"></a>
## 关于 Agent Skills

**Agent Skills** 是一个简单、开放的格式，用于为 AI Agents 提供新的能力和专业知识。

### 核心价值

| 功能               | 说明                                        |
| ------------------ | ------------------------------------------- |
| **领域专业知识**   | 将专业知识打包成可重用指令                  |
| **新能力**         | 创建演示文稿、构建 MCP 服务器、分析数据集等 |
| **可重复工作流程** | 将多步骤任务转化为一致、可审计的流程        |
| **互操作性**       | 在不同 Agent 产品中重用相同 Skill           |

### 支持的平台

Gemini CLI、OpenCode、Cursor、Claude Code、Claude、OpenAI Codex 等

---

<a name="skills-list"></a>
## Skills 列表

### UI/Design

| Skill | 描述 | 来源 |
| ----- | ---- | ---- |
| designprompt | AI驱动的设计系统构建器。基于项目特征智能推荐最合适的设计风格（从30+专业设计系统中选择），自动应用完整的设计系统规范来实现界面。 | [GitHub](https://github.com/ttmouse/skills/tree/main/designprompt) |
| frontend-design | 创建独特、生产级的前端界面。避免通用的"AI审美"，注重排版、色彩、动效和创意设计，适用于网站、落地页、仪表盘等。 | [GitHub](https://github.com/anthropics/skills/tree/main/skills/frontend-design) |
| ui-skills | 为 agent 构建更好界面的约束规范。涵盖技术栈（Tailwind、framer-motion）、组件设计（可访问性、原语）、交互（对话框、加载状态）、动画（性能优化）、排版、布局和性能优化等方面的最佳实践。 | [GitHub](https://github.com/ibelick/ui-skills/tree/main/src) |
| ui-ux-pro-max | UI/UX设计智能助手。包含50种风格、21个配色板、50种字体搭配、20种图表类型，支持9种技术栈（React、Next.js、Vue等）。 | [GitHub](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/main/.claude/skills/ui-ux-pro-max) |

### Best Practices

| Skill | 描述 | 来源 |
| ----- | ---- | ---- |
| react-best-practices | Vercel Engineering 提供的 React 和 Next.js 性能优化指南。包含45条规则，涵盖消除瀑布流、Bundle优化、SSR性能等方面。 | [GitHub](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) |
| web-design-guidelines | Web界面设计规范审核。用于检查UI代码是否符合可访问性、无障碍设计等Web最佳实践。 | [GitHub](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) |
| skill-creator | 创建有效 Skills 的指南。涵盖技能设计原则、文件结构（SKILL.md、scripts、references、assets）、渐进式披露模式、以及从初始化到打包的完整创建流程。 | [GitHub](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |

### Cognitive & Mindset

| Skill | 描述 | 来源 |
| ----- | ---- | ---- |
| cross-domain-thinking-toolbox | 应用25种专业思维模型解决复杂问题。适用于：(1) 需要多角度思考的挑战，(2) 困于单一思路，(3) 需要创新解决方案，(4) 多利益相关方决策，(5) 理解复杂人类行为，(6) 打破认知偏见。 | 本地 |
| debog-yourself | 帮助用户识别和摆脱心理困境。当用户感到卡住、无法前进、陷入僵局或面临选择困难时使用。提供诊断框架（激活能量不足/糟糕的逃脱计划/自我困境）和具体策略。 | 本地 |
| deep-productivity | 深度工作生产力 mastery。通过三种工作类型框架（建设/维护/恢复）帮助用户建立可持续的深度工作习惯。仅需1小时/天即可产生有意义的目标进展。 | 本地 |
| learning-first-principles | 基于学习第一性原理的认知框架。提供学习方法诊断、效率评估和优化建议。核心原理链：自学→归纳总结→自我输出→表达重构→逻辑理解→实践。 | 本地 |
| retrospective-master | 专业复盘教练，基于 GRAI 复盘模型（Goal-Result-Analysis-Insight）引导用户进行结构化复盘。将经历转化为经验，将经验转化为能力。 | 本地 |
| mungers-lattice | 多学科分析引擎，使用查理·芒格的格栅思维模型。通过数学、物理、生物学、心理学和经济学等跨学科视角剖析生活 和商业决策。 | 本地 |

---

<a name="add-skill"></a>
## 添加新 Skill

```bash
# 使用 skills CLI 添加 skill
npx skills add https://github.com/hexbee/hello-skills
```

每个 Skill 需包含：
- `SKILL.md` - Skill 配置和指令文件
- 相关资源文件

---

<a name="resources"></a>
## 资源链接

- [Agent Skills 官方文档](https://agentskills.io)
- [Anthropic Skills 仓库](https://github.com/anthropics/skills)
- [技能规范 (Specification)](https://agentskills.io/specification)
- [skills NPM 包](https://www.npmjs.com/package/skills)
- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills)
