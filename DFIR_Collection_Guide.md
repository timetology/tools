# DFIR Disk Data Collection Guide

|Artefact | Location|
|---------|---------|
|Ntuser.dat |  C:\Users\(user name)| 
|USERCLASS.dat |  % USERPROFILE %\AppData\Local\Microsoft\Windows\UsrClass.dat| 
|SAM |  C:\Windows\System32\Config\SAM| 
|Outlook Mail |  %USERPROFILE%\AppData\Local\Microsoft\Outlook| 
|Skype (not skype for business) |  %USERPROFILE%\AppData\Roaming\Skype\(skype name)| 
|Browser Artefacts| | 
|IE 10 – 11 |  %USERPROFILE%\AppData\Local\Microsoft\Windows\WebCache\WebCacheV*.dat| 
|Firefox |  %USERPROFILE%\AppData\Roaming\Mozilla \Firefox\Profiles\(random text).default\places.sqlite Table:moz_annos| 
|Chrome |  %USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default\History| 
|Browser Session Restore | | 
|IE |  %USERPROFILE%\AppData\Local\Microsoft\Internet Explorer\Recovery| 
|Firefox |   %USERPROFILE%\AppData\Roaming\Mozilla \Firefox\Profiles\(random text).default\sessionrestore.js| 
|Chrome |  %USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default\ (Files = current session,  current tabs, last session, last tabs)| 
|Jump List |  %USERPROFILE%\AppData\Roaming\Microsoft\ Windows\Recent\AutomaticDestinations| 
|Prefetch |  C:\Windows\Prefetch| 
|Amcache.hve |  C:\Windows\AppCompat\Progress\Amcache.hve| 
|Link Files |  %USERPROFILE%\AppData\Roaming\Microsoft\Windows\Recent %USERPROFILE%\AppData\Roaming\Microsoft\Office\Recent| 
|Event Logs |  C:\Windows\system32\winevt\logs| 
|SRUM |  C:\Windows\System32\SRU| 
|Flash Player |  %APPDATA%\Roaming\Macromedia\FlashPlayer\#SharedObjects\(random profile pid)| 
