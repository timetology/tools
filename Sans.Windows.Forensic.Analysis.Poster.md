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
`SYSTEM\CurrentControlSet\Control\SessionManager\AppCompatibility`
#### Win7/8/10:
`SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache`
#### Win Disk Location
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
* https://github.com/keydet89/RegRipper3.0
* https://github.com/timetology/ecat/tree/master/scripts/rmt/3_Aggregators

## Amcache
### Description
ProgramDataUpdater (a task associated with the Application Experience Service) uses the registry file Amcache.hve to store data during process creation
### Location
Win7/8/10:
`C:\Windows\AppCompat\Programs\Amcache.hve`
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
From: http://journeyintoir.blogspot.com/2013/12/revealing-recentfilecachebcf-file.html
The RecentFileCache.bcf file on the other hand only contained references to programs that recently executed. The reason for this is because the RecentFileCache.bcf file is a temporary storage location used during the process creation. It appears this storage location is not used during all process creation; it's mostly used for those processes that spawned from executables which were recently copied or downloaded to the system.

Extensive testing was performed to shed light on the actions which lead to executables names being listed in the RecentFileCache.bcf file. The testing included executing the same program the following ways:

* executing program already on the system
* renaming and then executing the program already on the system
* executing the program from a removable media
* copying the program to the system and then executing it
* downloading the program with a web  browser and then executing it
* copying a different program that has an installation process and then executing it
### Location
`C:\Windows\AppCompat\Programs\RecentFilecache.bcf`
### Interpretation
### Tools
* https://github.com/prolsen/recentfilecache-parser
* https://ericzimmerman.github.io/ - RecentFileCacheParser

## User Assist
### Description
GUI-based programs launched from the desktop are tracked in the launcher on a Windows System.
### Location
#### Win7+
`C:\users\<user>\ntuser.dat`
#### Win XP
`C:\Documents and Settings\<user>\ntuser.dat`
#### NTUSER.DAT HIVE:
NTUSER.DAT\Software\Microsoft\Windows\Currentversion\Explorer\UserAssist\{GUID}\Count
### Interpretation
All values are ROT-13 Encoded • GUID for XP
- 75048700 Active Desktop • GUID for Win7/8/10
- CEBFF5CD Executable File Execution - F4E57C4B Shortcut File Execution
### Tools
* https://github.com/keydet89/RegRipper3.0
* https://github.com/tasoskoutlis/Automated-Forensic-Analysis/blob/master/plugins/userassist.py
* https://blog.didierstevens.com/programs/userassist/
## Prefetch
### Description
* Increases performance of a system by pre-loading code pages of commonly used applications. Cache Manager monitors all files and directories referenced for each application or process and maps them into a .pf file. Utilized to know an application was executed on a system.
* Limited to 128 files on XP and Win7
* Limited to 1024 files on Win8
* Format: (exename)-(hash).pf
* **Typically disabled by default on Servers & systems with SSD**
### Location
#### WinXP/7/8/10:
`C:\Windows\Prefetch`
### Interpretation
* Each .pf will include last time of execution, number of times run, and device and file handles used by the program
* Date/Time file by that name and path was first executed - Creation Date of .pf file (-10 seconds)
* Date/Time file by that name and path was last executed - Embedded last execution time of .pf file
  * Last modification date of .pf file (-10 seconds)
  * Win8-10 will contain last 8 times of execution
### Tools
* https://ericzimmerman.github.io/ - PECmd
* https://github.com/PoorBillionaire/Windows-Prefetch-Parser/blob/master/windowsprefetch/windowsprefetch.py
## Windows 10 Timeline
### Description
Win10 records recently used applications and files in a “timeline” accessible via the “WIN+TAB” key. The data is recorded in a SQLite database.
### Location
`C:\Users\<profile>\AppData\Local\ConnectedDevices Platform\<random-name-folder>\ActivitiesCache.db`


