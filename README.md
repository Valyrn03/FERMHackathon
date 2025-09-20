# Interaction of Frontend and Backend
Backend will be written in Python, and send the following json file:
## File Structure
*for lock, the value is what should be written*

From Backend:

    lock: 1
    player_hp:
    abilities: []
    player_buffs: []
    ai_action: 
    ai_buffs: []

From Frontend:
    
    lock: 0
    action:
### Synchronization
Using a mutex as the first line of the file. If 0, write state and switch to 1.

If 1, write output and switch to 0
# Rules
Buffs will last for 3 rounds, they will not stack