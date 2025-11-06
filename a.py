#!/bin/bash
#=====================================
#    Universal Linux Cache Cleaner
#=====================================
#
#  Made by: Ömer Ali Adalı (Cezzar)
#  GitHub: github.com/cezzar
#  Date: November 2025
#  Version: 2.0
#
#  A powerful cache cleaning script
#  for Linux systems. Safe, fast,
#  and works across all distros!
#
#=====================================

echo -e "\033[36m"
echo "╔════════════════════════════════════════════╗"
echo "║                                            ║"
echo "║    🧹 Universal Linux Cache Cleaner 🧹    ║"
echo "║                                            ║"
echo "║         Made by Ömer Ali Adalı (Cezzar)   ║"
echo "║                                            ║"
echo "╚════════════════════════════════════════════╝"
echo -e "\033[0m"

#calculating the current available storage
Storage=$(df -h "$HOME" | grep "$HOME" | awk '{print($4)}' | tr 'i' 'B')
StorageUsed=$(df -h "$HOME" | grep "$HOME" | awk '{print($3)}' | tr 'i' 'B')
if [ "$Storage" == "0BB" ];
then
    Storage="0B"
fi
echo -e "\033[33m\n========================================\033[0m"
echo -e "\033[33m   DISK SPACE BEFORE CLEANING\033[0m"
echo -e "\033[33m========================================\033[0m"
echo -e "\033[33m   Used: $StorageUsed\033[0m"
echo -e "\033[33m   Available: $Storage\033[0m"
echo -e "\033[33m========================================\033[0m"
echo -e "\033[31m\n🧹 Starting cleanup process...\n\033[0m "
should_log=0
if [[ "$1" == "-p" || "$1" == "--print" ]]; then
    should_log=1
