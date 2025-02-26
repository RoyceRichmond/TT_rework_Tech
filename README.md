# TT_rework_Tech
Miscellaneous scripts for TT submition

## executing the replacement of technology
The python script needs two parameters, the directory where it will find the .mag files to replace and a flag, when set to true it replaces the node to 130A, when set to false it replaces the node to 130B
```shell
python3 replace_120A.py xschem/skywater_submission/ --flag False 
```
