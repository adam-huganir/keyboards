## For building
Symlink `./addy64` to `${ZMK_REPO}/app/boards/shields/addy64``

```powershell
# if your zmk repo is in same parent dir as this repo
$ZMK_REPO = "../zmk"
New-Item -Force -Type SymbolicLink -Target ./addy64 $ZMK_REPO/app/boards/shields/addy64
```
