#Invoke-Expression $(New-Object IOStreamReader ($(New-Object IOCompressionDeflateStream ($(New-Object IOMemoryStream (,$([Convert]::FromBase64String('<***BASE64__DATA***>')))), [IOCompressionCompressionMode]::Decompress)), [TextEncoding]::ASCII))ReadToEnd();

$base64data = "insert compressed and base64 data here"
$data = [System.Convert]::FromBase64String($base64data)
$ms = New-Object System.IO.MemoryStream
$ms.Write($data, 0, $data.Length)
$ms.Seek(0,0) | Out-Null

$sr = New-Object System.IO.StreamReader(New-Object System.IO.Compression.DeflateStream($ms, [System.IO.Compression.CompressionMode]::Decompress))

while ($line = $sr.ReadLine()) {  
    $line
}
