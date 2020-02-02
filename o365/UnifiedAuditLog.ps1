
    $UserCredential = Get-Credential
    $Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection
    Import-PSSession $Session -DisableNameChecking
    $OutputFile = ".\UnifiedAuditLog_FULL.csv"
    $Today = Get-Date -Date (Get-Date -Format “yyyy-MM-dd”)
    $intDays = 90
    For ($i=0; $i -le $intDays; $i++){
      For ($j=23; $j -ge 0; $j--){
        $StartDate = ($Today.AddDays(-$i)).AddHours($j)
        $EndDate = ($Today.AddDays(-$i)).AddHours($j + 1)
        $Audit = Search-UnifiedAuditLog -StartDate $StartDate -EndDate $EndDate -ResultSize 5000
        $ConvertAudit = $Audit | Select-Object -ExpandProperty AuditData | ConvertFrom-Json
        $ConvertAudit | Select-Object CreationTime,UserId,Operation,Workload,ObjectID,SiteUrl,SourceFileName,ClientIP,UserAgent | Export-Csv $OutputFile -NoTypeInformation -Append
        Write-Host $StartDate `t $Audit.Count
      }
    }

