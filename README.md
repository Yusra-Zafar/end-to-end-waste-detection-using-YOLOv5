# End-to-end Waste Detection using YOLOv5

- added the folder structure
- added the readme file
- created requirements.txt file
- created setup.py file
- create and annotate data
- perform google colab notebook experiments
- created log module to track all the progress with timestamps
- created exception module to define custom exceptions with all the details, for easy debugging

```
Errors I got: 
1. from from_root import from_root
ModuleNotFoundError: No module named 'from_root'

FIX: Installed from-root

2. AttributeError: module 'datetime' has no attribute 'now'

FIX: import datetime class directly from the module datetime

3. Some formatting and identation errors :)
```