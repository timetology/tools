# Tools
## Host Forensics

### Windows
#### Zimmerman
* https://ericzimmerman.github.io/#!index.md
#### $MFT
* https://github.com/dkovar/analyzeMFT
* https://github.com/EricZimmerman/MFTECmd (Source - See [Zimmerman Section](https://github.com/timetology/tools/blob/master/README.md#zimmerman) for downloads)
* https://github.com/EricZimmerman/MFT (Source - See [Zimmerman Section](https://github.com/timetology/tools/blob/master/README.md#zimmerman) for downloads)
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
