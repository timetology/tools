Notes based on the Sans DFIR Windows Forensic Analysis Poster - http://dfir.to/GET-FREE-DFIR-POSTER
## ITEM
### Description
### Location
### Interpretation
### Tools

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
### Tools
* https://github.com/mandiant/ShimCacheParser
* https://ericzimmerman.github.io - AppCompatCacheParser
* https://github.com/timetology/ecat/tree/master/scripts/rmt/3_Aggregators

## Amcache
### Description
ProgramDataUpdater (a task associated with the Application Experience Service) uses the registry file Amcache.hve to store data during process creation
### Location
Win7/8/10:
C:\Windows\AppCompat\Programs\Amcache.hve
### Interpretation
* Amcache.hve – Keys = Amcache.hve\Root\File\{Volume GUID}\####### 
* Entry for every executable run, full path information, File’s $StandardInfo Last Modification Time, and Disk volume the executable was run from
* First Run Time = Last Modification Time of Key
* SHA1 hash of executable also contained in the key
### Tools
* https://ericzimmerman.github.io - AmcacheParser
* https://github.com/williballenthin/python-registry/blob/master/samples/amcache.py
* https://github.com/timetology/ecat/tree/master/scripts/rmt/3_Aggregators



## RecentFileCache
### Description
### Location
C:\Windows\AppCompat\Programs\RecentFilecache.bcf
### Interpretation
### Tools


## User Assist
### Description
### Location
### Interpretation
### Tools

## Prefetch
### Description
### Location
### Interpretation
### Tools

## Windows 10 Timeline
### Description
### Location
### Interpretation
### Tools

## System Resource Usage Monitor (SRUM)
### Description
### Location
### Interpretation
### Tools

## Last Visited MRU
### Description
### Location
### Interpretation
### Tools

## Jump Lists
### Description
### Location
### Interpretation
### Tools
# File / Folder Opening

# Account Usage
# File Download

# Deleted File of File Knowledge

# Network Activity / Physical Location

# Browser Usage

# External Device / USB Usage
