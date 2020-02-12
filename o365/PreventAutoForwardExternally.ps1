# Block Inbox Rules from forwarding mail externally in your own Office 365 tenant using PowerShell
# https://gcits.com/knowledge-base/block-inbox-rules-forwarding-mail-externally-office-365-using-powershell/
Function Connect-EXOnline {
    $credentials = Get-Credential
    Write-Output "Getting the Exchange Online cmdlets"
    $session = New-PSSession -ConnectionUri https://outlook.office365.com/powershell-liveid/ `
        -ConfigurationName Microsoft.Exchange -Credential $credentials `
        -Authentication Basic -AllowRedirection
    Import-PSSession $session
}
Connect-EXOnline
 
$externalTransportRuleName = "Inbox Rules To External Block"
$rejectMessageText = "To improve security, auto-forwarding rules to external addresses has been disabled. Please contact your Administrator for further information."
 
$externalForwardRule = Get-TransportRule | Where-Object {$_.Identity -contains $externalTransportRuleName}
 
if (!$externalForwardRule) {
    Write-Output "Client Rules To External Block not found, creating Rule"
    New-TransportRule -name "Client Rules To External Block" -Priority 1 -SentToScope NotInOrganization -FromScope InOrganization -MessageTypeMatches AutoForward -RejectMessageEnhancedStatusCode 5.7.1 -RejectMessageReasonText $rejectMessageText
}
