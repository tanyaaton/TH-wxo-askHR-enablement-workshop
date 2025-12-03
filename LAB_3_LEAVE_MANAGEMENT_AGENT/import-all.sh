set -x

orchestrate env activate trial-env
orchestrate tools import -k openapi -f tools/langflow_leave_balance.yml
orchestrate agents import -f agents/langflow_agent.yml