The catalog `Users\%profile name%\AppData\Local\ConnectedDevicesPlatform\` contains a CDP file with information about the last Windows 10 Timeline synchronization with the cloud (CNCNotificationUriLastSynced) and about the user ID (0b5569b899437c21 in the image below).


User activity information in Windows 10 Timeline is saved to the file ActivitiesCache.db with the path \Users\%profile name%\AppData\Local\ConnectedDevicesPlatform\L.%profile name%\.


ActivitiesCache.db is an SQLite database (version 3). Like any SQLite database, it has two auxiliary files: ActivitiesCache.db-shm and ActivitiesCache.db-wal.
Additional information about deleted records may be contained in unused space, freelists, and the WAL file.
### Interpretation
* Application execution
* Focus count per application
Links: 
* https://blog.group-ib.com/windows10_timeline_for_forensics
### Tools
* https://ericzimmerman.github.io/ - WxTCmd
* https://github.com/kacos2000/WindowsTimeline
## System Resource Usage Monitor (SRUM)
### Description
Records 30 to 60 days of historical system performance. Applications run, user account responsible for each, and application and bytes sent/received per application per hour.

### Location
SOFTWARE\Microsoft\WindowsNT\CurrentVersion\SRUM\Extensions {d10ca2fe-6fcf- 4f6d-848e-b2e99266fa89} = Application Resource Usage Provider C:\Windows\ System32\SRU\

#### SRUM Database & Software Hive
* SRU Database: `C:\Windows\system32\sru\SRUDB.dat`
* SOFTWARE HIVE: `C:\Windows\system32\config\SOFTWARE`

### Interpretation
Repairing the SRUDB.dat
When you run SrumECmd, you will likely encounter an error message that states the file is dirty.
1. Make a copy of the files within the .\SRU directory
2. Ensure the .\SRU directory itself is not Read Only. This can be done by right clicking on the directory itself, Properties, and unchecking Read Only if it is checked.
3. Open a PowerShell session as an Administrator in the directory where your copied files reside
4. Execute this command within the PowerShell Admin session: `esentutl.exe /r sru /i`
   1. https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh875546(v=ws.11)
5. Try running SrumECmd again against the location where these repaired files reside:
### Tools
* https://ericzimmerman.github.io/ - SrumECmd
* https://github.com/MarkBaggett/srum-dump

## Last Visited MRU
### Description
Tracks the specific executable used by an application to open the files documented in the OpenSaveMRU key. In addition, each value also tracks the directory location for the last file that was accessed by that application.
Example: Notepad.exe was last run using the C:\%USERPROFILE%\ Desktop folder
### Location
`C:\users\<user>\ntuser.dat`
#### XP:
NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedMRU
#### Win7/8/10: 
NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU
### Interpretation
Tracks the application executables used to open files in OpenSaveMRU and the last file path used.
### Tools
* https://github.com/keydet89/RegRipper3.0

## Jump Lists
### Description
### Location
### Interpretation
### Tools
* https://github.com/kacos2000/Win10/blob/master/JumpList/readme.md
* https://ericzimmerman.github.io/ - JLECmd, JumpList Explorer

## BAM / DAM (Windows Background Activity Moderator)
### Description
Windows Background Activity Moderator (BAM)
### Location
#### Win10
`C:\Windows\system32\config\SYSTEM`
* SYSTEM\CurrentControlSet\Services\bam\UserSettings\{SID} 
* SYSTEM\CurrentControlSet\Services\dam\UserSettings\{SID}
### Interpretation
Provides full path of the executable file that was run on the system and last execution date/time
### Tools
* https://github.com/keydet89/RegRipper3.0
* https://github.com/Ektoplasma/BamParser
* https://github.com/prolsen/bam
* https://github.com/kacos2000/Win10/blob/master/Bam/readme.md
* https://github.com/kacos2000/Win10/blob/master/Bam/bamoffline.ps1
#### Win10 v1809 & v1903
* https://github.com/kacos2000/Win10/blob/master/Bam/bamoffline1.ps1

## MuiCache (Not in the Poster but adding here anyway
### Description
Each time that you start using a new application, Windows operating system automatically extract the application name from the version resource of the exe file, and stores it for using it later, in Registry key known as the 'MuiCache'.
### Location
#### Win7+
`C:\users\<user>\ntuser.dat`
`C:\users\<user>\AppData\Local\Microsoft\Windows\usrclass.dat`

The location of the MUICache data in the registry prior to Windows Vista is: `HKEY_CURRENT_USER\Software\Microsoft\Windows\ShellNoRoam\MUICache`

Starting with Windows Vista, MUICache data is stored in `HKEY_CURRENT_USER\Software\Classes\Local\Settings\Software\Microsoft\Windows\Shell\MuiCache`
### Interpretation
Extracts the Last Write, name and data from the MuiCache in NTUSER.DAT or USRCLASS.DAT
https://openmuifile.com/muicache.html

### Tools
* https://github.com/timetology/ecat/blob/master/scripts/rmt/3_Aggregators/muicache.py
* https://www.nirsoft.net/utils/muicache_view.html

# File / Folder Opening

# Account Usage
# File Download

# Deleted File of File Knowledge

# Network Activity / Physical Location

# Browser Usage

# External Device / USB Usage
