# LAB 4 — Multi HR Agent

This lab demonstrates how to import and work with the Multi HR Agent which composes smaller HR-related agents (for example: general knowledge and leave management).

**Prerequisites:**
- `orchestrate` CLI installed and configured and available on your `PATH`.
- A working shell (this repo was developed on Linux; examples use the `fish` shell).

**Files of interest:**
- Agent manifest: `agent/HR_Agent.yaml`

**Import the agent**
1. Change into the `agent` folder where the agent manifest lives:

```fish
cd LAB_4_MULTI_HR_AGENT/agent
```

2. Import the agent using the `orchestrate` CLI:

```fish
orchestrate import agent -f HR_Agent.yaml
```

This command tells the orchestrator to create (or update) the agent described in `HR_Agent.yaml`. Run it from inside the `agent` folder so the relative paths in the YAML (if any) resolve correctly.

**What to expect**
- The CLI should print a success message if the import completes.
- The imported agent will reference/configure the smaller agents (e.g., general knowledge, leave management) as defined in the YAML.
- You can verify the agent in your orchestrator's UI or using any CLI commands your orchestrator exposes to list/describe agents.

**Troubleshooting**
- `file not found` or `no such file`: ensure you are in `LAB_4_MULTI_HR_AGENT/agent` and that `HR_Agent.yaml` exists.
- YAML validation errors: open `HR_Agent.yaml` and check for indentation or schema issues.
- Permission errors: ensure you have rights to run the `orchestrate` binary.

**Next steps**
- After a successful import, test the agent end-to-end: send a sample query, verify responses, or check logs for integrated small agents.
- Inspect `agent/HR_Agent.yaml` to see how the agent composes other agents and what credentials or endpoints are required.