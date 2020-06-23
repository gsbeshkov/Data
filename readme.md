Techical assesment 
==================

For the black box recorder we are using a specific configuration file called `recorder-config.xml`. For the test cases, we need an application that constructs all data structures from the `recorder-config.xml`.  The pseudocode implementation would look like:
```
class App:
    
    def __init__(self):
        self.framedata
        self.logserver
        self.heartbeat
        ....
        self.plugins = [......]
```
or use any design by your liking. 
For reading `xml` you may want to learn a bit how to use `python`'s xml module.

Your tasks:
==========
- You have to use xml module in python to parse the xml file.
- You have to design `class`-es for all tags in xml (ex. FrameData) 
```
<FrameData
    header="32"
    channels="32"
    samplesPerChan="16"
/>

class FrameData:
    def __init__(self, ...):
        self.header
        self.channels
        self.samplesPerChan
```
- You have to use `Facade pattern` to group all in `Application.py` that will init all classes after parsing xml file.
- We have tag `<Plugin>` which can appear multiple times. We need every plugin to have the corresponing class and the `App` to hold an array or a dictionary, your choice of those, so we can easily traverse the plugins.
- `Plugin` must have a function `put_data()` that can store in `Plugin` class some data, `string`, `array`, `int`, whatever you design.

Extra credits:
=============
(Difficutly Level: 5)
Extra credits will be given if a `class PluginManager` is created and can traverse to `class Plugin`. For this, you may want to implement a `linked list` 

Time limit (1 month)

Enjoy!
