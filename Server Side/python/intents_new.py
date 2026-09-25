intents = {

    # ============================================================
    # FILESYSTEM / NAVIGATION
    # ============================================================

    "linux.pwd": [
        "show current directory",
        "where am I",
        "kaha hu",
        "what directory am I in",
        "show working directory",
        "current path dikhao",
        "abhi kis directory me hoon",
        "current folder batao",
        "pwd dikhao",
        "present working directory dikhao",
        "main kaha hoon",
        # --- NEW HINGLISH COMMANDS ---
        "mera current path kya hai",
        "abhi exact kis path par hu",
    ],

    "linux.ls": [
        "list files",
        "show files",
        "list directory",
        "show directory contents",
        "files dikhao",
        "folder ke files dikhao",
        "directory ke andar kya hai",
        "is folder me kya hai",
        "saare files dikhao",
        "current directory list karo",
        "ls karo",
        "folder dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "folder me kya kya pada hai",
        "andar ka maal dikhao",
    ],

    "linux.ls.hidden": [
        "show hidden files",
        "list hidden files",
        "show all files including hidden",
        "hidden files dikhao",
        "chhupe hue files dikhao",
        "hidden files bhi dikhao",
        "all files show karo",
        "ls including hidden files",
        "hidden files list karo",
        # --- NEW HINGLISH COMMANDS ---
        "dot files dikha do",
        "hidden files check karo",
    ],

    "linux.cd": [
        "change directory",
        "go to another folder",
        "open a directory",
        "change folder",
        "directory change karo",
        "folder me jao",
        "is folder me jao",
        "home directory me jao",
        "parent directory me jao",
        "cd karo",
        # --- NEW HINGLISH COMMANDS ---
        "is wale folder ke andar jao",
        "path change kardo",
    ],

    "linux.cd.parent": [
        "go to parent directory",
        "go one directory back",
        "move to parent folder",
        "parent folder me jao",
        "ek folder peeche jao",
        "upar wali directory me jao",
        "previous directory me jao",
        "cd parent",
        # --- NEW HINGLISH COMMANDS ---
        "ek level upar jao",
        "back aao",
    ],

    "linux.cd.home": [
        "go home",
        "go to home directory",
        "home folder me jao",
        "home directory par jao",
        "ghar wale folder me jao",
        "home par jao",
        # --- NEW HINGLISH COMMANDS ---
        "main home me chalo",
        "wapas home jao",
    ],

    "linux.mkdir": [
        "create a directory",
        "create a folder",
        "make a directory",
        "new folder banao",
        "directory banao",
        "folder create karo",
        "naya folder bana do",
        "directory bana do",
        "mkdir karo",
        "ek folder banana hai",
        # --- NEW HINGLISH COMMANDS ---
        "ek naya folder banado",
        "folder bana de",
    ],

    "linux.mkdir.parents": [
        "create nested directories",
        "create parent directories",
        "create directory with parents",
        "nested folder banao",
        "andar ke folders bhi create karo",
        "parent folders ke saath directory banao",
        "multiple directories create karo",
        # --- NEW HINGLISH COMMANDS ---
        "ek ke andar ek folder banao",
        "tree structure me folder banao",
    ],

    "linux.touch": [
        "create a file",
        "make a new file",
        "create an empty file",
        "new file banao",
        "file create karo",
        "nayi file bana do",
        "empty file bana do",
        "touch file karo",
        "ek file banana hai",
        # --- NEW HINGLISH COMMANDS ---
        "khali file bana de",
        "ek blank file create kardo",
    ],

    "linux.cp": [
        "copy a file",
        "copy a folder",
        "copy this file",
        "file copy karo",
        "file ko dusre folder me copy karo",
        "folder copy kar do",
        "file ki copy bana do",
        "copy kar do",
        "cp karo",
        # --- NEW HINGLISH COMMANDS ---
        "file ka duplicate bana do",
        "is file ko waha paste kardo",
    ],

    "linux.mv": [
        "move a file",
        "move a folder",
        "move this file",
        "file move karo",
        "file ko dusre folder me move karo",
        "folder move kar do",
        "file ko shift karo",
        "move kar do",
        "mv karo",
        # --- NEW HINGLISH COMMANDS ---
        "file ko waha daal do",
        "folder shift kardo",
    ],

    "linux.rename": [
        "rename a file",
        "rename a folder",
        "change file name",
        "change folder name",
        "file ka naam badal do",
        "file rename karo",
        "folder ka naam change karo",
        "naam change kar do",
        "rename kar do",
        # --- NEW HINGLISH COMMANDS ---
        "naam badal de bhai",
        "is file ka new name set karo",
    ],

    "linux.rm": [
        "delete a file",
        "remove a file",
        "delete this file",
        "file hata do",
        "file delete karo",
        "file remove kar do",
        "is file ko hata do",
        "rm karo",
        "file mita do",
        # --- NEW HINGLISH COMMANDS ---
        "file uda do",
        "ye file delete maar do",
    ],

    "linux.rm.directory": [
        "delete a directory",
        "remove a folder",
        "delete this folder",
        "folder hata do",
        "directory delete karo",
        "folder remove kar do",
        "directory mita do",
        "is folder ko delete karo",
        # --- NEW HINGLISH COMMANDS ---
        "ye folder uda do",
        "folder delete maar do",
    ],

    "linux.rm.recursive": [
        "delete folder recursively",
        "remove directory recursively",
        "delete folder and everything inside",
        "folder ke andar sab kuch delete karo",
        "poora folder delete kar do",
        "directory aur uske files hata do",
        "folder recursively remove karo",
        # --- NEW HINGLISH COMMANDS ---
        "sab kuch uda do andar ka",
        "force delete kardo pura folder",
    ],

    "linux.find": [
        "find a file",
        "search for a file",
        "find this file",
        "locate a file",
        "file dhundo",
        "file search karo",
        "is file ko dhundo",
        "folder me file search karo",
        "find command use karo",
        # --- NEW HINGLISH COMMANDS ---
        "kaha rakhi hai ye file",
        "file find karke do",
    ],

    "linux.locate": [
        "locate a file",
        "search file by name",
        "locate this file",
        "file ka location batao",
        "file kaha hai",
        "file ka path dhundo",
        "locate command chalao",
        # --- NEW HINGLISH COMMANDS ---
        "file ki exact location dhundo",
    ],

    "linux.file.type": [
        "show file type",
        "what type of file is this",
        "check file type",
        "file ka type batao",
        "ye file kis type ki hai",
        "file type check karo",
        # --- NEW HINGLISH COMMANDS ---
        "kis tarah ki file hai ye",
        "extension kya hai iska",
    ],

    "linux.stat": [
        "show file information",
        "show file metadata",
        "check file details",
        "file ki details dikhao",
        "file metadata batao",
        "file information dikhao",
        "stat file karo",
        # --- NEW HINGLISH COMMANDS ---
        "file ki puri kundli nikaalo",
        "file ki properties batao",
    ],

    # ============================================================
    # FILE CONTENT
    # ============================================================

    "linux.cat": [
        "show file contents",
        "read this file",
        "display file contents",
        "file ka content dikhao",
        "file padho",
        "file ke andar kya hai",
        "file content show karo",
        "cat file karo",
        # --- NEW HINGLISH COMMANDS ---
        "file me likha kya hai",
        "text dikhao file ka",
    ],

    "linux.less": [
        "open file for reading",
        "view a large file",
        "read file page by page",
        "large file dikhao",
        "file ko page wise dikhao",
        "file read karni hai",
        "less command use karo",
        # --- NEW HINGLISH COMMANDS ---
        "badi file hai scroll karke dikhao",
    ],

    "linux.head": [
        "show first lines of file",
        "show beginning of file",
        "first ten lines dikhao",
        "file ki starting dikhao",
        "file ki first lines batao",
        "head command karo",
        # --- NEW HINGLISH COMMANDS ---
        "shuru ki lines dikha do",
        "upar ka text padhna hai",
    ],

    "linux.tail": [
        "show last lines of file",
        "show end of file",
        "last ten lines dikhao",
        "file ka end dikhao",
        "last lines batao",
        "tail command karo",
        # --- NEW HINGLISH COMMANDS ---
        "aakhiri ki lines batao",
        "neeche kya likha hai dikhao",
    ],

    "linux.tail.follow": [
        "watch file live",
        "follow log file",
        "monitor log file",
        "show live logs",
        "live logs dikhao",
        "logs ko continuously dekho",
        "file ko live monitor karo",
        "tail follow karo",
        # --- NEW HINGLISH COMMANDS ---
        "logs chalne do",
        "realtime logs dikhate raho",
    ],

    "linux.grep": [
        "search text in a file",
        "find text in files",
        "search for a word",
        "file me text dhundo",
        "word search karo",
        "files ke andar search karo",
        "specific text find karo",
        "grep karo",
        # --- NEW HINGLISH COMMANDS ---
        "is line ko dhundo",
        "ye word kahan likha hai",
    ],

    "linux.grep.recursive": [
        "search text recursively",
        "search all files for this text",
        "search inside all folders",
        "poore folder me text dhundo",
        "sab files me word search karo",
        "recursive grep karo",
        "directory ke andar har file me search karo",
        # --- NEW HINGLISH COMMANDS ---
        "har jagah ye word dhundo",
        "pure project me find karo",
    ],

    "linux.wc": [
        "count lines in a file",
        "count words in a file",
        "count characters in a file",
        "file ki lines count karo",
        "file me kitne words hain",
        "file ka size count karo",
        "wc command karo",
        # --- NEW HINGLISH COMMANDS ---
        "kitni lines hain batao",
        "total words gin ke batao",
    ],

    "linux.sort": [
        "sort file contents",
        "sort these lines",
        "sort the file",
        "file sort karo",
        "lines ko sort karo",
        "alphabetically sort karo",
        "sort command use karo",
        # --- NEW HINGLISH COMMANDS ---
        "sequence me laga do",
        "data order me karo",
    ],

    "linux.uniq": [
        "remove duplicate lines",
        "show unique lines",
        "remove duplicate entries",
        "duplicate lines hata do",
        "unique lines dikhao",
        "duplicates remove karo",
        "uniq command karo",
        # --- NEW HINGLISH COMMANDS ---
        "repeated lines uda do",
        "sirf ek bar dikhao",
    ],

    "linux.cut": [
        "extract columns from file",
        "extract fields from text",
        "cut specific columns",
        "file se column nikalo",
        "specific field extract karo",
        "text ka column nikalo",
        # --- NEW HINGLISH COMMANDS ---
        "bich ka data kaat ke nikaalo",
    ],

    "linux.awk": [
        "process text with awk",
        "extract data using awk",
        "filter columns using awk",
        "awk se data nikalo",
        "awk command chalao",
        "text ko awk se process karo",
        # --- NEW HINGLISH COMMANDS ---
        "pattern match karke data laao",
    ],

    "linux.sed": [
        "replace text in file",
        "edit text using sed",
        "replace a string",
        "text replace karo",
        "file me string replace karo",
        "sed se text change karo",
        "sed command chalao",
        # --- NEW HINGLISH COMMANDS ---
        "find and replace maar do",
        "word ko dusre word se badal do",
    ],

    # ============================================================
    # FILE PERMISSIONS
    # ============================================================

    "linux.chmod": [
        "change file permissions",
        "modify file permissions",
        "change permissions",
        "file permission change karo",
        "permissions set karo",
        "file ko executable banao",
        "chmod karo",
        "file permissions modify karo",
        # --- NEW HINGLISH COMMANDS ---
        "access rights badal do",
        "file ke rights change kardo",
    ],

    "linux.chmod.readwrite": [
        "give read write permission",
        "set read write permissions",
        "read write permission do",
        "file ko read write permission do",
        "permission rw set karo",
        # --- NEW HINGLISH COMMANDS ---
        "edit karne ki power de do",
        "padhne aur likhne ka access do",
    ],

    "linux.chmod.execute": [
        "make file executable",
        "give execute permission",
        "make this script executable",
        "file executable banao",
        "script ko executable banao",
        "execute permission do",
        "chmod executable karo",
        # --- NEW HINGLISH COMMANDS ---
        "run karne ki permission de do",
        "script chalne laayak bana do",
    ],

    "linux.chown": [
        "change file owner",
        "change ownership",
        "change owner of file",
        "file ka owner change karo",
        "ownership change karo",
        "file kisi user ko assign karo",
        "chown karo",
        # --- NEW HINGLISH COMMANDS ---
        "is file ka maalik badal do",
        "user ki ownership de do",
    ],

    "linux.chgrp": [
        "change file group",
        "change group ownership",
        "file ka group change karo",
        "group ownership change karo",
        "chgrp karo",
        # --- NEW HINGLISH COMMANDS ---
        "is file ko dusre group me daal do",
    ],

    "linux.umask": [
        "show umask",
        "change umask",
        "check default permissions",
        "umask dikhao",
        "umask check karo",
        "default file permissions check karo",
    ],

    # ============================================================
    # DISK / STORAGE
    # ============================================================

    "linux.df": [
        "show disk space",
        "check disk space",
        "how much disk space is available",
        "disk space dikhao",
        "kitni disk space bachi hai",
        "disk usage check karo",
        "df karo",
        # --- NEW HINGLISH COMMANDS ---
        "space kitna khali hai batao",
        "hard disk ki jagah check karo",
    ],

    "linux.df.human": [
        "show disk usage in human readable format",
        "human readable disk space",
        "disk space readable format me dikhao",
        "disk usage easy format me dikhao",
        "df human readable karo",
        # --- NEW HINGLISH COMMANDS ---
        "MB GB me space batao",
        "samajh aane wale format me space dikhao",
    ],

    "linux.du": [
        "show directory size",
        "check folder size",
        "find what is using disk space",
        "folder kitna space le raha hai",
        "directory ka size batao",
        "disk usage by folder dikhao",
        "du karo",
        # --- NEW HINGLISH COMMANDS ---
        "ye folder kitna bada hai",
        "size calculate karo iska",
    ],

    "linux.du.large": [
        "find largest files",
        "find largest folders",
        "which files are taking most space",
        "sabse bade files dhundo",
        "kaunsa folder sabse zyada space le raha hai",
        "largest files batao",
        "disk me kya zyada space le raha hai",
        # --- NEW HINGLISH COMMANDS ---
        "sabse bhari files kaunsi hain",
        "memory kaun khaa raha hai",
    ],

    "linux.lsblk": [
        "show disks",
        "list block devices",
        "show attached disks",
        "disk devices dikhao",
        "attached disks batao",
        "block devices list karo",
        "lsblk karo",
        # --- NEW HINGLISH COMMANDS ---
        "hard drives ki list dikhao",
        "partitions dikha do",
    ],

    "linux.mount": [
        "mount a disk",
        "mount a filesystem",
        "mount this drive",
        "disk mount karo",
        "drive mount kar do",
        "filesystem mount karo",
        "mount command chalao",
        # --- NEW HINGLISH COMMANDS ---
        "usb drive connect kardo",
    ],

    "linux.umount": [
        "unmount a disk",
        "unmount filesystem",
        "remove mounted drive",
        "disk unmount karo",
        "drive unmount kar do",
        "filesystem unmount karo",
        # --- NEW HINGLISH COMMANDS ---
        "drive ko safely nikal do",
        "eject maar do",
    ],

    "linux.fdisk": [
        "show disk partitions",
        "manage disk partitions",
        "partition disk",
        "disk partition dikhao",
        "partitions check karo",
        "disk partition manage karo",
        # --- NEW HINGLISH COMMANDS ---
        "hard disk ko divide karo",
    ],

    "linux.free": [
        "show memory usage",
        "check RAM usage",
        "how much memory is free",
        "RAM kitni free hai",
        "memory usage dikhao",
        "free memory batao",
        "free command karo",
        # --- NEW HINGLISH COMMANDS ---
        "kitni RAM bachi hai",
        "memory ka haal batao",
    ],

    "linux.free.swap": [
        "show swap usage",
        "check swap memory",
        "swap kitni use ho rahi hai",
        "swap usage dikhao",
        "swap memory check karo",
        # --- NEW HINGLISH COMMANDS ---
        "virtual memory kitni bachi hai",
    ],

    # ============================================================
    # PROCESSES
    # ============================================================

    "linux.ps": [
        "show running processes",
        "list processes",
        "show running programs",
        "running processes dikhao",
        "kaunse processes chal rahe hain",
        "process list dikhao",
        "ps command karo",
        # --- NEW HINGLISH COMMANDS ---
        "background me kya chal raha hai",
        "tasks ki list do",
    ],

    "linux.ps.all": [
        "show all processes",
        "list all processes",
        "show processes from all users",
        "saare processes dikhao",
        "all processes list karo",
        "sab users ke processes dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "system ka har ek process dikha do",
    ],

    "linux.top": [
        "show system processes",
        "monitor processes",
        "show CPU usage live",
        "show running processes live",
        "live process monitor dikhao",
        "CPU usage live batao",
        "top command karo",
        # --- NEW HINGLISH COMMANDS ---
        "kaunsa task cpu khaa raha hai",
        "live stats dikha do",
    ],

    "linux.htop": [
        "open htop",
        "show htop",
        "monitor processes with htop",
        "htop chalao",
        "interactive process monitor kholo",
        "processes ko htop me dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "htop on kardo",
        "color wala task manager dikhao",
    ],

    "linux.kill": [
        "kill a process",
        "stop a process",
        "terminate a process",
        "process ko kill karo",
        "process band karo",
        "process terminate karo",
        "PID ko kill karo",
        "kill command chalao",
        # --- NEW HINGLISH COMMANDS ---
        "is task ko band maar do",
        "process khatam kar do",
    ],

    "linux.kill.force": [
        "force kill a process",
        "force stop process",
        "kill process forcefully",
        "process ko force kill karo",
        "process ko zabardasti band karo",
        "SIGKILL bhejo",
        "forcefully process terminate karo",
        # --- NEW HINGLISH COMMANDS ---
        "zabardasti kill maar do",
        "process ko uda do instantly",
    ],

    "linux.pgrep": [
        "find process by name",
        "find PID by process name",
        "get process id",
        "process ka PID batao",
        "name se process dhundo",
        "process ID find karo",
        "pgrep karo",
        # --- NEW HINGLISH COMMANDS ---
        "is naam ka process id nikaalo",
    ],

    "linux.pkill": [
        "kill process by name",
        "stop processes by name",
        "process name se kill karo",
        "naam se process band karo",
        "all matching processes kill karo",
        "pkill command karo",
        # --- NEW HINGLISH COMMANDS ---
        "is naam wale sab process uda do",
    ],

    "linux.jobs": [
        "show background jobs",
        "list shell jobs",
        "show running background jobs",
        "background jobs dikhao",
        "shell jobs batao",
        "jobs list karo",
        # --- NEW HINGLISH COMMANDS ---
        "piche kya chal raha hai batao",
    ],

    "linux.bg": [
        "send process to background",
        "move job to background",
        "run job in background",
        "process ko background me bhejo",
        "job background me chalao",
        "background me daal do",
        # --- NEW HINGLISH COMMANDS ---
        "is task ko background me daal de",
    ],

    "linux.fg": [
        "bring process to foreground",
        "bring job to foreground",
        "run background job in foreground",
        "process foreground me lao",
        "job foreground me lao",
        "foreground me bhejo",
        # --- NEW HINGLISH COMMANDS ---
        "task ko samne le aao",
    ],

    # ============================================================
    # SYSTEM INFORMATION
    # ============================================================

    "linux.uname": [
        "show system information",
        "show kernel information",
        "check Linux version",
        "system information dikhao",
        "kernel version batao",
        "Linux version check karo",
        "uname dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "kaunsa OS chal raha hai",
        "system details batao",
    ],

    "linux.hostname": [
        "show hostname",
        "what is my hostname",
        "check computer name",
        "hostname batao",
        "system ka naam kya hai",
        "machine name dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "mera pc ka naam kya hai",
    ],

    "linux.uptime": [
        "show system uptime",
        "how long has system been running",
        "system kitne time se running hai",
        "uptime batao",
        "server kitne time se up hai",
        "uptime check karo",
        # --- NEW HINGLISH COMMANDS ---
        "kab se chal raha hai system",
    ],

    "linux.date": [
        "show date",
        "show current date",
        "what is today's date",
        "current date batao",
        "aaj ki date kya hai",
        "date dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "aaj kya taarikh hai",
    ],

    "linux.time": [
        "show current time",
        "what time is it",
        "current time batao",
        "abhi kitne baje hain",
        "system time dikhao",
        "time batao",
        # --- NEW HINGLISH COMMANDS ---
        "kya time ho raha hai",
    ],

    "linux.whoami": [
        "show current user",
        "who am I",
        "which user am I",
        "current username batao",
        "main kis user se logged in hoon",
        "whoami karo",
        # --- NEW HINGLISH COMMANDS ---
        "mera username kya hai",
    ],

    "linux.who": [
        "show logged in users",
        "who is logged in",
        "list logged in users",
        "logged in users dikhao",
        "kaun kaun login hai",
        "current users batao",
        # --- NEW HINGLISH COMMANDS ---
        "system me aur kon login hai",
    ],

    "linux.id": [
        "show user id",
        "show group id",
        "show my user information",
        "user ID batao",
        "UID aur GID dikhao",
        "user identity check karo",
        # --- NEW HINGLISH COMMANDS ---
        "meri ids dikha do",
    ],

    "linux.lscpu": [
        "show CPU information",
        "show processor details",
        "check CPU details",
        "processor information dikhao",
        "CPU details batao",
        "CPU architecture check karo",
        # --- NEW HINGLISH COMMANDS ---
        "mera processor kaunsa hai",
        "cpu ke cores batao",
    ],

    "linux.lsmem": [
        "show memory information",
        "show RAM details",
        "check memory information",
        "RAM details dikhao",
        "memory details batao",
        # --- NEW HINGLISH COMMANDS ---
        "kitni ram lagi hai dikhao",
    ],

    # ============================================================
    # PACKAGE MANAGEMENT - APT
    # ============================================================

    "ubuntu.apt.update": [
        "update package list",
        "update apt",
        "refresh package list",
        "apt update karo",
        "package list update karo",
        "packages ki list refresh karo",
        "repository information update karo",
        # --- NEW HINGLISH COMMANDS ---
        "repo update maar do",
        "apt ko refresh kardo",
    ],

    "ubuntu.apt.upgrade": [
        "upgrade packages",
        "update installed packages",
        "upgrade all packages",
        "apt upgrade karo",
        "saare packages upgrade karo",
        "installed packages update karo",
        "system packages upgrade karo",
        # --- NEW HINGLISH COMMANDS ---
        "sab kuch naya update kardo",
        "system upgrade maar do",
    ],

    "ubuntu.apt.install": [
        "install a package",
        "install software",
        "install this package",
        "package install karo",
        "software install kar do",
        "naya package install karo",
        "apt se install karo",
        # --- NEW HINGLISH COMMANDS ---
        "apt se daal do",
        "ye tool install maar do",
    ],

    "ubuntu.apt.remove": [
        "remove a package",
        "uninstall software",
        "uninstall this package",
        "package uninstall karo",
        "software hata do",
        "package remove kar do",
        "apt package uninstall karo",
        # --- NEW HINGLISH COMMANDS ---
        "is software ko uda do",
        "uninstall maar do",
    ],

    "ubuntu.apt.purge": [
        "purge a package",
        "remove package and configuration",
        "completely uninstall package",
        "package ko completely remove karo",
        "package aur config hata do",
        "purge package karo",
        # --- NEW HINGLISH COMMANDS ---
        "jad se mita do is package ko",
        "config ke sath uda do",
    ],

    "ubuntu.apt.search": [
        "search for a package",
        "find an apt package",
        "search software package",
        "package dhundo",
        "apt package search karo",
        "software package find karo",
        "available package check karo",
        # --- NEW HINGLISH COMMANDS ---
        "repo me dhundo ye tool",
    ],

    "ubuntu.apt.show": [
        "show package information",
        "show apt package details",
        "check package details",
        "package ki details batao",
        "package information dikhao",
        "apt package details check karo",
        # --- NEW HINGLISH COMMANDS ---
        "is software ki info dikhao",
    ],

    "ubuntu.apt.list.installed": [
        "list installed packages",
        "show installed packages",
        "which packages are installed",
        "installed packages dikhao",
        "kaunse packages installed hain",
        "saare installed packages batao",
        # --- NEW HINGLISH COMMANDS ---
        "kya kya install hai system me",
    ],

    "ubuntu.apt.autoremove": [
        "remove unused packages",
        "remove unnecessary packages",
        "clean unused dependencies",
        "unused packages hata do",
        "unnecessary dependencies remove karo",
        "apt autoremove karo",
        # --- NEW HINGLISH COMMANDS ---
        "faltu packages uda do",
        "kachra saaf kardo",
    ],

    "ubuntu.apt.autoclean": [
        "clean apt cache",
        "remove old package files",
        "clean package cache",
        "apt cache clean karo",
        "old package files hata do",
        "package cache clean kar do",
        # --- NEW HINGLISH COMMANDS ---
        "cache uda do",
    ],

    "ubuntu.snap.install": [
        "install a snap package",
        "install software using snap",
        "snap package install karo",
        "snap se software install karo",
        "snap install kar do",
        # --- NEW HINGLISH COMMANDS ---
        "snap se daal do",
    ],

    "ubuntu.snap.remove": [
        "remove a snap package",
        "uninstall snap package",
        "snap package hata do",
        "snap uninstall karo",
        "snap remove kar do",
        # --- NEW HINGLISH COMMANDS ---
        "snap wala tool uda do",
    ],

    "ubuntu.snap.list": [
        "list snap packages",
        "show installed snaps",
        "snap packages dikhao",
        "installed snaps batao",
        "snap list karo",
        # --- NEW HINGLISH COMMANDS ---
        "snap me kya install hai",
    ],

    # ============================================================
    # SERVICES / SYSTEMD
    # ============================================================

    "linux.systemctl.status": [
        "check service status",
        "show service status",
        "is the service running",
        "service status dikhao",
        "service chal rahi hai kya",
        "service check karo",
        "systemctl status dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "service ka haal batao",
        "service up hai ya down",
    ],

    "linux.systemctl.start": [
        "start a service",
        "start the service",
        "service start karo",
        "service chalu karo",
        "service ko start kar do",
        "systemctl start karo",
        # --- NEW HINGLISH COMMANDS ---
        "service on kar do",
        "ye background service chalao",
    ],

    "linux.systemctl.stop": [
        "stop a service",
        "stop the service",
        "service stop karo",
        "service band karo",
        "service ko stop kar do",
        "systemctl stop karo",
        # --- NEW HINGLISH COMMANDS ---
        "service off kardo",
        "service rok do",
    ],

    "linux.systemctl.restart": [
        "restart a service",
        "restart the service",
        "service restart karo",
        "service ko restart kar do",
        "service dobara start karo",
        "systemctl restart karo",
        # --- NEW HINGLISH COMMANDS ---
        "service ek baar reset maar do",
        "phir se chalu karo service",
    ],

    "linux.systemctl.reload": [
        "reload a service",
        "reload service configuration",
        "service reload karo",
        "configuration reload karo",
        "service config reload kar do",
        # --- NEW HINGLISH COMMANDS ---
        "changes apply kardo service me",
    ],

    "linux.systemctl.enable": [
        "enable service at boot",
        "start service automatically on boot",
        "enable a service",
        "service ko boot par start karo",
        "service enable karo",
        "startup par service chalao",
        # --- NEW HINGLISH COMMANDS ---
        "boot pe auto start kardo",
    ],

    "linux.systemctl.disable": [
        "disable service at boot",
        "prevent service from starting on boot",
        "disable a service",
        "service boot par start na ho",
        "service disable karo",
        "startup service band karo",
        # --- NEW HINGLISH COMMANDS ---
        "auto start band kardo",
    ],

    "linux.systemctl.list": [
        "list services",
        "show system services",
        "show running services",
        "services dikhao",
        "running services batao",
        "system services list karo",
        # --- NEW HINGLISH COMMANDS ---
        "sari services ki list do",
    ],

    "linux.journalctl": [
        "show system logs",
        "show service logs",
        "view journal logs",
        "system logs dikhao",
        "service ke logs dikhao",
        "journal logs check karo",
        "journalctl karo",
        # --- NEW HINGLISH COMMANDS ---
        "systemctl ke logs batao",
    ],

    "linux.journalctl.follow": [
        "watch system logs live",
        "follow service logs",
        "show live service logs",
        "logs live dikhao",
        "service logs continuously dekho",
        "journal logs follow karo",
        # --- NEW HINGLISH COMMANDS ---
        "live logs on kardo system ke",
    ],

    # ============================================================
    # NETWORKING
    # ============================================================

    "linux.ip.address": [
        "show IP address",
        "show my IP",
        "check IP address",
        "what is my IP",
        "IP address batao",
        "mera IP kya hai",
        "network IP dikhao",
        "ip address check karo",
        # --- NEW HINGLISH COMMANDS ---
        "machine ka ip kya hai",
    ],

    "linux.ip.interface": [
        "show network interfaces",
        "list network interfaces",
        "show network devices",
        "network interfaces dikhao",
        "network devices batao",
        "kaunse network interfaces hain",
        "ip link dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "network cards dikha do",
    ],

    "linux.ip.route": [
        "show routing table",
        "show network routes",
        "check routes",
        "routing table dikhao",
        "network routes batao",
        "route table check karo",
        "ip route dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "traffic kahan se ja raha hai",
    ],

    "linux.ip.neighbor": [
        "show ARP table",
        "show network neighbors",
        "show connected neighbors",
        "ARP table dikhao",
        "network neighbors batao",
        "neighbor table dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "arp cache check karo",
    ],

    "linux.ping": [
        "ping a host",
        "check connectivity",
        "check if server is reachable",
        "ping this server",
        "server ko ping karo",
        "network connectivity check karo",
        "connection check karo",
        "ping karo",
        # --- NEW HINGLISH COMMANDS ---
        "dekho server chal raha hai kya",
        "ping maar ke check karo",
    ],

    "linux.traceroute": [
        "trace network route",
        "show path to server",
        "trace route to host",
        "network path dikhao",
        "server tak ka route batao",
        "traceroute karo",
        "packet kis route se ja raha hai",
        # --- NEW HINGLISH COMMANDS ---
        "rasta trace karo packet ka",
    ],

    "linux.dig": [
        "lookup DNS records",
        "check DNS",
        "find DNS information",
        "DNS lookup karo",
        "DNS records dikhao",
        "domain ka DNS check karo",
        "dig command karo",
        # --- NEW HINGLISH COMMANDS ---
        "domain kaha point kar raha hai",
    ],

    "linux.nslookup": [
        "lookup domain DNS",
        "check domain IP",
        "resolve domain name",
        "domain ka IP batao",
        "DNS se domain resolve karo",
        "nslookup karo",
        # --- NEW HINGLISH COMMANDS ---
        "naam ka ip nikaalo",
    ],

    "linux.curl": [
        "make an HTTP request",
        "call this URL",
        "fetch a URL",
        "download from URL using curl",
        "URL ko curl karo",
        "API call karo",
        "HTTP request bhejo",
        "curl request karo",
        # --- NEW HINGLISH COMMANDS ---
        "api hit maar do",
        "url se response lao",
    ],

    "linux.wget": [
        "download a file",
        "download from URL",
        "download this URL",
        "file download karo",
        "URL se file lao",
        "wget se download karo",
        # --- NEW HINGLISH COMMANDS ---
        "link se file utha lo",
    ],

    "linux.ss": [
        "show open network connections",
        "show listening ports",
        "list network sockets",
        "open ports dikhao",
        "listening ports batao",
        "network connections dikhao",
        "ss command karo",
        # --- NEW HINGLISH COMMANDS ---
        "kaunse ports khule hai",
    ],

    "linux.netstat": [
        "show network connections",
        "show listening ports",
        "check network sockets",
        "network connections dikhao",
        "ports check karo",
        "netstat karo",
        # --- NEW HINGLISH COMMANDS ---
        "network ka status batao",
    ],

    "linux.hostname.resolve": [
        "resolve hostname",
        "find IP from hostname",
        "find hostname from IP",
        "hostname resolve karo",
        "hostname ka IP batao",
        "IP se hostname dhundo",
        # --- NEW HINGLISH COMMANDS ---
        "machine ka ip resolve karo",
    ],

    # ============================================================
    # SSH
    # ============================================================

    "linux.ssh.connect": [
        "connect to a server using ssh",
        "ssh into server",
        "login to remote server",
        "server par ssh karo",
        "remote server me login karo",
        "ssh se server connect karo",
        "remote machine par jao",
        # --- NEW HINGLISH COMMANDS ---
        "server me ghus jao ssh se",
    ],

    "linux.ssh.keygen": [
        "generate ssh key",
        "create ssh key",
        "make a new ssh key",
        "ssh key banao",
        "new SSH key generate karo",
        "ssh key create kar do",
        # --- NEW HINGLISH COMMANDS ---
        "meri nayi key nikal do",
    ],

    "linux.ssh.copy_id": [
        "copy ssh key to server",
        "setup passwordless ssh",
        "add my ssh key to server",
        "server par ssh key copy karo",
        "passwordless ssh setup karo",
        "authorized key add karo",
        # --- NEW HINGLISH COMMANDS ---
        "meri key server me daal do",
        "bina password login set karo",
    ],

    "linux.scp.upload": [
        "copy file to remote server",
        "upload file using scp",
        "send file to server",
        "file server par bhejo",
        "remote server par file copy karo",
        "scp se upload karo",
        # --- NEW HINGLISH COMMANDS ---
        "file remote pe daal do",
    ],

    "linux.scp.download": [
        "download file from server",
        "copy file from remote server",
        "get file from server using scp",
        "server se file lao",
        "remote server se file copy karo",
        "scp se download karo",
        # --- NEW HINGLISH COMMANDS ---
        "server se file utha lo",
    ],

    # ============================================================
    # USERS / GROUPS
    # ============================================================

    "linux.user.list": [
        "list users",
        "show users",
        "show system users",
        "users dikhao",
        "saare users batao",
        "system users list karo",
        # --- NEW HINGLISH COMMANDS ---
        "kon kon accounts hai system me",
    ],

    "linux.user.add": [
        "create a user",
        "add a new user",
        "new user banao",
        "user create karo",
        "naya user add karo",
        "ek user banana hai",
        "add user",
        # --- NEW HINGLISH COMMANDS ---
        "account bana de ek aur",
    ],

    "linux.user.delete": [
        "delete a user",
        "remove a user",
        "user delete karo",
        "user hata do",
        "user remove kar do",
        "system user delete karo",
        # --- NEW HINGLISH COMMANDS ---
        "user ka account uda do",
    ],

    "linux.user.modify": [
        "modify a user",
        "change user settings",
        "modify user account",
        "user settings change karo",
        "user account modify karo",
        "usermod karo",
        # --- NEW HINGLISH COMMANDS ---
        "user ki details update kardo",
    ],

    "linux.user.password": [
        "change user password",
        "set password",
        "change my password",
        "password change karo",
        "user ka password set karo",
        "password update karo",
        # --- NEW HINGLISH COMMANDS ---
        "mera pass badal do",
    ],

    "linux.group.list": [
        "list groups",
        "show groups",
        "system groups dikhao",
        "groups batao",
        "saare groups list karo",
        # --- NEW HINGLISH COMMANDS ---
        "user groups ki list do",
    ],

    "linux.group.add": [
        "create a group",
        "add a new group",
        "new group banao",
        "group create karo",
        "naya group add karo",
        # --- NEW HINGLISH COMMANDS ---
        "ek group banado",
    ],

    "linux.group.delete": [
        "delete a group",
        "remove a group",
        "group delete karo",
        "group hata do",
        "group remove kar do",
        # --- NEW HINGLISH COMMANDS ---
        "group ko uda do",
    ],

    "linux.group.add_user": [
        "add user to group",
        "add user to a group",
        "put user in group",
        "user ko group me add karo",
        "group me user daalo",
        "user ko group membership do",
        # --- NEW HINGLISH COMMANDS ---
        "is user ko is group me ghusa do",
    ],

    # ============================================================
    # ARCHIVES / COMPRESSION
    # ============================================================

    "linux.tar.create": [
        "create a tar archive",
        "make a tar file",
        "archive these files",
        "tar archive banao",
        "files ko tar karo",
        "tar file create karo",
        "archive bana do",
        # --- NEW HINGLISH COMMANDS ---
        "sab ko milakar ek tar bana do",
    ],

    "linux.tar.extract": [
        "extract a tar archive",
        "untar a file",
        "extract tar file",
        "tar file extract karo",
        "archive kholo",
        "tar ko extract karo",
        "untar kar do",
        # --- NEW HINGLISH COMMANDS ---
        "tar ko uncompress karo",
    ],

    "linux.tar.list": [
        "list contents of tar",
        "show files inside tar",
        "tar ke andar kya hai",
        "archive contents dikhao",
        "tar files list karo",
        # --- NEW HINGLISH COMMANDS ---
        "bina extract kiye tar dikhao",
    ],

    "linux.gzip": [
        "compress a file with gzip",
        "gzip a file",
        "compress using gzip",
        "file gzip karo",
        "gzip se compress karo",
        "gzip file banao",
        # --- NEW HINGLISH COMMANDS ---
        "file ko compress maar do",
    ],

    "linux.gunzip": [
        "decompress gzip file",
        "ungzip a file",
        "extract gzip file",
        "gzip file decompress karo",
        "gunzip karo",
        "compressed file kholo",
        # --- NEW HINGLISH COMMANDS ---
        "gz file ko extract kardo",
    ],

    "linux.zip": [
        "create a zip file",
        "zip these files",
        "compress files into zip",
        "zip file banao",
        "files ko zip karo",
        "zip archive create karo",
        # --- NEW HINGLISH COMMANDS ---
        "in sabka ek zip bana de",
    ],

    "linux.unzip": [
        "extract zip file",
        "unzip this file",
        "open zip archive",
        "zip file extract karo",
        "unzip kar do",
        "zip archive kholo",
        # --- NEW HINGLISH COMMANDS ---
        "zip file ko bahar nikaalo",
    ],

    # ============================================================
    # TEXT / SHELL UTILITIES
    # ============================================================

    "linux.echo": [
        "print text",
        "display text",
        "print this message",
        "text print karo",
        "message dikhao",
        "terminal me text print karo",
        "echo karo",
        # --- NEW HINGLISH COMMANDS ---
        "screen pe likh ke do",
    ],

    "linux.env": [
        "show environment variables",
        "list environment variables",
        "show env",
        "environment variables dikhao",
        "env variables batao",
        "environment check karo",
        "env command karo",
        # --- NEW HINGLISH COMMANDS ---
        "sare envs print karo",
    ],

    "linux.export": [
        "set environment variable",
        "export an environment variable",
        "set an env variable",
        "environment variable set karo",
        "env variable configure karo",
        "export variable karo",
        # --- NEW HINGLISH COMMANDS ---
        "env set kardo shell me",
    ],

    "linux.alias": [
        "show aliases",
        "create a shell alias",
        "set an alias",
        "shell alias banao",
        "alias create karo",
        "command ka shortcut banao",
        "alias set karo",
        # --- NEW HINGLISH COMMANDS ---
        "is lamba command ka shortcut banado",
    ],

    "linux.history": [
        "show command history",
        "show terminal history",
        "what commands did I run",
        "command history dikhao",
        "terminal history batao",
        "pichle commands dikhao",
        "history check karo",
        # --- NEW HINGLISH COMMANDS ---
        "purane run kiye command dikhao",
    ],

    "linux.clear": [
        "clear terminal",
        "clear the screen",
        "clean terminal",
        "terminal clear karo",
        "screen saaf karo",
        "terminal clean kar do",
        # --- NEW HINGLISH COMMANDS ---
        "screen clear maar do",
        "kachra hatao screen se",
    ],

    "linux.which": [
        "find command location",
        "where is this command installed",
        "find executable path",
        "command kaha installed hai",
        "command ka path batao",
        "executable kaha hai",
        "which command use karo",
        # --- NEW HINGLISH COMMANDS ---
        "ye command kahan se chal raha hai",
    ],

    "linux.whereis": [
        "locate a command",
        "find binary and man page",
        "find command files",
        "command ke files dhundo",
        "binary kaha hai",
        "whereis command karo",
        # --- NEW HINGLISH COMMANDS ---
        "is command ki source file kidhar hai",
    ],

    "linux.man": [
        "show command manual",
        "show manual for command",
        "how does this command work",
        "command ka manual dikhao",
        "command ki documentation batao",
        "man page dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "iska manual open karo",
    ],

    "linux.help": [
        "show command help",
        "get command help",
        "how to use this command",
        "command help dikhao",
        "command ka help batao",
        "help dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "isse use kaise karte hai batao",
    ],

    # ============================================================
    # PROCESS PRIORITY / JOB CONTROL
    # ============================================================

    "linux.nice": [
        "run process with priority",
        "start process with nice value",
        "change process priority",
        "process priority set karo",
        "nice value ke saath process chalao",
        "nice command use karo",
        # --- NEW HINGLISH COMMANDS ---
        "priority ke sath command run karo",
    ],

    "linux.renice": [
        "change process priority",
        "change running process priority",
        "renice a process",
        "running process ki priority change karo",
        "process priority badal do",
        "renice karo",
        # --- NEW HINGLISH COMMANDS ---
        "is chalte task ki priority badha do",
    ],

    # ============================================================
    # CRON / SCHEDULING
    # ============================================================

    "linux.cron.list": [
        "show cron jobs",
        "list scheduled jobs",
        "show my crontab",
        "cron jobs dikhao",
        "scheduled tasks batao",
        "crontab dikhao",
        "cron list karo",
        # --- NEW HINGLISH COMMANDS ---
        "kaun kaun si scripts schedule hain",
    ],

    "linux.cron.edit": [
        "edit cron jobs",
        "create a cron job",
        "schedule a command",
        "cron job banao",
        "command schedule karo",
        "scheduled task add karo",
        "crontab edit karo",
        # --- NEW HINGLISH COMMANDS ---
        "cron setup kardo iska",
    ],

    "linux.cron.remove": [
        "remove cron job",
        "delete scheduled job",
        "delete cron task",
        "cron job hata do",
        "scheduled task delete karo",
        "crontab se job hata do",
        # --- NEW HINGLISH COMMANDS ---
        "cron delete maar do",
    ],

    # ============================================================
    # LOGGING
    # ============================================================

    "linux.logs.system": [
        "show system logs",
        "check system logs",
        "system logs dikhao",
        "system ke logs batao",
        "logs check karo",
        "Linux logs dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "syslog check karo jara",
    ],

    "linux.logs.kernel": [
        "show kernel logs",
        "check kernel messages",
        "kernel logs dikhao",
        "kernel messages batao",
        "dmesg dikhao",
        "kernel errors check karo",
        # --- NEW HINGLISH COMMANDS ---
        "hardware logs batao",
    ],

    "linux.logs.service": [
        "show service logs",
        "check logs for service",
        "service ke logs dikhao",
        "service logs check karo",
        "particular service ke logs batao",
        # --- NEW HINGLISH COMMANDS ---
        "is service ne kya error diya hai",
    ],

    # ============================================================
    # FIREWALL / SECURITY
    # ============================================================

    "ubuntu.ufw.status": [
        "show firewall status",
        "check ufw status",
        "is firewall enabled",
        "firewall status dikhao",
        "ufw status batao",
        "firewall check karo",
        # --- NEW HINGLISH COMMANDS ---
        "ufw chal raha hai ya nahi",
    ],

    "ubuntu.ufw.enable": [
        "enable firewall",
        "turn on ufw",
        "start firewall",
        "firewall enable karo",
        "ufw chalu karo",
        "firewall on kar do",
        # --- NEW HINGLISH COMMANDS ---
        "ufw activate kardo",
    ],

    "ubuntu.ufw.disable": [
        "disable firewall",
        "turn off ufw",
        "stop firewall",
        "firewall disable karo",
        "ufw band karo",
        "firewall off kar do",
        # --- NEW HINGLISH COMMANDS ---
        "ufw ko rok do",
    ],

    "ubuntu.ufw.allow": [
        "allow a port through firewall",
        "open a port in firewall",
        "allow traffic on port",
        "firewall me port allow karo",
        "port open karo",
        "ufw port allow karo",
        # --- NEW HINGLISH COMMANDS ---
        "firewall se is port ko pass hone do",
    ],

    "ubuntu.ufw.deny": [
        "block a port",
        "deny traffic on port",
        "close a port in firewall",
        "firewall me port block karo",
        "port block kar do",
        "ufw port deny karo",
        # --- NEW HINGLISH COMMANDS ---
        "is port ko firewall se block maar do",
    ],

    "ubuntu.ufw.delete_rule": [
        "remove firewall rule",
        "delete ufw rule",
        "firewall rule hata do",
        "ufw rule delete karo",
        "firewall rule remove kar do",
        # --- NEW HINGLISH COMMANDS ---
        "ufw ka ye rule uda do",
    ],

    "linux.sudo": [
        "run command as root",
        "run command with sudo",
        "execute as administrator",
        "root ke taur par command chalao",
        "sudo ke saath command chalao",
        "admin privileges ke saath run karo",
        # --- NEW HINGLISH COMMANDS ---
        "sudo lagake chalao",
        "super user banke execute karo",
    ],

    # ============================================================
    # PACKAGE / BINARY DISCOVERY
    # ============================================================

    "linux.command.version": [
        "show command version",
        "check installed version",
        "what version is installed",
        "version batao",
        "installed version check karo",
        "command ka version dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "kaunsa version chal raha hai",
    ],

    "linux.command.exists": [
        "check if command is installed",
        "is this command installed",
        "check whether package exists",
        "command installed hai kya",
        "ye command available hai kya",
        "command installed check karo",
        # --- NEW HINGLISH COMMANDS ---
        "system me ye hai ya nahi",
    ],

    # ============================================================
    # SYSTEM SHUTDOWN / REBOOT
    # ============================================================

    "linux.shutdown": [
        "shutdown the system",
        "turn off the computer",
        "power off the system",
        "system shutdown karo",
        "computer band karo",
        "machine shutdown kar do",
        "system ko off karo",
        # --- NEW HINGLISH COMMANDS ---
        "pc band kardo",
    ],

    "linux.reboot": [
        "restart the system",
        "reboot the computer",
        "restart machine",
        "system restart karo",
        "computer reboot karo",
        "machine ko restart kar do",
        "server reboot karo",
        # --- NEW HINGLISH COMMANDS ---
        "machine ko reset maar do",
    ],

    "linux.logout": [
        "logout",
        "log me out",
        "exit user session",
        "logout karo",
        "session se bahar niklo",
        "user session close karo",
        # --- NEW HINGLISH COMMANDS ---
        "mera account log out kardo",
    ],

    # ============================================================
    # TERMINAL / SHELL
    # ============================================================

    "linux.exit": [
        "exit terminal",
        "close terminal",
        "exit shell",
        "terminal band karo",
        "shell se bahar niklo",
        "terminal close kar do",
        "exit karo",
        # --- NEW HINGLISH COMMANDS ---
        "terminal khatam kardo",
    ],

    "linux.source": [
        "reload shell configuration",
        "source bashrc",
        "reload bash configuration",
        "bashrc reload karo",
        "shell config reload karo",
        "configuration dobara load karo",
        # --- NEW HINGLISH COMMANDS ---
        "bash profile source maar do",
    ],

    "linux.bash": [
        "run bash",
        "open bash shell",
        "start bash",
        "bash shell kholo",
        "bash chalao",
        # --- NEW HINGLISH COMMANDS ---
        "nayi bash session kholo",
    ],

    "linux.ssh.exit": [
        "exit ssh session",
        "disconnect from server",
        "logout from ssh",
        "ssh session close karo",
        "server se disconnect karo",
        "remote server se bahar niklo",
        # --- NEW HINGLISH COMMANDS ---
        "ssh se nikal aao",
    ],

    # ============================================================
    # DOCKER
    # ============================================================

    "docker.ps": [
        "show docker containers",
        "list running containers",
        "docker containers dikhao",
        "running containers batao",
        "docker ke status dikhau",
        "docker ps karo",
        "containers list karo",
        # --- NEW HINGLISH COMMANDS ---
        "kaunse containers chal rahe hain batao",
        "active docker process dikha de",
        "chalte hue containers ki list do",
    ],

    "docker.ps.all": [
        "show all docker containers",
        "list all containers",
        "show stopped containers",
        "saare containers dikhao",
        "stopped containers bhi dikhao",
        "all docker containers batao",
        # --- NEW HINGLISH COMMANDS ---
        "sab containers dikha do chahe band ho",
    ],

    "docker.images": [
        "list docker images",
        "show docker images",
        "docker images dikhao",
        "images list karo",
        "available docker images batao",
        # --- NEW HINGLISH COMMANDS ---
        "mere pas kaunsi images hai",
    ],

    "docker.pull": [
        "pull docker image",
        "download docker image",
        "docker image pull karo",
        "image download karo",
        "docker hub se image lao",
        # --- NEW HINGLISH COMMANDS ---
        "image ko server se pull kar lo",
    ],

    "docker.run": [
        "run a docker container",
        "start a container",
        "create and run docker container",
        "docker container chalao",
        "container start karo",
        "docker run karo",
        # --- NEW HINGLISH COMMANDS ---
        "image ko container me chalu karo",
    ],

    "docker.stop": [
        "stop docker container",
        "stop a container",
        "docker container band karo",
        "container stop kar do",
        "docker stop karo",
        # --- NEW HINGLISH COMMANDS ---
        "is container ko rok do",
    ],

    "docker.start": [
        "start docker container",
        "start a stopped container",
        "docker container start karo",
        "stopped container chalao",
        "docker start karo",
        # --- NEW HINGLISH COMMANDS ---
        "band container ko on kardo",
    ],

    "docker.restart": [
        "restart docker container",
        "restart a container",
        "container restart karo",
        "docker container ko restart karo",
        # --- NEW HINGLISH COMMANDS ---
        "phir se restart maar do",
    ],

    "docker.rm": [
        "remove docker container",
        "delete container",
        "docker container hata do",
        "container remove karo",
        "docker rm karo",
        # --- NEW HINGLISH COMMANDS ---
        "container ko uda do",
    ],

    "docker.rmi": [
        "remove docker image",
        "delete docker image",
        "docker image hata do",
        "image remove karo",
        "docker rmi karo",
        # --- NEW HINGLISH COMMANDS ---
        "image ko delete maar do",
    ],

    "docker.logs": [
        "show docker logs",
        "show container logs",
        "docker container logs dikhao",
        "container ke logs batao",
        "docker logs karo",
        # --- NEW HINGLISH COMMANDS ---
        "container me kya error hai dikhao",
    ],

    "docker.exec": [
        "execute command inside container",
        "open shell inside container",
        "enter docker container",
        "container ke andar jao",
        "container me command chalao",
        "docker exec karo",
        # --- NEW HINGLISH COMMANDS ---
        "container ke andar bash khol do",
    ],

    # ============================================================
    # SYSTEM NETWORK CONFIGURATION
    # ============================================================

    "linux.networkmanager.status": [
        "show network manager status",
        "check network manager",
        "network manager status dikhao",
        "NetworkManager check karo",
        # --- NEW HINGLISH COMMANDS ---
        "network ka status kya hai",
    ],

    "linux.networkmanager.restart": [
        "restart network manager",
        "restart networking",
        "network manager restart karo",
        "network restart kar do",
        "network service restart karo",
        # --- NEW HINGLISH COMMANDS ---
        "internet reset maar do",
    ],

    "linux.dns.status": [
        "check DNS configuration",
        "show DNS settings",
        "DNS configuration dikhao",
        "DNS settings batao",
        "DNS check karo",
        # --- NEW HINGLISH COMMANDS ---
        "name server ki setting dikhao",
    ],

    # ============================================================
    # FILE LINKS
    # ============================================================

    "linux.ln": [
        "create a symbolic link",
        "create symlink",
        "make a link to a file",
        "symbolic link banao",
        "symlink create karo",
        "file ka link bana do",
        "ln command karo",
        # --- NEW HINGLISH COMMANDS ---
        "shortcut bana do is file ka",
    ],

    "linux.ln.hard": [
        "create a hard link",
        "make a hard link",
        "hard link banao",
        "hard link create karo",
        "file ka hard link bana do",
        # --- NEW HINGLISH COMMANDS ---
        "iska ek clone link banao",
    ],

    # ============================================================
    # DISK / FILESYSTEM
    # ============================================================

    "linux.mount.list": [
        "show mounted filesystems",
        "list mounted drives",
        "show mounted disks",
        "mounted drives dikhao",
        "kaunse disks mounted hain",
        "mounted filesystems batao",
        # --- NEW HINGLISH COMMANDS ---
        "kaunsi drives lagi hai batao",
    ],

    "linux.fsck": [
        "check filesystem",
        "check filesystem errors",
        "repair filesystem",
        "filesystem check karo",
        "disk filesystem errors dhundo",
        "filesystem repair karo",
        # --- NEW HINGLISH COMMANDS ---
        "hard disk scan maar do",
    ],

    # ============================================================
    # PACKAGE FILES
    # ============================================================

    "ubuntu.dpkg.list": [
        "list installed deb packages",
        "show installed dpkg packages",
        "installed deb packages dikhao",
        "dpkg packages list karo",
        "installed deb files batao",
        # --- NEW HINGLISH COMMANDS ---
        "kon kon se deb packages hain",
    ],

    "ubuntu.dpkg.install": [
        "install a deb package",
        "install deb file",
        "install this deb",
        "deb package install karo",
        "deb file install kar do",
        "dpkg se install karo",
        # --- NEW HINGLISH COMMANDS ---
        "is deb file ko install kardo",
    ],

    "ubuntu.dpkg.remove": [
        "remove deb package",
        "uninstall deb package",
        "deb package hata do",
        "dpkg package remove karo",
        # --- NEW HINGLISH COMMANDS ---
        "deb file ko delete maar do",
    ],

    # ====================================
    #           git command intents           
    # ====================================            

    "git.branch.list": [
        "show git branches",
        "list all branches",
        "git ke branches dikhao",
        "branch dikha do",
        "kaunse branches hai",
        "git branches dikhao",
        "saare branches dikhao",
        "branches ki list dikhao",
        "current branches batao",
        "git me kitne branches hai",
        "mere branches dikhao",
        "all branches show karo",
        "branches show kar",
        "branch list karo",
        "git branch dikha",
        # --- NEW HINGLISH COMMANDS ---
        "branches batao konsi hai",
    ],

    "git.branch.create": [
        "create a new branch",
        "naya branch banao",
        "branch banado",
        "new branch create karo",
        "ek naya branch bana do",
        "branch bana de",
        "git me naya branch banao",
        "new branch bana do",
        "branch create kar do",
        "ek branch bana",
        "branch banana hai",
        "nayi branch create karni hai",
        "git branch bana do",
        "new branch bana",
        "branch create karo",
        "ek naya branch bana",
        "branch banani hai",
        # --- NEW HINGLISH COMMANDS ---
        "nayi branch me daal do",
    ],

    "git.branch.delete": [
        "delete the branch",
        "delete this branch",
        "remove the branch",
        "branch delete karo",
        "branch hata do",
        "branch remove kar do",
        "ye branch delete karo",
        "branch ko delete kar do",
        "branch hata de",
        "is branch ko hata do",
        "git branch delete karo",
        "branch remove karo",
        "branch ko remove karna hai",
        "branch mita do",
        "branch delete karni hai",
        # --- NEW HINGLISH COMMANDS ---
        "is branch ko uda do",
    ],

    "git.branch.rename": [
        "rename the branch",
        "rename this branch",
        "change branch name",
        "branch ka naam change karo",
        "branch rename karo",
        "branch ka naam badal do",
        "is branch ka naam change karo",
        "branch ko rename kar do",
        "branch ka naam rename karo",
        "current branch ka naam badal do",
        "branch rename karni hai",
        # --- NEW HINGLISH COMMANDS ---
        "branch ka naya naam rakh do",
    ],

    "git.branch.current": [
        "show current branch",
        "which branch am I on",
        "what branch am I on",
        "current branch batao",
        "abhi kaunsa branch hai",
        "main kaunsa branch hai",
        "current branch dikhao",
        "meri current branch batao",
        "main branch check karo",
        "current branch check karo",
        "abhi kis branch par hoon",
        # --- NEW HINGLISH COMMANDS ---
        "konsi branch me hu mai",
    ],

    "git.branch.switch": [
        "switch branch",
        "switch to another branch",
        "change branch",
        "checkout another branch",
        "branch change karo",
        "branch switch karo",
        "dusre branch par jao",
        "branch badal do",
        "is branch par switch karo",
        "branch change karni hai",
        "dusri branch me jao",
        "branch checkout karo",
        "branch par switch kar do",
        # --- NEW HINGLISH COMMANDS ---
        "waha wali branch me chalo",
    ],

    "git.branch.checkout": [
        "checkout the branch",
        "checkout a branch",
        "git checkout branch",
        "branch checkout karo",
        "branch ko checkout karo",
        "is branch ko checkout kar do",
        "branch checkout karni hai",
        "checkout branch",
        "branch par checkout karo",
        "git me branch checkout karo",
    ],

    "git.branch.merge": [
        "merge the branch",
        "merge this branch",
        "merge two branches",
        "merge branch",
        "branch merge karo",
        "branch ko merge kar do",
        "ye branch merge karo",
        "do branches ko merge karo",
        "branch ko main me merge karo",
        "merge karna hai",
        "is branch ko merge kar do",
        "git branch merge karo",
        # --- NEW HINGLISH COMMANDS ---
        "code merge maar do",
    ],

    "git.branch.rebase": [
        "rebase the branch",
        "rebase this branch",
        "rebase branch",
        "branch rebase karo",
        "branch ko rebase kar do",
        "rebase karna hai",
        "git rebase karo",
        "current branch ko rebase karo",
        "branch ko main ke upar rebase karo",
        # --- NEW HINGLISH COMMANDS ---
        "code base rebase kardo",
    ],

    "git.status": [
        "git status dikhao",
        "check git status",
        "kya changes hai",
        "show git status",
        "status dikhao",
        "git ka status batao",
        "repo ka status dikhao",
        "repository status check karo",
        "kya change hua hai",
        "working tree ka status dikhao",
        "mere changes dikhao",
        "git status check karo",
        "abhi git me kya status hai",
        "working directory ka status dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "repo ka haal batao",
        "uncommitted changes batao yaar",
    ],

    "git.add": [
        "add the files",
        "stage the files",
        "git add files",
        "files ko stage karo",
        "files add karo",
        "changes stage karo",
        "saare files stage karo",
        "all files add karo",
        "git me files add karo",
        "changes ko stage kar do",
        "file ko staging me daalo",
        "files ko git me add karo",
        "sab changes stage karo",
        # --- NEW HINGLISH COMMANDS ---
        "stage kar le bhai ye file",
    ],

    "git.add.all": [
        "add all files",
        "stage all files",
        "git add all",
        "saari files add karo",
        "sabhi files stage karo",
        "saare changes add karo",
        "all changes stage karo",
        "sab files ko stage kar do",
        "poora project stage karo",
        "everything stage karo",
        "saare changes ko git add karo",
        # --- NEW HINGLISH COMMANDS ---
        "sab kuch add maar do",
    ],

    "git.commit": [
        "commit the changes",
        "create a commit",
        "commit changes",
        "changes commit karo",
        "commit kar do",
        "changes ko commit karo",
        "git commit karo",
        "ek commit bana do",
        "changes commit karne hain",
        "commit create karo",
        "saare changes commit karo",
        "changes ko commit kar do",
        # --- NEW HINGLISH COMMANDS ---
        "code commit maar do",
        "changes save kar lo git me",
    ],

    "git.commit.message": [
        "commit with message",
        "create commit with a message",
        "commit message set karo",
        "message ke saath commit karo",
        "commit message ke saath commit karo",
        "is message se commit karo",
        "commit karo aur message add karo",
        "message ke saath changes commit karo",
        "commit message do",
        # --- NEW HINGLISH COMMANDS ---
        "description ke sath commit karo",
    ],

    "git.commit.history": [
        "show commit history",
        "show git commits",
        "list commits",
        "git log dikhao",
        "commits dikhao",
        "commit history batao",
        "saare commits dikhao",
        "recent commits dikhao",
        "git ki history dikhao",
        "commit history show karo",
        "pichle commits dikhao",
        "git log show karo",
        # --- NEW HINGLISH COMMANDS ---
        "history log dikha do",
    ],

    "git.commit.last": [
        "show the last commit",
        "show latest commit",
        "last commit dikhao",
        "latest commit batao",
        "recent commit dikhao",
        "last commit kya tha",
        "sabse recent commit dikhao",
        "latest commit show karo",
        "last commit check karo",
        # --- NEW HINGLISH COMMANDS ---
        "aakhiri wala commit dikhao",
    ],

    "git.diff": [
        "show git diff",
        "show my changes",
        "show differences",
        "git diff dikhao",
        "changes ka diff dikhao",
        "kya changes kiye hain dikhao",
        "changes compare karo",
        "difference dikhao",
        "mere changes ka diff batao",
        "git changes dikhao",
        "uncommitted changes dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "kya badla hai code me batao",
    ],

    "git.diff.staged": [
        "show staged changes",
        "show staged diff",
        "staged changes dikhao",
        "staging ka diff dikhao",
        "jo changes stage kiye hain dikhao",
        "staged files ka diff dikhao",
        "staged changes check karo",
        "git staged diff dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "stage wale file me kya diff hai",
    ],

    "git.push": [
        "push the changes",
        "push to git",
        "push changes to remote",
        "git push karo",
        "changes push karo",
        "remote par push karo",
        "code push kar do",
        "changes ko github par push karo",
        "branch push karo",
        "remote branch par push karo",
        "git me push kar do",
        # --- NEW HINGLISH COMMANDS ---
        "code server pe daal do",
        "github pe push maar do",
    ],

    "git.push.remote": [
        "push to remote repo",
        "remote me push karo code",
        "url mein push karo",
        "push code in remote repo with url ",
        "repo mein code push karo with url",
        "remote repo mein push karo",
        "repo mein changes push karo",
        "repo mein changes push karo ",
        "push the changed code to remote repo with url",
    ],

    "git.push.branch":[
        "remote branch mein push karo",
        "remote url wale branch mein push karo",
        "push to repo with branch in url",
        "code push kardo in branch named",
        "changes push karo in in branch",
        "sab push kar do with branch",
        "remote branch push codes with url",
    ],

    "git.pull": [
        "pull the latest changes",
        "git pull karo",
        "latest changes pull karo",
        "remote se changes lao",
        "latest code lao",
        "remote changes download karo",
        "git se latest changes lao",
        "repository update karo",
        "remote ka latest code pull karo",
        "changes pull kar do",
        # --- NEW HINGLISH COMMANDS ---
        "upar se naya code le aao",
    ],

    "git.fetch": [
        "fetch the latest changes",
        "git fetch karo",
        "remote changes fetch karo",
        "latest changes fetch karo",
        "remote se updates fetch karo",
        "git se fetch karo",
        "remote branches update karo",
        "remote ki latest information lao",
        "fetch kar do",
        # --- NEW HINGLISH COMMANDS ---
        "updates fetch maar lo",
    ],

    "git.remote.list": [
        "show git remotes",
        "list remote repositories",
        "show remote",
        "git remotes dikhao",
        "remote repositories dikhao",
        "configured remotes batao",
        "git remote list karo",
        "remote urls dikhao",
        "mere git remotes dikhao",
        "remote connections dikhao",
    ],

    "git.remote.verbose": [
        "show remote repositories",
        "show git remotes",
        "list git remotes",
        "list remote repositories",
        "show all remotes",
        "git remote dikhao",
        "git remotes dikhao",
        "remote dikhao",
        "remote repositories dikhao",
        "kaunse remotes hai",
        "git ke remotes dikhao",
        "git remote list karo",
        "remote list karo",
        "remote connections dikhao",
        "github remotes dikhao",
        "remote urls dikhao",
        "git remote urls dikhao",
        "remote ka url dikhao",
        "remotes aur unke urls dikhao",
        "remote details dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "remote with verbose batao",
    ],

    "git.remote.add": [
        "add a remote",
        "add git remote",
        "new remote add karo",
        "git remote add karo",
        "remote repository add karo",
        "remote connect karo",
        "github remote add karo",
        "naya remote configure karo",
        "remote repository connect karo",
        # --- NEW HINGLISH COMMANDS ---
        "ek remote aur jod do",
    ],

    "git.remote.remove": [
        "remove the remote",
        "delete git remote",
        "remove remote repository",
        "remote hata do",
        "git remote delete karo",
        "remote remove karo",
        "configured remote hata do",
        "git remote ko remove karo",
        # --- NEW HINGLISH COMMANDS ---
        "remote disconnect kardo",
    ],

    "git.remote.show": [
        "show remote details",
        "show remote information",
        "remote details dikhao",
        "remote ka information batao",
        "remote url batao",
        "remote details check karo",
        "git remote details dikhao",
        "remote configuration dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "remote pe kya detail hai dikhao",
    ],

    "git.log": [
        "show git log",
        "show git history",
        "git log dikhao",
        "git history batao",
        "repository history dikhao",
        "commit log dikhao",
        "git ka pura log dikhao",
        "history check karo",
        "repository ke commits dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "pura khata dikha do",
    ],

    "git.log.graph": [
        "show git log graph",
        "show branch history graph",
        "git graph dikhao",
        "branch graph dikhao",
        "commit graph show karo",
        "git history graph dikhao",
        "branches ka graph dikhao",
        "visual git history dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "graph me dikhao commits ko",
    ],

    "git.stash": [
        "stash my changes",
        "save my changes temporarily",
        "git stash karo",
        "changes stash kar do",
        "changes ko temporarily save karo",
        "current changes stash karo",
        "changes side me rakh do",
        "kaam temporarily save karo",
        "git changes stash kar do",
        # --- NEW HINGLISH COMMANDS ---
        "bad me use karne ke liye chupa do code",
    ],

    "git.stash.list": [
        "show stashes",
        "list git stashes",
        "git stash list dikhao",
        "stashed changes dikhao",
        "mere stashes dikhao",
        "stash list karo",
        "saved stashes dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "stash ki puri list dikhao",
    ],

    "git.stash.apply": [
        "apply the stash",
        "restore stashed changes",
        "stash apply karo",
        "stash ke changes wapas lao",
        "stashed changes restore karo",
        "stash ko apply kar do",
        "saved changes wapas lao",
        "stash changes restore kar do",
        # --- NEW HINGLISH COMMANDS ---
        "chupe hue changes wapas laao",
    ],

    "git.stash.pop": [
        "pop the stash",
        "apply and remove the stash",
        "git stash pop karo",
        "stash pop kar do",
        "stash ke changes wapas lao aur hata do",
        "stash restore karke remove karo",
        # --- NEW HINGLISH COMMANDS ---
        "stash apply kar aur uda de",
    ],

    "git.reset": [
        "reset the changes",
        "git reset karo",
        "changes reset kar do",
        "git changes undo karo",
        "reset my changes",
        "changes ko reset karo",
        "git reset karna hai",
        # --- NEW HINGLISH COMMANDS ---
        "piche jao reset karke",
    ],

    "git.reset.hard": [
        "hard reset",
        "reset everything",
        "discard all changes",
        "git hard reset karo",
        "saare changes hata do",
        "all changes discard karo",
        "working changes delete karo",
        "changes completely reset karo",
        "sab kuch reset kar do",
        # --- NEW HINGLISH COMMANDS ---
        "pura clean reset maar do",
    ],

    "git.revert": [
        "revert the commit",
        "undo the commit",
        "git revert karo",
        "commit revert kar do",
        "last commit undo karo",
        "commit ko reverse karo",
        "commit ke changes undo karo",
        "previous commit revert karo",
        # --- NEW HINGLISH COMMANDS ---
        "commit wapas le lo",
    ],

    "git.tag.list": [
        "show git tags",
        "list all tags",
        "git ke tags dikhao",
        "git tags ki list dikhao",
        "all tags show karo",
        "repository tags batao",
        "git tag list karo",
    ],

    "git.tag.create": [
        "create a git tag",
        "create a new tag",
        "git tag banao",
        "new tag create karo",
        "tag bana do",
        "git me tag create karo",
        "release tag banao",
        "ek tag bana do",
        # --- NEW HINGLISH COMMANDS ---
        "is version ko tag kardo",
    ],

    "git.tag.delete": [
        "delete the tag",
        "remove git tag",
        "git tag delete karo",
        "tag hata do",
        "tag remove kar do",
        "git tag ko delete karo",
        "tag delete karni hai",
        # --- NEW HINGLISH COMMANDS ---
        "tag ko uda do",
    ],

    "git.remote.branch.list": [
        "show remote branches",
        "list remote branches",
        "remote branches dikhao",
        "remote ke branches batao",
        "github branches dikhao",
        "remote branch list karo",
        "saare remote branches dikhao",
        "remote branches show karo",
        # --- NEW HINGLISH COMMANDS ---
        "server wali branches batao",
    ],

    "git.remote.branch.delete": [
        "delete remote branch",
        "remove remote branch",
        "remote branch delete karo",
        "github se branch delete karo",
        "remote branch hata do",
        "remote par branch remove karo",
        "remote branch ko delete kar do",
        # --- NEW HINGLISH COMMANDS ---
        "server se branch delete maar do",
    ],

    "git.clone": [
        "clone a repository",
        "git clone karo",
        "repository clone karo",
        "repo download karo",
        "github repository clone karo",
        "remote repository clone karni hai",
        "repo ko local me clone karo",
        "repository local me lao",
        # --- NEW HINGLISH COMMANDS ---
        "pura repo utha ke laao",
    ],

    "git.init": [
        "initialize git",
        "initialize a git repository",
        "git init karo",
        "new git repository banao",
        "is folder me git initialize karo",
        "git repo initialize kar do",
        "folder ko git repository banao",
        "git repository setup karo",
        # --- NEW HINGLISH COMMANDS ---
        "yaha pe naya git bana do",
    ],

    "git.config.get": [
        "show git config",
        "show git configuration",
        "git config dikhao",
        "git configuration batao",
        "git settings dikhao",
        "current git config dikhao",
        "git configuration check karo",
    ],

    "git.config.user": [
        "show git username",
        "show git user email",
        "git username batao",
        "git email batao",
        "configured git user dikhao",
        "git user details batao",
        "git config user check karo",
    ],

    "git.config.set": [
        "set git username",
        "set git email",
        "change git username",
        "change git email",
        "git username set karo",
        "git email set karo",
        "git user configure karo",
        "git configuration change karo",
        # --- NEW HINGLISH COMMANDS ---
        "mera naam and email set kardo",
    ],

    "git.diff.compare": [
        "compare two branches",
        "compare branches",
        "compare branch changes",
        "do branches compare karo",
        "branches ke differences dikhao",
        "branch compare karni hai",
        "two branches ka diff dikhao",
        "branches me kya difference hai",
        # --- NEW HINGLISH COMMANDS ---
        "dono branches milake check karo",
    ],

    "git.file.restore": [
        "restore a file",
        "discard changes from a file",
        "restore file from git",
        "file ke changes hata do",
        "file restore karo",
        "file ko previous state me lao",
        "file changes undo karo",
        "file ko git se restore karo",
        # --- NEW HINGLISH COMMANDS ---
        "file me kiye gaye changes wapas lo",
    ],

    "git.untracked.list": [
        "show untracked files",
        "list untracked files",
        "untracked files dikhao",
        "kaunse files untracked hai",
        "untracked files batao",
        "git ke untracked files dikhao",
        "new files dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "nayi add hui files dikhao",
    ],

    "git.clean": [
        "remove untracked files",
        "clean untracked files",
        "git clean karo",
        "untracked files hata do",
        "extra files remove karo",
        "untracked files delete karo",
        "working directory clean karo",
        # --- NEW HINGLISH COMMANDS ---
        "untracked kachra saaf kardo",
    ],

    "git.blame": [
        "show git blame",
        "who changed this line",
        "who wrote this code",
        "git blame dikhao",
        "is line ko kisne change kiya",
        "ye code kisne likha",
        "file ka blame dikhao",
        "kis developer ne change kiya",
        # --- NEW HINGLISH COMMANDS ---
        "kisne foda ye code batao",
    ],

    "git.show": [
        "show a commit",
        "show commit details",
        "git show karo",
        "commit details dikhao",
        "commit ka complete information dikhao",
        "commit me kya changes the",
        "commit details batao",
    ],

    "git.cherry_pick": [
        "cherry pick a commit",
        "cherry pick this commit",
        "git cherry pick karo",
        "commit cherry pick karo",
        "ek commit ko current branch me lao",
        "commit ko dusri branch me apply karo",
        "specific commit apply karo",
        # --- NEW HINGLISH COMMANDS ---
        "wo wala commit yaha le aao",
    ],

    "git.reflog": [
        "show reflog",
        "git reflog dikhao",
        "show git reference log",
        "reflog check karo",
        "git reflog show karo",
        "previous git actions dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "git ki saari history nikaalo",
    ],

    "git.remote.prune": [
        "prune remote branches",
        "remove deleted remote branches",
        "git remote prune karo",
        "deleted remote branches hata do",
        "stale remote branches remove karo",
        "remote branches clean karo",
        # --- NEW HINGLISH COMMANDS ---
        "jo branches waha nahi hai unhe uda do",
    ],

    # ============================================================
    # CONTAINERS
    # ============================================================

    "docker.container.list": [
        "show running docker containers",
        "list running containers",
        "docker containers dikhao",
        "running containers dikhao",
        "kaunse containers chal rahe hain",
        "docker mein kya kya containers running hain",
        "show me running containers",
        "docker ke running containers batao",
        "active containers dikhao",
        "abhi kaunse containers chal rahe hain",
        # --- NEW HINGLISH COMMANDS ---
        "container dikhao jo chal rahe hain",
    ],

    "docker.container.list.all": [
        "show all docker containers",
        "list all containers",
        "docker ke saare containers dikhao",
        "running aur stopped containers dikhao",
        "all containers batao",
        "docker mein saare containers kaunse hain",
        "stopped containers bhi dikhao",
        "show every docker container",
        "docker ke sabhi containers list karo",
        "saare containers dikha do",
        # --- NEW HINGLISH COMMANDS ---
        "sare container dikhao chalte ho ya na chalte ho",
    ],

    "docker.container.run": [
        "run a docker container",
        "start a container from an image",
        "docker container chalao",
        "image se container run karo",
        "docker image ko run karo",
        "container start karo image se",
        "is image ka container chala do",
        "run this docker image",
        # --- NEW HINGLISH COMMANDS ---
        "container up kardo iska",
    ],

    "docker.container.run.name": [
        "run the container with a name",
        "create a named docker container",
        "container ko naam ke saath run karo",
        "docker container ka naam set karo",
        "named container chalao",
        "image ko is naam ke container mein run karo",
        # --- NEW HINGLISH COMMANDS ---
        "naam de kar container chalao",
    ],

    "docker.container.run.port": [
        "run docker container on a port",
        "map a docker port",
        "container ko port ke saath run karo",
        "docker port expose karo",
        "host port ko container port se map karo",
        "port mapping ke saath container chalao",
        "container ka port map karo",
        # --- NEW HINGLISH COMMANDS ---
        "port forward karke chalao",
    ],

    "docker.container.run.detached": [
        "run the container in background",
        "run docker container detached",
        "container ko background mein chalao",
        "docker container background mein run karo",
        "detached mode mein container chalao",
        "container ko background mein start karo",
        # --- NEW HINGLISH COMMANDS ---
        "piche chala do container",
    ],

    "docker.container.run.interactive": [
        "run docker container interactively",
        "start container in interactive mode",
        "container ko interactive mode mein chalao",
        "docker container ke andar interactively jao",
        "interactive container run karo",
        "container ko terminal ke saath run karo",
        # --- NEW HINGLISH COMMANDS ---
        "container ke andar ghuske chalao",
    ],

    "docker.container.start": [
        "start a docker container",
        "start the container",
        "docker container start karo",
        "stopped container ko start karo",
        "container chala do",
        "docker container ko dobara start karo",
        "container ko activate karo",
        # --- NEW HINGLISH COMMANDS ---
        "band container shuru karo",
    ],

    "docker.container.stop": [
        "stop a docker container",
        "stop the container",
        "docker container band karo",
        "container ko stop karo",
        "running container ko band kar do",
        "docker container rok do",
        "container ko terminate karo",
        # --- NEW HINGLISH COMMANDS ---
        "docker container off kardo",
    ],

    "docker.container.restart": [
        "restart a docker container",
        "restart the container",
        "docker container restart karo",
        "container ko dobara start karo",
        "container restart kar do",
        "docker container ko restart karna hai",
        "container ko phir se chalao",
        # --- NEW HINGLISH COMMANDS ---
        "phir se chalado container ko",
    ],

    "docker.container.pause": [
        "pause a docker container",
        "pause the container",
        "docker container pause karo",
        "container ko temporarily rok do",
        "container ko pause kar do",
        "running container ko pause karo",
        # --- NEW HINGLISH COMMANDS ---
        "container ko freeze kardo",
    ],

    "docker.container.unpause": [
        "unpause the docker container",
        "resume a paused container",
        "paused container ko resume karo",
        "docker container ko unpause karo",
        "container ko wapas chalao",
        "paused container start karo",
        # --- NEW HINGLISH COMMANDS ---
        "container wapas on kardo",
    ],

    "docker.container.kill": [
        "kill a docker container",
        "forcefully stop the container",
        "docker container ko kill karo",
        "container ko forcefully band karo",
        "container ko zabardasti stop karo",
        "docker container kill kar do",
        # --- NEW HINGLISH COMMANDS ---
        "container mita do abhi",
    ],

    "docker.container.remove": [
        "remove a docker container",
        "delete a container",
        "docker container delete karo",
        "container ko remove karo",
        "docker ka container hata do",
        "container delete kar do",
        "stopped container ko remove karo",
        # --- NEW HINGLISH COMMANDS ---
        "container uda do",
    ],

    "docker.container.remove.force": [
        "force remove a docker container",
        "force delete the container",
        "container ko forcefully delete karo",
        "docker container ko zabardasti remove karo",
        "force se container hata do",
        "container ko force remove karo",
        # --- NEW HINGLISH COMMANDS ---
        "container completely uda do",
    ],

    "docker.container.inspect": [
        "inspect a docker container",
        "show container details",
        "container ki details dikhao",
        "docker container inspect karo",
        "container ke baare mein information do",
        "container ka configuration dikhao",
        "container ki complete details batao",
        # --- NEW HINGLISH COMMANDS ---
        "container ke bare me puri khabar do",
    ],

    "docker.container.logs": [
        "show container logs",
        "show docker logs",
        "container ke logs dikhao",
        "docker container ka log batao",
        "container mein kya logs aaye hain",
        "container ki output dikhao",
        "docker ke logs check karo",
        # --- NEW HINGLISH COMMANDS ---
        "container ki logs print karo",
    ],

    "docker.container.logs.follow": [
        "follow container logs",
        "show live container logs",
        "container ke live logs dikhao",
        "docker logs ko continuously dekho",
        "container ke logs follow karo",
        "live docker logs chahiye",
        "real time container logs dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "logs continuously dekho",
    ],

    "docker.container.logs.tail": [
        "show last few container logs",
        "show the last 100 lines of logs",
        "container ke last logs dikhao",
        "sirf last few logs dikhao",
        "container ke recent logs batao",
        "last lines of docker logs dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "thode logs dikhao bas",
    ],

    "docker.container.stats": [
        "show container resource usage",
        "show docker container stats",
        "container ka cpu aur memory usage dikhao",
        "docker container ki stats batao",
        "container kitna cpu use kar raha hai",
        "container ki memory usage dikhao",
        "container ka resource usage check karo",
        # --- NEW HINGLISH COMMANDS ---
        "container ki memory consume kitni hai",
    ],

    "docker.container.top": [
        "show processes running inside the container",
        "show container processes",
        "container ke andar kaunse processes chal rahe hain",
        "docker container ke processes dikhao",
        "container ke running processes batao",
        "container ke andar kya run ho raha hai",
        # --- NEW HINGLISH COMMANDS ---
        "container ke andar kon kon chal raha hai",
    ],

    "docker.container.exec": [
        "execute a command inside the container",
        "run a command inside docker container",
        "container ke andar command chalao",
        "docker container mein command execute karo",
        "container ke andar command run karo",
        "container ke andar kuch execute karna hai",
        # --- NEW HINGLISH COMMANDS ---
        "container ke andar ye run karo",
    ],

    "docker.container.exec.interactive": [
        "open a shell inside the container",
        "enter the docker container",
        "open terminal inside the container",
        "container ke andar shell kholo",
        "docker container ke andar jao",
        "container mein terminal open karo",
        "container ke andar interactive shell chahiye",
        # --- NEW HINGLISH COMMANDS ---
        "container ke shell me ghus jao",
    ],

    "docker.container.rename": [
        "rename a docker container",
        "change container name",
        "docker container ka naam badlo",
        "container rename karo",
        "container ka naam change kar do",
        "docker container ko naya naam do",
        # --- NEW HINGLISH COMMANDS ---
        "container ka name update kardo",
    ],

    "docker.container.cp.to": [
        "copy a file into the container",
        "copy files from host to container",
        "host se container mein file copy karo",
        "container ke andar file bhejo",
        "docker container mein file copy karo",
        "local file ko container mein copy karo",
        # --- NEW HINGLISH COMMANDS ---
        "file ko container ke andar daal do",
    ],

    "docker.container.cp.from": [
        "copy a file from the container",
        "copy files from container to host",
        "container se file bahar copy karo",
        "container se host mein file copy karo",
        "docker container se file nikalo",
        "container ki file local machine par copy karo",
        # --- NEW HINGLISH COMMANDS ---
        "container ke andar ki file bahar laao",
    ],


    # ============================================================
    # IMAGES
    # ============================================================

    "docker.image.list": [
        "show docker images",
        "list docker images",
        "docker images dikhao",
        "mere paas kaunse docker images hain",
        "all docker images batao",
        "available docker images dikhao",
        "docker ki images list karo",
        "local images dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "downloaded images dikha do",
        "system me kaun kaun si images hain",
        "docker images ki list print karo",
    ],

    "docker.image.list.all": [
        "show all docker images",
        "show dangling and normal images",
        "docker ki saari images dikhao",
        "all images including intermediate images",
        "docker images with all layers dikhao",
        "all local docker images batao",
        # --- NEW HINGLISH COMMANDS ---
        "saari images list karo hidden bhi",
    ],

    "docker.image.pull": [
        "pull a docker image",
        "download a docker image",
        "docker image download karo",
        "docker hub se image lao",
        "image pull karo",
        "docker ki image download kar do",
        "remote docker image local mein lao",
        # --- NEW HINGLISH COMMANDS ---
        "image server se le aao",
    ],

    "docker.image.push": [
        "push a docker image",
        "upload docker image",
        "docker image registry mein upload karo",
        "image ko docker hub par push karo",
        "docker image upload kar do",
        "local image ko registry mein bhejo",
        # --- NEW HINGLISH COMMANDS ---
        "image upar dal do",
    ],

    "docker.image.remove": [
        "remove a docker image",
        "delete a docker image",
        "docker image delete karo",
        "image ko remove karo",
        "docker image hata do",
        "local docker image delete kar do",
        # --- NEW HINGLISH COMMANDS ---
        "ye image uda do yar",
    ],

    "docker.image.remove.force": [
        "force remove a docker image",
        "force delete docker image",
        "docker image ko forcefully delete karo",
        "image ko zabardasti remove karo",
        "force se docker image hata do",
        # --- NEW HINGLISH COMMANDS ---
        "jabardasti delete maar do",
    ],

    "docker.image.inspect": [
        "inspect a docker image",
        "show docker image details",
        "image ki details dikhao",
        "docker image inspect karo",
        "image ka configuration batao",
        "docker image ki information dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "image ka pura inspection dikhao",
    ],

    "docker.image.history": [
        "show docker image history",
        "show image layers",
        "docker image ki history dikhao",
        "image ke layers batao",
        "docker image ka build history dikhao",
        "image ka history check karo",
        # --- NEW HINGLISH COMMANDS ---
        "image kaise bani thi dikha do",
    ],

    "docker.image.tag": [
        "tag a docker image",
        "create a tag for an image",
        "docker image ko tag karo",
        "image ka naya tag banao",
        "docker image ka naam aur tag change karo",
        "image ko registry tag do",
        # --- NEW HINGLISH COMMANDS ---
        "is image ko tag maar do",
    ],

    "docker.image.save": [
        "save a docker image to a file",
        "export docker image as a tar file",
        "docker image ko file mein save karo",
        "image ko tar file mein convert karo",
        "docker image export karo",
        "image ka backup file banao",
        # --- NEW HINGLISH COMMANDS ---
        "image export karke save kardo",
    ],

    "docker.image.load": [
        "load a docker image from a file",
        "import docker image from tar",
        "tar file se docker image load karo",
        "docker image ko file se import karo",
        "saved docker image load karo",
        "file wali image docker mein lao",
        # --- NEW HINGLISH COMMANDS ---
        "file se image andar le lo",
    ],

    "docker.image.prune": [
        "remove unused docker images",
        "clean unused images",
        "unused docker images hata do",
        "docker ki unused images clean karo",
        "dangling images remove karo",
        "docker images cleanup karo",
        # --- NEW HINGLISH COMMANDS ---
        "faltu image delete maar do",
    ],

    "docker.image.prune.all": [
        "remove all unused docker images",
        "clean all unused images",
        "docker ki saari unused images hata do",
        "all unused docker images delete karo",
        "docker images ko completely clean karo",
        # --- NEW HINGLISH COMMANDS ---
        "sari bina use wali image ko saaf kardo",
    ],


    # ============================================================
    # BUILD
    # ============================================================

    "docker.build": [
        "build a docker image",
        "build docker image",
        "docker image build karo",
        "Dockerfile se image banao",
        "docker image create karo",
        "project ki docker image build karo",
        # --- NEW HINGLISH COMMANDS ---
        "docker image tayar karo",
    ],

    "docker.build.tagged": [
        "build docker image with a tag",
        "build and tag a docker image",
        "docker image ko tag ke saath build karo",
        "image build karo aur naam do",
        "docker image build karke tag karo",
        "Dockerfile se tagged image banao",
        # --- NEW HINGLISH COMMANDS ---
        "tag lagake build karo",
    ],

    "docker.build.no_cache": [
        "build docker image without cache",
        "rebuild docker image without cache",
        "docker image bina cache ke build karo",
        "cache use mat karo aur image build karo",
        "fresh docker build karo",
        "docker image clean build karo",
        # --- NEW HINGLISH COMMANDS ---
        "scratch se build maar do cache hata ke",
    ],

    "docker.build.pull": [
        "build docker image and pull latest base image",
        "build using the latest base image",
        "docker build ke time base image pull karo",
        "latest base image ke saath build karo",
        "docker image build karte waqt image update karo",
        # --- NEW HINGLISH COMMANDS ---
        "latest base image la kar build karo",
    ],


    # ============================================================
    # NETWORKS
    # ============================================================

    "docker.network.list": [
        "show docker networks",
        "list docker networks",
        "docker networks dikhao",
        "mere docker networks kaunse hain",
        "all docker networks batao",
        "docker ke networks list karo",
        # --- NEW HINGLISH COMMANDS ---
        "network ka connection dikhao",
    ],

    "docker.network.create": [
        "create a docker network",
        "make a new docker network",
        "docker network banao",
        "naya docker network create karo",
        "container ke liye network banao",
        "custom docker network create karo",
        # --- NEW HINGLISH COMMANDS ---
        "naya docker network banado",
    ],

    "docker.network.remove": [
        "remove a docker network",
        "delete docker network",
        "docker network delete karo",
        "network ko hata do",
        "docker network remove karo",
        "custom network delete kar do",
        # --- NEW HINGLISH COMMANDS ---
        "docker network ko uda do",
    ],

    "docker.network.inspect": [
        "inspect a docker network",
        "show docker network details",
        "docker network ki details dikhao",
        "network inspect karo",
        "docker network mein kaunse containers hain",
        "network configuration batao",
        # --- NEW HINGLISH COMMANDS ---
        "network ke bare me jankari do",
    ],

    "docker.network.connect": [
        "connect a container to a network",
        "attach container to docker network",
        "container ko network se connect karo",
        "docker container ko network mein add karo",
        "container ko is network se jodo",
        "network ke saath container connect karo",
        # --- NEW HINGLISH COMMANDS ---
        "container ko network de do",
    ],

    "docker.network.disconnect": [
        "disconnect a container from a network",
        "remove container from network",
        "container ko docker network se disconnect karo",
        "container ko network se hata do",
        "network se container disconnect karo",
        "container ko network se remove karo",
        # --- NEW HINGLISH COMMANDS ---
        "container ko network se hata lo",
    ],

    "docker.network.disconnect.force": [
        "force disconnect container from network",
        "force remove container from docker network",
        "container ko forcefully network se hatao",
        "network se container ko zabardasti disconnect karo",
        # --- NEW HINGLISH COMMANDS ---
        "network zabardasti disconnect maar do",
    ],

    "docker.network.prune": [
        "remove unused docker networks",
        "clean unused docker networks",
        "unused networks hata do",
        "docker networks cleanup karo",
        "unused docker network remove karo",
        "docker ke unused networks clean karo",
        # --- NEW HINGLISH COMMANDS ---
        "bekar network ko saaf karo",
    ],


    # ============================================================
    # VOLUMES
    # ============================================================

    "docker.volume.list": [
        "show docker volumes",
        "list docker volumes",
        "docker volumes dikhao",
        "mere docker volumes kaunse hain",
        "all docker volumes batao",
        "docker ke volumes list karo",
        # --- NEW HINGLISH COMMANDS ---
        "mere volumes dikha do",
    ],

    "docker.volume.create": [
        "create a docker volume",
        "make a new docker volume",
        "docker volume banao",
        "naya volume create karo",
        "persistent storage ke liye volume banao",
        "docker volume create kar do",
        # --- NEW HINGLISH COMMANDS ---
        "ek volume aur bana do",
    ],

    "docker.volume.inspect": [
        "inspect a docker volume",
        "show volume details",
        "docker volume ki details dikhao",
        "volume inspect karo",
        "docker volume ki information batao",
        "volume ka configuration dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "volume details show karo",
    ],

    "docker.volume.remove": [
        "remove a docker volume",
        "delete docker volume",
        "docker volume delete karo",
        "volume hata do",
        "docker volume remove karo",
        "volume ko delete kar do",
        # --- NEW HINGLISH COMMANDS ---
        "ye volume uda de bhai",
    ],

    "docker.volume.prune": [
        "remove unused docker volumes",
        "clean unused volumes",
        "unused docker volumes hata do",
        "docker volumes cleanup karo",
        "unused volumes delete karo",
        "docker ke unused volumes clean karo",
        # --- NEW HINGLISH COMMANDS ---
        "faltu volume uda do",
    ],


    # ============================================================
    # DOCKER COMPOSE
    # ============================================================

    "docker.compose.up": [
        "start docker compose",
        "run docker compose",
        "docker compose start karo",
        "compose application chalao",
        "docker compose services start karo",
        "compose project run karo",
        # --- NEW HINGLISH COMMANDS ---
        "compose file se sab up kardo",
        "docker compose chalu kar do",
        "saari services start maar do",
        "compose environment up karo",
    ],

    "docker.compose.up.detached": [
        "start docker compose in background",
        "run compose in detached mode",
        "docker compose background mein chalao",
        "compose ko detached mode mein start karo",
        "docker compose ko background mein run karo",
        "compose services background mein start karo",
        # --- NEW HINGLISH COMMANDS ---
        "background me compose chala do",
    ],

    "docker.compose.down": [
        "stop docker compose",
        "bring docker compose down",
        "docker compose band karo",
        "compose services stop karo",
        "compose project ko shutdown karo",
        "docker compose down karo",
        # --- NEW HINGLISH COMMANDS ---
        "compose gira do",
        "compose pura down maar do",
    ],

    "docker.compose.down.volumes": [
        "stop compose and remove volumes",
        "bring compose down and delete volumes",
        "docker compose ke saath volumes bhi hatao",
        "compose down karo aur volumes delete karo",
        "compose aur uske volumes remove karo",
        # --- NEW HINGLISH COMMANDS ---
        "compose aur volumes dono gira do",
    ],

    "docker.compose.start": [
        "start docker compose services",
        "start compose services",
        "docker compose services start karo",
        "compose services ko chalao",
        "stopped compose services start karo",
        # --- NEW HINGLISH COMMANDS ---
        "compose start kar de bhai",
    ],

    "docker.compose.stop": [
        "stop docker compose services",
        "stop compose services",
        "docker compose services band karo",
        "compose services rok do",
        "docker compose ko stop karo",
        # --- NEW HINGLISH COMMANDS ---
        "compose rukwa do abhi",
    ],

    "docker.compose.restart": [
        "restart docker compose services",
        "restart compose",
        "docker compose restart karo",
        "compose services ko restart karo",
        "docker compose dobara chalao",
        # --- NEW HINGLISH COMMANDS ---
        "compose firse restart maar do",
    ],

    "docker.compose.ps": [
        "show docker compose containers",
        "list compose services",
        "docker compose containers dikhao",
        "compose mein kaunse containers chal rahe hain",
        "docker compose ke status dikhao",
        "compose services ki list batao",
        # --- NEW HINGLISH COMMANDS ---
        "compose wale containers dikha do",
    ],

    "docker.compose.logs": [
        "show docker compose logs",
        "show compose logs",
        "docker compose ke logs dikhao",
        "compose services ke logs batao",
        "docker compose logs check karo",
        # --- NEW HINGLISH COMMANDS ---
        "compose project ki logs print karo",
    ],

    "docker.compose.logs.follow": [
        "follow docker compose logs",
        "show live compose logs",
        "docker compose ke live logs dikhao",
        "compose logs continuously dekho",
        "compose ke logs follow karo",
        "real time compose logs dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "compose ki logs aate rehne do",
    ],

    "docker.compose.pull": [
        "pull docker compose images",
        "download compose images",
        "docker compose images pull karo",
        "compose ki latest images download karo",
        "compose images update karo",
        # --- NEW HINGLISH COMMANDS ---
        "compose ke image server se le aao",
    ],

    "docker.compose.build": [
        "build docker compose services",
        "build compose images",
        "docker compose images build karo",
        "compose project build karo",
        "docker compose build chalao",
        # --- NEW HINGLISH COMMANDS ---
        "compose firse build kardo",
    ],

    "docker.compose.build.no_cache": [
        "build compose without cache",
        "rebuild compose images without cache",
        "docker compose bina cache ke build karo",
        "compose ko fresh build karo",
        "compose images clean build karo",
        # --- NEW HINGLISH COMMANDS ---
        "cache uda kar compose build maar do",
    ],

    "docker.compose.exec": [
        "execute a command in a compose service",
        "run command inside compose service",
        "compose service ke andar command chalao",
        "docker compose service mein command execute karo",
        "compose container ke andar command run karo",
        # --- NEW HINGLISH COMMANDS ---
        "compose ke andar ye wali command dal do",
    ],

    "docker.compose.run": [
        "run a command in a compose service",
        "run a one time compose service",
        "compose service ke liye command run karo",
        "docker compose service ko command ke saath run karo",
        "compose mein temporary command chalao",
        # --- NEW HINGLISH COMMANDS ---
        "ek bar run karke dekho compose me",
    ],


    # ============================================================
    # SYSTEM / INFORMATION
    # ============================================================

    "docker.version": [
        "show docker version",
        "what docker version am I using",
        "docker ka version batao",
        "docker version dikhao",
        "mere system mein docker kaunsa version hai",
        "check docker version",
        # --- NEW HINGLISH COMMANDS ---
        "docker kitna purana hai dikhao",
    ],

    "docker.info": [
        "show docker information",
        "show docker system information",
        "docker ki system information dikhao",
        "docker daemon ki details batao",
        "docker info check karo",
        "docker system ke baare mein batao",
        # --- NEW HINGLISH COMMANDS ---
        "docker ke overall detail de do",
    ],

    "docker.disk.usage": [
        "show docker disk usage",
        "how much disk is docker using",
        "docker kitni storage use kar raha hai",
        "docker ka disk usage batao",
        "docker storage usage dikhao",
        "docker ne kitni space li hai",
        # --- NEW HINGLISH COMMANDS ---
        "docker space check karo",
    ],

    "docker.disk.usage.verbose": [
        "show detailed docker disk usage",
        "show detailed docker storage usage",
        "docker ki detailed storage information dikhao",
        "docker disk usage detail mein batao",
        "images containers volumes ki storage usage dikhao",
        # --- NEW HINGLISH COMMANDS ---
        "puri memory ki detailed information do",
    ],


    # ============================================================
    # CLEANUP
    # ============================================================

    "docker.system.prune": [
        "clean unused docker resources",
        "remove unused docker resources",
        "docker cleanup karo",
        "unused containers networks images clean karo",
        "docker ki unused cheezein hata do",
        "docker system cleanup karo",
        # --- NEW HINGLISH COMMANDS ---
        "docker kachra uda de bhai",
    ],

    "docker.system.prune.all": [
        "remove all unused docker resources",
        "clean all unused docker resources",
        "docker ki saari unused resources hata do",
        "all unused docker images containers networks delete karo",
        "docker ko completely clean karo",
        # --- NEW HINGLISH COMMANDS ---
        "jo use nahi ho raha sab mita do",
    ],

    "docker.system.prune.volumes": [
        "clean docker resources including volumes",
        "remove unused docker resources and volumes",
        "docker cleanup with volumes karo",
        "unused volumes bhi delete karo",
        "docker ki unused resources aur volumes hata do",
        # --- NEW HINGLISH COMMANDS ---
        "volume bhi sath me uda do",
    ],

    "docker.container.prune": [
        "remove all stopped containers",
        "clean stopped docker containers",
        "stopped containers hata do",
        "docker ke stopped containers delete karo",
        "unused containers remove karo",
        "saare stopped containers clean karo",
        # --- NEW HINGLISH COMMANDS ---
        "band hue containers clear maar do",
    ],


    # ============================================================
    # REGISTRY / LOGIN
    # ============================================================

    "docker.login": [
        "login to docker",
        "docker login karo",
        "docker registry mein login karo",
        "docker hub login karo",
        "docker mein authenticate karo",
        "docker account se login karo",
        # --- NEW HINGLISH COMMANDS ---
        "hub me login karwa do",
    ],

    "docker.login.registry": [
        "login to a docker registry",
        "login to this docker registry",
        "docker registry mein login karo",
        "private registry mein login karo",
        "custom docker registry login karo",
        "registry ke saath authenticate karo",
        # --- NEW HINGLISH COMMANDS ---
        "private hub pe connect kardo",
    ],

    "docker.logout": [
        "logout from docker",
        "docker logout karo",
        "docker se logout karo",
        "docker account se sign out karo",
        "docker authentication remove karo",
        # --- NEW HINGLISH COMMANDS ---
        "logout maar do abhi",
    ],

    "docker.logout.registry": [
        "logout from docker registry",
        "logout from this registry",
        "docker registry se logout karo",
        "private registry se sign out karo",
        "registry authentication remove karo",
        # --- NEW HINGLISH COMMANDS ---
        "registry se disconnect kardo",
    ],


    # ============================================================
    # COMMIT
    # ============================================================

    "docker.container.commit": [
        "create an image from a container",
        "save container as a docker image",
        "container ko image mein convert karo",
        "docker container se image banao",
        "container ka image create karo",
        "running container ko image ke roop mein save karo",
        # --- NEW HINGLISH COMMANDS ---
        "is container ka ek clone image bana lo",
    ],


    # ============================================================
    # EXPORT / IMPORT
    # ============================================================

    "docker.container.export": [
        "export a docker container",
        "save container filesystem to a file",
        "docker container ko file mein export karo",
        "container ka backup lo",
        "container ko tar file mein export karo",
        "container filesystem save karo",
        # --- NEW HINGLISH COMMANDS ---
        "container utha kar export maar do",
    ],

    "docker.container.import": [
        "import a docker container from a file",
        "create image from exported container",
        "docker container file import karo",
        "tar file se docker image banao",
        "exported container ko import karo",
        "container archive se image create karo",
        # --- NEW HINGLISH COMMANDS ---
        "tar file wapas se import kar lo",
    ],

    "windows.touch": [
        "create a file",
        "create a new file",
        "make a file",
        "make ",
        "touch",
        "new file banao",
        "file banao",
        "ek file banao",
        "nayi file banao",
        "new text file banao",
        "text file create karo",
    ],

    "windows.cd.desktop": [
        "go to desktop",
        "open desktop",
        "desktop pe jao",
        "desktop par jao",
        "desktop me jao",
        "desktop folder me jao",
        "desktop kholo",
        "desktop open karo",
        "mujhe desktop par le jao",
        "desktop pe le chalo",
        "desktop directory me jao",
        "desktop dikhao",
    ],

    "windows.cd.documents": [
        "go to documents",
        "open documents",
        "documents pe jao",
        "documents par jao",
        "documents me jao",
        "documents folder me jao",
        "documents kholo",
        "documents open karo",
        "mujhe documents me le jao",
        "documents directory me jao",
    ],

    "windows.cd.downloads": [
        "go to downloads",
        "open downloads",
        "downloads pe jao",
        "downloads par jao",
        "downloads me jao",
        "downloads folder me jao",
        "downloads kholo",
        "downloads open karo",
        "mujhe downloads me le jao",
        "downloads directory me jao",
    ],

    "windows.cd.home": [
        "go to home directory",
        "go to user folder",
        "open home directory",
        "home folder me jao",
        "user folder me jao",
        "home directory kholo",
        "main folder me jao",
        "user directory me jao",
        "ghar wale folder me jao",
    ],

    "windows.cd.parent": [
        "go to parent directory",
        "go back one folder",
        "go back",
        "parent folder me jao",
        "ek folder peeche jao",
        "ek directory peeche jao",
        "pichle folder me jao",
        "upar wale folder me jao",
        "parent directory kholo",
    ],

    "windows.pwd": [
        "show current directory",
        "where am I",
        "what directory am I in",
        "show current path",
        "show working directory",
        "current path dikhao",
        "kaha hu",
        "main kaha hoon",
        "abhi kis folder me hoon",
        "abhi kis directory me hoon",
        "current folder batao",
        "current directory batao",
        "mera current path kya hai",
    ],

    "windows.dir": [
        "list files",
        "show files",
        "list directory",
        "show directory contents",
        "show folder contents",
        "files dikhao",
        "folder ke files dikhao",
        "directory ke andar kya hai",
        "is folder me kya hai",
        "saare files dikhao",
        "current directory list karo",
        "folder dikhao",
        "folder me kya kya pada hai",
        "andar ka maal dikhao",
        "dir karo",
    ],

    "windows.dir.hidden": [
        "show hidden files",
        "list hidden files",
        "show all files",
        "show hidden files and folders",
        "hidden files dikhao",
        "chhupe hue files dikhao",
        "hidden files bhi dikhao",
        "all files show karo",
        "hidden files list karo",
        "hidden folders dikhao",
        "hidden files check karo",
    ],

    "windows.mkdir": [
        "create a folder",
        "make a folder",
        "create directory",
        "make directory",
        "new folder banao",
        "folder banao",
        "ek folder banao",
        "naya folder banao",
        "directory banao",
        "folder create karo",
        "new directory banao",
    ],

    "windows.delete.file": [
        "delete a file",
        "remove a file",
        "delete file",
        "remove file",
        "file delete karo",
        "file hatao",
        "file remove karo",
        "is file ko delete karo",
        "ye file hata do",
    ],

    "windows.delete.folder": [
        "delete a folder",
        "remove a folder",
        "delete directory",
        "remove directory",
        "folder delete karo",
        "folder hatao",
        "folder remove karo",
        "is folder ko delete karo",
        "ye folder hata do",
    ],

    "windows.copy": [
        "copy a file",
        "copy file",
        "copy this file",
        "file copy karo",
        "is file ko copy karo",
        "file ki copy banao",
        "copy bana do",
        "file ko copy karo",
    ],

    "windows.move": [
        "move a file",
        "move file",
        "move this file",
        "file move karo",
        "is file ko move karo",
        "file ko dusre folder me le jao",
        "file ko shift karo",
        "file shift kar do",
    ],

    "windows.rename": [
        "rename a file",
        "rename file",
        "rename this file",
        "file rename karo",
        "is file ka naam badlo",
        "file ka naam change karo",
        "naam badal do",
        "file ko rename karo",
    ],

    "windows.clear": [
        "clear terminal",
        "clear screen",
        "clean terminal",
        "clear the screen",
        "terminal clear karo",
        "screen clear karo",
        "terminal saaf karo",
        "screen saaf karo",
        "sab hata do screen se",
    ],

    "windows.echo": [
        "print text",
        "display text",
        "show text",
        "print something",
        "text print karo",
        "text dikhao",
        "ye text print karo",
        "message print karo",
    ],

    "windows.type": [
        "show file contents",
        "read file",
        "read this file",
        "display file contents",
        "file ka content dikhao",
        "file ke andar kya hai",
        "file padho",
        "file ka data dikhao",
        "is file ko read karo",
    ],
}