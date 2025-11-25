set -x

orchestrate env activate trial-env
orchestrate tools import -k python -f tools/get_employee_leave_balance/get_employee_leave_balance.py -a langflow_secret
orchestrate agents import -f agents/langflow_agent.yml


