# Interaction of Frontend and Backend
Backend will be written in Python, and send a string with the following structure:

### To Frontend
    HP\n
    \tAbility (Text Descriptor)\n
    \tAbility (Text Descriptor)\n
    \tAbility (Text Descriptor)\n
    \tActive Buffs <- list of strings
    AI Ability (Text Descriptor)
    \tActive AI Buffs <- list of strings
### From Frontend
Ability
### Synchronization
Using a mutex as the first line of the file. If 0, write state and switch to 1.

If 1, write output and switch to 0
# Rules
Buffs will last for 3 rounds