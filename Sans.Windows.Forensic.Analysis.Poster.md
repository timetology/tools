Notes based on the Sans DFIR Windows Forensic Analysis Poster - http://dfir.to/GET-FREE-DFIR-POSTER

# $MFT Analysis
* https://ericzimmerman.github.io - [MFTECmd](https://github.com/EricZimmerman/MFTECmd), MFTExplorer
* https://github.com/dkovar/analyzeMFT

# Program Execution
## Shimcache (AppCompatCache - Application Compatability Cache)
### Description
* Windows Application Compatibility Database is used by Windows to identify possible application compatibility challenges with executables.
* Tracks the executables file name, file size, last modified time, and in Windows XP the last update time
### Location
#### XP
SYSTEM\CurrentControlSet\Control\SessionManager\AppCompatibility
#### Win7/8/10:
SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache

`C:\Windows\system32\config\SYSTEM`
### Interpretation
Any executable run on the Windows system could be found in this key. You can use this key to identify systems that specific malware was executed on. In addition, based on the interpretation of the time-based data you might be able to determine the last time of execution or activity on the system.
* Windows XP contains at most 96 entries
  * LastUpdateTime is updated when the files are executed
* Windows 7 contains at most 1,024 entries
  * LastUpdateTime does not exist on Win7 systems
* Win7+ Timestamp is Last Modified of File

## Amcache

## RecentFileCache
## User Assist
## Prefetch
## Windows 10 Timeline
## System Resource Usage Monitor (SRUM)
## Last Visited MRU
## Jump Lists

# File / Folder Opening

# Account Usage
# File Download

# Deleted File of File Knowledge

# Network Activity / Physical Location

# Browser Usage

# External Device / USB Usage
