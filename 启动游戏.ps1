# NES 红白机游戏站 - PowerShell 启动脚本

Write-Host "`n🎮 NES 红白机游戏站`n" -ForegroundColor Cyan

# 启动服务器
Write-Host "正在启动服务器..." -ForegroundColor Yellow
$serverJob = Start-Job -ScriptBlock {
    Set-Location $args[0]
    python -m http.server 8000
} -ArgumentList (Split-Path -Parent $MyInvocation.MyCommand.Path)

# 等待服务器启动
Start-Sleep -Seconds 1

# 打开浏览器
Write-Host "✅ 服务器已启动！" -ForegroundColor Green
Write-Host "📍 访问地址: http://localhost:8000`n" -ForegroundColor Yellow
Start-Process "http://localhost:8000"

Write-Host "按 Ctrl+C 停止服务器`n" -ForegroundColor Gray

# 保持运行
try {
    Wait-Job $serverJob
} finally {
    Stop-Job $serverJob
    Remove-Job $serverJob
}
