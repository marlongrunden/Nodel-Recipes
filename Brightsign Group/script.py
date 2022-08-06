# An example of a group node that controls multiple brightsigns nodes (from the official nodel recipes repo) which in turn control brightsigns via UDP

def play01(arg = None):
  print("Playing Clip 1")
  for parameters in lookup_parameter('members') or []:
    if(parameters != None):
      targetNode = parameters.get('targetNode')
      remoteplay1command= parameters.get('play1command')
      lookup_remote_action(str(targetNode) + str(remoteplay1command)).call()

def play02(arg = None):
  print("Playing Clip 2")
  for parameters in lookup_parameter('members') or []:
    if(parameters != None):
      targetNode = parameters.get('targetNode')
      remoteplay2command= parameters.get('play2command')
      lookup_remote_action(str(targetNode) + str(remoteplay2command)).call()

param_members = Parameter(
    {'title': 'Management Node Member', 'schema': 
        {'type': 'array', 'items':
            {'type': 'object', 'properties':
                {
                    'targetNode': {'title': 'Target Node', 'type': 'string', 'required': True, 'order': 1},
                    'play1command': {'title': 'Play 1 Command', 'type': 'string', 'required': True, 'order': 2},
                    'play2command': {'title': 'Play 2 Command', 'type': 'string', 'required': True, 'order': 3},
                }
            }   
        }   
    }
)

def main(arg = None):
  print("Node started...")
  create_local_action("Play 1", play01, None)
  create_local_action("Play 2", play02, None)
  
  for parameters in lookup_parameter('members') or []:
    if(parameters != None):
      targetNode = parameters.get('targetNode')
      remoteplay1command = parameters.get('play1command')
      create_remote_action(str(targetNode) + str(remoteplay1command), None, targetNode, remoteplay1command)
  
  for parameters in lookup_parameter('members') or []:
    if(parameters != None):
      targetNode = parameters.get('targetNode')
      remoteplay2command = parameters.get('play2command')
      create_remote_action(str(targetNode) + str(remoteplay2command), None, targetNode, remoteplay2command)