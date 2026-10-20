import json, platform, shutil, subprocess, sys
from pathlib import Path
DAY_ROOT=Path(__file__).resolve().parents[1]
ROOT=Path(__file__).resolve().parents[2]
def check(cmd,args):
    path=shutil.which(cmd); result={"command":cmd,"available":bool(path),"path":path}
    if path:
        try:
            p=subprocess.run([path,*args],capture_output=True,text=True,timeout=15); result.update(exit_code=p.returncode,output=(p.stdout or p.stderr).strip()[:500])
        except Exception as e: result["error"]=f"{type(e).__name__}: {e}"
    return result
def main():
    data={"python":{"version":sys.version.split()[0],"executable":sys.executable},"platform":platform.platform(),"git":check("git",["--version"]),"ollama":check("ollama",["list"]),"curl":check("curl",["--version"]),"portfolio_root":str(ROOT),"safe_lab_directories":(ROOT/"Day-01-Lab-Setup").is_dir() and (ROOT/"Day-02-Python-Security-Toolkit").is_dir(),"network_testing":"NOT RUN: Day 1 performs no network requests or scans"}
    print(json.dumps(data,indent=2)); (DAY_ROOT/"evidence"/"environment-check.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__": main()