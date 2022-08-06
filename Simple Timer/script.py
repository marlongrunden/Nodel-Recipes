###
# This recipe allows the user to define multiple remote actions that trigger at a definable time every day.
#
# TO DO
# - Day of the week selection
###

# Import necessary python libraries
from datetime import datetime
from datetime import time

# Define parameters and their schemas
param_members = Parameter(
    {'title': 'Timers', 'schema': 
        {'type': 'array', 'items':
            {'type': 'object', 'properties':
                {
                  'targetNode': {'title': 'Target Node', 'type': 'string', 'required': True, 'order': 1},
                  'remoteAction': {'title': 'Remote Action', 'type': 'string', 'required': True, 'order': 2},
                  'triggerHour': {'title': 'Trigger Hour', 'type': 'integer', 'required': True, 'order': 3},
                  'triggerMinute': {'title': 'Trigger Minute', 'type': 'integer', 'required': True, 'order': 4},
                  'repeatDaily': {'title': 'Repeat Daily?', 'type': 'boolean', 'required': False, 'order': 5},
                }
            }   
        }   
    }
)


# Define a local event that displays the current time
local_event_currentTime = LocalEvent({'title': 'Current Time', 'group': 'Timers', 'schema': {'type': 'string'}})

# Defines the function that is run every second. It checks to see if the trigger time and current time are the same.
# If they are, it sends a call to the defined target node calling it's remote action
def trigger_events (arg = None):
  for parameters in lookup_parameter('members') or []:
    if(parameters != None):
      targetNode = parameters.get('targetNode')
      remoteAction = parameters.get('remoteAction')
      triggerTime = str(time((parameters.get('triggerHour')), (parameters.get('triggerMinute'))))
      timeObject = datetime.now()
      time_now = timeObject.strftime("%H:%M:%S")
      local_event_currentTime.emit(time_now)
      if(triggerTime == time_now):
        console.info("Triggering %s on node %s" % (remoteAction, targetNode))
        lookup_remote_action(str(targetNode) + str(remoteAction)).call()


# Main entry point
def main():
  console.info("Timer has started")
  main_timer = Timer(trigger_events, 1) # Defines a timer that triggeres every second, calling the trigger_event function
  
  # Create remote actions from the parameters 
  for parameters in lookup_parameter('members') or []:
    if(parameters != None):
      targetNode = parameters.get('targetNode')
      remoteAction = parameters.get('remoteAction')
      create_remote_action(str(targetNode) + str(remoteAction), None, targetNode, remoteAction)