fi
function clean_glob {
    # don't do anything if argument count is zero (unmatched glob).
    if [ -z "$1" ]; then
        return 0
    fi
    if [ $should_log -eq 1 ]; then
        for arg in "$@"; do
            du -sh "$arg" 2>/dev/null
        done
    fi
    /bin/rm -rf "$@" &>/dev/null
    return 0
}
function clean {
    # to avoid printing empty lines
    # or unnecessarily calling /bin/rm
    # we resolve unmatched globs as empty strings.
    shopt -s nullglob
    echo -ne "\033[38;5;208m"
    
    echo "🎵 Cleaning Spotify cache..."
    clean_glob "$HOME"/.var/app/com.spotify.Client/cache/spotify/Data/*
    clean_glob "$HOME"/.var/app/com.spotify.Client/cache/spotify/*/Cache/*
    clean_glob "$HOME"/.var/app/com.spotify.Client/cache/spotify/*/Code\ Cache/*
    clean_glob "$HOME"/.var/app/com.spotify.Client/cache/spotify/*/GPUCache/*
    clean_glob "$HOME"/.var/app/com.spotify.Client/cache/spotify/DeferredBrowserMetrics/*
    clean_glob "$HOME"/.var/app/com.spotify.Client/cache/spotify/GrShaderCache/*
    clean_glob "$HOME"/.var/app/com.spotify.Client/cache/fontconfig/*
    clean_glob "$HOME"/.var/app/com.spotify.Client/cache/mesa_shader_cache*/*
    
    echo "💻 Cleaning VSCode caches..."
    # VSCode Flatpak (all variants)
    clean_glob "$HOME"/.var/app/com.visualstudio.code*/config/Code*/CachedExtensionVSIXs/*
    clean_glob "$HOME"/.var/app/com.visualstudio.code*/config/Code*/Cache/*
    clean_glob "$HOME"/.var/app/com.visualstudio.code*/config/Code*/CachedData/*
    clean_glob "$HOME"/.var/app/com.visualstudio.code*/config/Code*/Code\ Cache/*
    clean_glob "$HOME"/.var/app/com.visualstudio.code*/config/Code*/GPUCache/*
    clean_glob "$HOME"/.var/app/com.visualstudio.code*/config/Code*/logs/*
    clean_glob "$HOME"/.var/app/com.visualstudio.code*/config/Code*/Crashpad/*
    clean_glob "$HOME"/.var/app/com.visualstudio.code*/config/Code*/Service\ Worker/CacheStorage/*
    clean_glob "$HOME"/.var/app/com.visualstudio.code*/cache/*
    
    # VSCode Native (Code, Code - OSS, VSCodium, etc.)
    for code_dir in "$HOME"/.config/Code*; do
        [ -d "$code_dir" ] || continue
        clean_glob "$code_dir"/CachedExtensionVSIXs/*
        clean_glob "$code_dir"/Cache/*
        clean_glob "$code_dir"/CachedData/*
        clean_glob "$code_dir"/Code\ Cache/*
        clean_glob "$code_dir"/GPUCache/*
        clean_glob "$code_dir"/logs/*
        clean_glob "$code_dir"/Crashpad/*
    done
    clean_glob "$HOME"/.vscode*/extensions/.obsolete
    
    # VSCode C++ Tools Cache
    echo "🔧 Cleaning VSCode C++ Tools IntelliSense cache..."
    clean_glob "$HOME"/.cache/vscode-cpptools/ipch/*
    clean_glob "$HOME"/.cache/clangd/index/*
    
    echo "🌐 Cleaning Browser caches..."
    # Google Chrome (all profiles)
    for profile in "$HOME"/.config/google-chrome/*/; do
        [ -d "$profile" ] || continue
        clean_glob "$profile"Cache/*
        clean_glob "$profile"Code\ Cache/*
        clean_glob "$profile"GPUCache/*
        clean_glob "$profile"Service\ Worker/CacheStorage/*
        clean_glob "$profile"Service\ Worker/ScriptCache/*
    done
    clean_glob "$HOME"/.config/google-chrome/component_crx_cache/*
    clean_glob "$HOME"/.config/google-chrome/extensions_crx_cache/*
    clean_glob "$HOME"/.config/google-chrome/*/GrShaderCache/*
    clean_glob "$HOME"/.config/google-chrome/ShaderCache/*
    clean_glob "$HOME"/.config/google-chrome/optimization_guide_model_store/*
    clean_glob "$HOME"/.cache/google-chrome/*/Cache/*
    clean_glob "$HOME"/.cache/google-chrome/*/Code\ Cache/*
    clean_glob "$HOME"/.cache/google-chrome/*/GPUCache/*
    
    # Chromium (all profiles)
    for profile in "$HOME"/.config/chromium/*/; do
        [ -d "$profile" ] || continue
        clean_glob "$profile"Cache/*
        clean_glob "$profile"Code\ Cache/*
        clean_glob "$profile"GPUCache/*
    done
    clean_glob "$HOME"/.cache/chromium/*/Cache/*
    clean_glob "$HOME"/.cache/chromium/*/Code\ Cache/*
    
    # Brave Browser
    for profile in "$HOME"/.config/BraveSoftware/Brave-Browser/*/; do
        [ -d "$profile" ] || continue
        clean_glob "$profile"Cache/*
        clean_glob "$profile"Code\ Cache/*
        clean_glob "$profile"GPUCache/*
    done
    
    # Microsoft Edge
    for profile in "$HOME"/.config/microsoft-edge/*/; do
        [ -d "$profile" ] || continue
        clean_glob "$profile"Cache/*
        clean_glob "$profile"Code\ Cache/*
        clean_glob "$profile"GPUCache/*
    done
    
    # Opera (all profiles)
    for profile in "$HOME"/.config/opera*/*/; do
        [ -d "$profile" ] || continue
        clean_glob "$profile"Cache/*
        clean_glob "$profile"Code\ Cache/*
        clean_glob "$profile"GPUCache/*
    done
    clean_glob "$HOME"/.config/opera*/component_crx_cache/*
    clean_glob "$HOME"/.config/opera*/GrShaderCache/*
    
    # Firefox (all profiles)
    clean_glob "$HOME"/.cache/mozilla/firefox/*/cache2/*
    clean_glob "$HOME"/.cache/mozilla/firefox/*/startupCache/*
    clean_glob "$HOME"/.mozilla/firefox/*/cache2/*
    clean_glob "$HOME"/.var/app/org.mozilla.firefox/cache/*
    
    echo "💬 Cleaning Communication apps caches..."
    # Slack (native and flatpak)
    clean_glob "$HOME"/.config/Slack/Cache/*
    clean_glob "$HOME"/.config/Slack/Code\ Cache/*
    clean_glob "$HOME"/.config/Slack/GPUCache/*
    clean_glob "$HOME"/.var/app/com.slack.Slack/cache/*
    clean_glob "$HOME"/.var/app/com.slack.Slack/config/Slack/Cache/*
    
    # Discord
    clean_glob "$HOME"/.config/discord/Cache/*
    clean_glob "$HOME"/.config/discord/Code\ Cache/*
    clean_glob "$HOME"/.config/discord/GPUCache/*
    clean_glob "$HOME"/.var/app/com.discordapp.Discord/config/discord/Cache/*
    
    # Teams
    clean_glob "$HOME"/.config/Microsoft/Microsoft\ Teams/Cache/*
    clean_glob "$HOME"/.config/Microsoft/Microsoft\ Teams/Code\ Cache/*
    
    # Zoom
    clean_glob "$HOME"/.zoom/data/VDI/*
    clean_glob "$HOME"/.zoom/logs/*
    
    echo "🖥️ Cleaning system caches..."
    # GNOME Software
    clean_glob "$HOME"/.cache/gnome-software/*
    clean_glob "$HOME"/.cache/tracker3/files/*
    clean_glob "$HOME"/.cache/flatpak/system-cache/*
    
    # All Flatpak app caches (generic)
    for app_cache in "$HOME"/.var/app/*/cache; do
        [ -d "$app_cache" ] || continue
        clean_glob "$app_cache"/*
    done
    
    # Clean parent directories (one level up from current location)
    if [ -n "$PWD" ] && [ "$PWD" != "$HOME" ]; then
        clean_glob "$PWD"/../*.o
        clean_glob "$PWD"/../*.a
        clean_glob "$PWD"/../*.so
        clean_glob "$PWD"/../*.tmp
        clean_glob "$PWD"/../*~
        clean_glob "$PWD"/../.*.swp
        clean_glob "$PWD"/../core
    fi
    
    # Clean current directory
    clean_glob "$PWD"/*.o
    clean_glob "$PWD"/*.a
    clean_glob "$PWD"/*.so
    clean_glob "$PWD"/*.tmp
    clean_glob "$PWD"/*~
    clean_glob "$PWD"/.*.swp
    clean_glob "$PWD"/core
    
    echo "🎓 Cleaning 42 specific caches..."
    clean_glob "$HOME"/.var/*.42*
    clean_glob "$HOME"/*.42*
    clean_glob "$HOME"/.zcompdump*
    clean_glob "$HOME"/.cocoapods.42_cache_bak*
    
    echo "🗑️ Cleaning trash..."
    clean_glob "$HOME"/.local/share/Trash/files/*
    clean_glob "$HOME"/.local/share/Trash/info/*
    
    echo "🖼️ Cleaning thumbnails..."
    clean_glob "$HOME"/.cache/thumbnails/*/*
    clean_glob "$HOME"/.thumbnails/*/*
    
    echo "📦 Cleaning development caches..."
    # Python
    clean_glob "$HOME"/.cache/pip/*
    clean_glob "$HOME"/.cache/pypoetry/cache/*
    clean_glob "$HOME"/.cache/pylint/*
    clean_glob "$HOME"/.mypy_cache/*
    
    # Node.js
    clean_glob "$HOME"/.npm/_cacache/*
    clean_glob "$HOME"/.yarn/cache/*
    clean_glob "$HOME"/.cache/node-gyp/*
    clean_glob "$HOME"/.pnpm-store/*
    
    # Rust
    clean_glob "$HOME"/.cargo/registry/cache/*
    
    # Go
    clean_glob "$HOME"/go/pkg/mod/cache/*
    
    # Ruby
    clean_glob "$HOME"/.gem/ruby/*/cache/*
    
    echo "🎨 Cleaning font and graphics caches..."
    clean_glob "$HOME"/.cache/fontconfig/*
    clean_glob "$HOME"/.cache/mesa_shader_cache/*
    clean_glob "$HOME"/.nv/GLCache/*
    clean_glob "$HOME"/.nv/ComputeCache/*
    
    echo "📝 Cleaning old logs..."
    clean_glob "$HOME"/.xsession-errors*
    clean_glob "$HOME"/.local/share/xorg/*.log.old
    clean_glob "$HOME"/.local/state/*/logs/*
    
    echo -ne "\033[0m"
}
clean
if [ $should_log -eq 1 ]; then
    echo
fi
#calculating the new available storage after cleaning
StorageAfter=$(df -h "$HOME" | grep "$HOME" | awk '{print($4)}' | tr 'i' 'B')
StorageUsedAfter=$(df -h "$HOME" | grep "$HOME" | awk '{print($3)}' | tr 'i' 'B')
if [ "$StorageAfter" == "0BB" ];
then
    StorageAfter="0B"
fi
sleep 1
echo -e "\033[32m\n========================================\033[0m"
echo -e "\033[32m   DISK SPACE AFTER CLEANING\033[0m"
echo -e "\033[32m========================================\033[0m"
echo -e "\033[32m   Used: $StorageUsedAfter\033[0m"
echo -e "\033[32m   Available: $StorageAfter\033[0m"
echo -e "\033[32m========================================\033[0m"
echo -e "\033[32m==========BABALAR SÖZÜNÜ TUTAR==========\033[0m"
echo -e "\033[36m\n✨ Cleanup completed successfully!\033[0m\n"
#installer