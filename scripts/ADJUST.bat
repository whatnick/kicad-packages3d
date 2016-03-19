cd %~p0
for %%x in (%*) do (
freecad.exe %%x rotate.FCMacro x x tmp
REM freecad.exe %%x align.FCMacro z-
REM freecad.exe %%x step2wrl.FCMacro
)