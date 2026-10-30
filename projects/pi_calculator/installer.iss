; Inno Setup installer for Pi Calculator
#define AppName "Pi Calculator"
#define AppVersion "0.2.0"
#define AppPublisher "pytoolbox"
#define AppExeName "PiCalculator.exe"

[Setup]
AppId={{B8F7A2E1-4B91-4A0D-9E5A-2B3C7D6F8120}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#AppPublisher}
DefaultDirName={autopf}\Pi Calculator
DefaultGroupName={#AppName}
OutputDir=installer
OutputBaseFilename=PiCalculator-Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64
UninstallDisplayIcon={app}\{#AppExeName}

[Files]
Source: "..\..\dist\{#AppExeName}"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#AppName}"; Filename: "{app}\{#AppExeName}"
Name: "{autodesktop}\{#AppName}"; Filename: "{app}\{#AppExeName}"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional shortcuts:"

[Run]
Filename: "{app}\{#AppExeName}"; Description: "Launch {#AppName}"; Flags: postinstall nowait skipifsilent
