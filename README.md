## For building
Symlink `./addy64` to `${ZMK_REPO}/app/boards/shields/addy64``

### Win:
```powershell
# if your zmk repo is at the below path
$ZMK_REPO = "C:/Users/adam/code/zmk"
New-Item -Force -Type SymbolicLink -Target $PWD/addy64 $ZMK_REPO/app/boards/shields/addy64
```

