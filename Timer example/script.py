from datetime import datetime

def main():
  console.info("Recipe has started!")

local_event_Timer = LocalEvent({'group': 'Timers', 'schema': {'type': 'string'}})

def update_current_time():
  time = datetime.now()
  time_now = time.strftime("%H:%M:%S")
  local_event_Timer.emit(time_now)
  
timer_timer = Timer(update_current_time, 0.5)
  


