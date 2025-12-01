# LAB 4 — Multi HR Agent

This lab shows how to import and configure the Multi HR Agent, which routes HR-related queries to smaller sub-agents (for example: general knowledge and leave management).

There are two ways to import the agent:

## Approach 1 — Import via UI (recommended for visual workflows)
  - Open the orchestrator web UI and go to the build/agents section (hamburger menu → Build).
  ![Click hamburger](./images/01.png)
  - Click **Create agent** and enter a name `HR_Agent`.
  - For the agent description, use description like this:

    ```text
    You are the central AI HR Orchestrator, acting as the primary router for employee and manager queries.
    Your sole responsibility is to route the user's query to the single most appropriate sub-agent. You have no tools and cannot perform actions yourself.
    ```

  ![agent base description](./images/02.png)

  - In the `Agents` section, click **Add agent** → **Local instance** and select the sub-agents to include (for example: `general_agent`, `langflow_agent_openapi_python`).

  ![Click Local instance](./images/03.png)
  ![add general](./images/04.png)
  ![add langflow](./images/05.png)

  - In the `Behavior` (or instructions) field, add global routing rules and style guidance. Example:

    ```text
    Important Global Rules

    Role
    - You are a router/orchestrator only. You have NO tools.
    - For every query, route to exactly one sub-agent that can handle it.
    - Respond in the language of the user's query (English or Thai).

    Routing Map
    - Leave / time-off (requests, balances, approvals) → langflow_agent_openapi_python
    - Policies & general HR info (policies, handbook, FAQ) → general_agent
    - Other HR topics (compensation, payroll, benefits, tax) → general_agent

    Style & Output
    - Be professional and concise.
    - Prefer compact, structured summaries (Markdown table or JSON) when needed.
    ```
---

## Approach 2 — Import via CLI (scriptable and repeatable)

**Prerequisites**
- `orchestrate` CLI installed and configured on your `PATH`.
- Shell examples here use the `fish` shell on Linux.

**Files of interest**
- Agent manifest: `agent/HR_Agent.yaml`

**Import the agent (CLI)**
1. Change to the `agent` folder:

```fish
cd LAB_4_MULTI_HR_AGENT/agent
```

2. Run the import command:

```fish
orchestrate import agent -f HR_Agent.yaml
```

Run this from the `agent` folder so any relative paths in the YAML resolve correctly.

**What to expect**
- The UI or CLI should confirm a successful import.
- The imported agent will be configured to route to the specified sub-agents.
- Verify the agent via the orchestrator UI or CLI list/describe commands.

**Troubleshooting**
- `file not found`: ensure you're in `LAB_4_MULTI_HR_AGENT/agent` and `HR_Agent.yaml` exists.
- YAML validation errors: check `HR_Agent.yaml` for syntax/indentation issues.
- Permission errors: confirm you can execute the `orchestrate` binary.

**Next steps**
- After import, exercise the agent with sample queries and review logs or responses from sub-agents.
- Inspect `agent/HR_Agent.yaml` to confirm routing, agent names, and any required credentials or endpoints.