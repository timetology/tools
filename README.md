# Awesome Lists of Tools
* https://github.com/meirwah/awesome-incident-response
* https://github.com/Cugu/awesome-forensics
* https://awesomedfir.com/dfir-tooling
* https://awesomeopensource.com/projects/incident-response
* https://dfirdiva.com/tools-and-distros/
* https://www.dfir.training/tools

# Tools

## Host Forensics

### Windows
#### Evidence of Execution
* https://github.com/timetology/tools/blob/master/Sans.Windows.Forensic.Analysis.Poster.md#program-execution
#### Zimmerman
* https://ericzimmerman.github.io/#!index.md
#### Triage
* Kape
* Wintriage - https://www.securizame.com/wintriage-the-triage-tool-for-windows-dfirers/
* Live Response - https://www.brimorlabs.com/tools/
* Ir Triage - https://github.com/AJMartel/IRTriage
* Cylr - https://github.com/orlikoski/CyLR
* cdqr - https://github.com/orlikoski/CDQR
* IR Rescue - https://github.com/diogo-fernan/ir-rescue
* https://github.com/TazWake/Useful-Scripts-Etc/blob/master/DFIR_Collection_Guide.md
#### $MFT
* https://github.com/timetology/tools/blob/master/Sans.Windows.Forensic.Analysis.Poster.md#mft-analysis
* https://github.com/dkovar/analyzeMFT
* https://github.com/EricZimmerman/MFTECmd (Source - See [Zimmerman Section](https://github.com/timetology/tools/blob/master/README.md#zimmerman) for downloads)
* https://github.com/EricZimmerman/MFT (Source - See [Zimmerman Section](https://github.com/timetology/tools/blob/master/README.md#zimmerman) for downloads)
#### $USNJRNL - $USN Journal
* http://forensicinsight.org/wp-content/uploads/2013/07/F-INSIGHT-Advanced-UsnJrnl-Forensics-English.pdf
* https://github.com/PoorBillionaire/USN-Journal-Parser
#### Program Execution
* https://github.com/timetology/ecat/tree/master/scripts/rmt
* https://ericzimmerman.github.io/#!index.md
#### Registry
* https://github.com/keydet89/RegRipper3.0
#### RDP
##### RDP Bitmap Cache
* https://www.allthingsdfir.com/do-you-even-bitmap-cache-bro/
* https://countuponsecurity.com/tag/rdp-bitmap-cache/
* https://github.com/ANSSI-FR/bmc-tools
* https://security.opentext.com/appDetails/RDP-Cached-Bitmap-Extractor
#### Shellbags
##### Notes
http://windowsir.blogspot.com/2012/08/shellbag-analysis.html
https://www.4n6k.com/2013/12/shellbags-forensics-addressing.html
https://volatility-labs.blogspot.com/2012/09/movp-32-shellbags-in-memory-setregtime.html
#### LNK
* https://github.com/silascutler/LnkParse
* https://github.com/HarmJ0y/pylnker
### Timeliner
* https://github.com/log2timeline/plaso
### Yara
* https://github.com/Neo23x0/Loki
### Memory
* Volatility
* https://github.com/andreafortuna/autotimeliner
* https://github.com/andreafortuna/malhunt
* https://www.fireeye.com/services/freeware/redline.html
#### Logs
* [Log Parser](https://www.microsoft.com/en-us/download/details.aspx?id=24659)
* [Event Log Explorer](https://eventlogxp.com/)
##### Windows User Access Logs (UAL)
`C:\Windows\System32\LogFiles\SUM`
* https://svch0st.medium.com/windows-user-access-logs-ual-9580f1100635
* https://github.com/brimorlabs/KStrike
* https://github.com/EricZimmerman/Sum
* 
### Browsers
#### Chrome
##### Notes
* https://resources.infosecinstitute.com/topic/browser-forensics-google-chrome/
##### Locations
```
Default Locations:
Windows XP:	\[userdir\]\Local Settings\Application Data\Google\Chrome\User Data
Vista/7/8/10:	\[userdir\]\AppData\Local\Google\Chrome\User Data
Linux:	\[userdir\]/.config/google-chrome
OSX/macOS:	\[userdir\]/Library/Application Support/Google/Chrome/Default
iOS:	\Applications\com.google.chrome.ios\Library\Application Support\Google\Chrome
Android:	/userdata/data/com.android.chrome/app_chrome
```
##### Links
* https://github.com/obsidianforensics/hindsight

#### Brave
##### Locations
```
Default Locations:
Vista/7/8/10:	\[userdir\]\AppData\Roaming\brave
Linux:	\[userdir\]/.config/brave
OSX/macOS:	\[userdir\]/Library/Application Support/brave
```
##### Links
* https://github.com/obsidianforensics/hindsight

### Bits
* https://dfrws.org/presentation/finding-your-naughty-bits/
* https://mgreen27.github.io/posts/2018/02/18/Sharing_my_BITS.html
#### Locations
```
%%ALLUSERSPROFILE%%\Microsoft\Network\Downloader\*
C:\ProgramData\Microsoft\Network\Downloader\*
```
Win10+
```
C:\ProgramData\Microsoft\Network\Downloader\qmgr.db
```
Pre-Win10
```
C:\ProgramData\Microsoft\Network\Downloader\qmgr0.dat
C:\ProgramData\Microsoft\Network\Downloader\qmgr1.dat
```
#### Parsers
* https://github.com/ANSSI-FR/bits_parser
* https://github.com/fireeye/BitsParser
## Malware Analysis
### Dynamic Analysis
* https://github.com/Rurik/Noriben
### Static Analysis
* https://www.fireeye.com/blog/threat-research/2021/07/capa-2-better-stronger-faster.html
* https://github.com/fireeye/capa

## Peristence
* https://www.andreafortuna.org/2017/07/06/malware-persistence-techniques/
