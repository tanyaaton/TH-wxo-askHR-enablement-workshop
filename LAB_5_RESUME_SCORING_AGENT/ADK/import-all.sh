set -x

orchestrate env activate trial-env
orchestrate tools import -k flow -f tools/resume_scoring_tool_6080yP/resume_scoring_tool_6080yP.json
orchestrate agents import -f agents/resume_scoring_agent.yaml


