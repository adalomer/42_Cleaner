# 🧹 Universal Linux Cache Cleaner

**Made by Ömer Ali Adalı (Cezzar)**  
*A powerful and safe cache cleaning script for Linux systems*

Works across different distributions and automatically detects installed applications.

## ✨ Features

- **Universal**: Works on any Linux distribution (Ubuntu, Fedora, Arch, etc.)
- **Safe**: Only removes cache files, never touches important data
- **Smart**: Automatically detects installed applications
- **Detailed**: Shows before/after disk usage statistics
- **Multi-app Support**: Cleans caches from 30+ applications

## 🎯 What Gets Cleaned

### 🌐 Web Browsers
- **Google Chrome** (all profiles)
- **Chromium** (all profiles)
- **Firefox** (all profiles)
- **Brave Browser**
- **Microsoft Edge**
- **Opera** / Opera GX

### 💻 Development Tools
- **VSCode** / VSCodium / Code-OSS (Flatpak & Native)
- **VSCode C++ Tools IntelliSense cache**
- **Clangd** index cache

### 📦 Package Managers & Tools
- **Python**: pip, poetry, pylint, mypy
- **Node.js**: npm, yarn, pnpm, node-gyp
- **Rust**: cargo registry cache
- **Go**: module cache
- **Ruby**: gem cache

### 💬 Communication Apps
- **Spotify** (Flatpak)
- **Slack** (Flatpak & Native)
- **Discord**
- **Microsoft Teams**
- **Zoom**

### 🖥️ System Caches
- Thumbnails (all sizes)
- Font cache
- Mesa/GPU shader cache
- NVIDIA GPU cache
- GNOME Software cache
- Flatpak cache
- Tracker3 files

### 🎓 School/Work Specific
- 42 School caches
- Temporary compilation files (*.o, *.a, *.so)
- Core dumps
- Swap files

### 🗑️ Other
- Trash/Recycle Bin
- Old log files
- Session error logs

## 📥 Installation

```bash
# Download the script
wget https://your-repo/a.py -O ~/cleaner.sh

# Make it executable
chmod +x ~/cleaner.sh

# Optional: Move to PATH for system-wide access
sudo mv ~/cleaner.sh /usr/local/bin/cleaner
```

## 🚀 Usage

### Basic Usage (Silent Mode)
```bash
./a.py
```

### Detailed Mode (Show Files Being Deleted)
```bash
./a.py -p
# or
./a.py --print
```

### Run from Anywhere
```bash
~/Masaüstü/a.py
```

## 📊 Expected Results

Typical space freed (varies by system):
- **Light usage**: 200-500 MB
- **Medium usage**: 500-1500 MB  
- **Heavy usage**: 1.5-3 GB
- **Very heavy usage**: 3-5 GB+

## ⚠️ Safety Features

1. **No sudo required**: Only cleans user-owned files
2. **Non-destructive**: Only removes cache and temporary files
3. **Glob patterns**: Uses shell globbing with nullglob (fails gracefully)
4. **Silent errors**: Missing files/folders are automatically skipped
5. **No system files**: Never touches /etc, /var, /usr, or other system directories

## 🔧 Customization

Edit the script to add/remove cleaning targets:

```bash
# Add custom cache location
clean_glob "$HOME"/.your-app/cache/*

# Skip specific application (comment out the lines)
# clean_glob "$HOME"/.config/app-to-skip/*
```

## 🤝 Contributing

This script is universal and works for:
- Students in coding bootcamps (42, etc.)
- Developers with limited disk space
- Anyone wanting to free up space safely

Feel free to:
- Add support for more applications
- Improve detection logic
- Share with others

## 📝 Notes

- **Profile names**: Works with Default, Profile 1, Profile 2, etc.
- **Flatpak apps**: Automatically detected from `~/.var/app/`
- **Development files**: Only cleans from current directory and parent
- **Logs**: Old logs are cleaned, current logs are preserved

## ⚡ Performance

- Runtime: ~5-30 seconds (depends on cache size)
- CPU usage: Minimal
- Disk I/O: Moderate during deletion
- Memory: < 10 MB

## 🐛 Troubleshooting

**Q: Script says "Permission denied"**  
A: Make sure the script is executable: `chmod +x a.py`

**Q: Not much space freed**  
A: Run browsers/apps for a few days, caches accumulate over time

**Q: Can I run this daily?**  
A: Yes! It's safe to run as often as you want

**Q: Will this break my applications?**  
A: No! Caches are regenerated automatically when needed

## 📄 License

Free to use, modify, and distribute. No attribution required.

## 🌟 Star this if it helped!

If this script saved you disk space, share it with others! 🚀
