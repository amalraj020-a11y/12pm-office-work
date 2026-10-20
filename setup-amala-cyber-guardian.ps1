$ErrorActionPreference = 'Stop'
$promptPath = Join-Path $PSScriptRoot 'AMALA_CYBER_GUARDIAN_PROMPT.md'
$prompt = (Get-Content -LiteralPath $promptPath -Raw).Replace('"','\\"').Replace("`r`n",' ').Replace("`n",' ')
openclaw cron add `
  --name 'Amala Cyber Guardian - Daily Security Research' `
  --cron '0 12 * * *' `
  --tz 'Asia/Kolkata' `
  --session isolated `
  --agent amala `
  --message $prompt `
  --model 'ollama/qwen3:4b' `
  --fallbacks '' `
  --timeout-seconds 3600 `
  --no-deliver