orchestrate env activate trial-env
orchestrate connections add -a langflow_secret
orchestrate connections configure -a langflow_secret --env draft -t team -k key_value
orchestrate connections configure -a langflow_secret --env live -t team -k key_value
orchestrate connections set-credentials \
  -a langflow_secret \
  --env draft \
  -e application_token=$ASTRA_TOKEN \
  -e organization_id=$ORG_ID
orchestrate connections set-credentials \
  -a langflow_secret \
  --env live \
  -e application_token=$ASTRA_TOKEN \
  -e organization_id=$ORG_ID