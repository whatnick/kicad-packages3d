cd %~p0
for %%x in (%*) do (
freecad.exe %%x rotate.FCMacro x z z
freecad.exe %%x step2wrl.FCMacro
)