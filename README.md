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

| Skill           | 来源                                                                                                     |
| --------------- | -------------------------------------------------------------------------------------------------------- |
| designprompt    | [GitHub](https://github.com/ttmouse/skills/tree/main/designprompt)                                       |
| frontend-design | [GitHub](https://github.com/anthropics/skills/tree/main/skills/frontend-design)                          |
| ui-skills       | [GitHub](https://github.com/ibelick/ui-skills/tree/main/src)                                             |
| ui-ux-pro-max   | [GitHub](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/main/.claude/skills/ui-ux-pro-max) |

### Best Practices

| Skill                 | 来源                                                                                         |
| --------------------- | -------------------------------------------------------------------------------------------- |
| react-best-practices  | [GitHub](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices)  |
| web-design-guidelines | [GitHub](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) |

---

<a name="add-skill"></a>
## 添加新 Skill

```bash
# 克隆 skill 仓库到 skills/ 目录
git clone <skill-repo-url> skills/<skill-name>
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
