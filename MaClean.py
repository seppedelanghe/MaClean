import os, rumps

ACTIONS = {
    'purge': """osascript -e 'do shell script "sudo purge" with administrator privileges'""",
    'dns': """osascript -e 'do shell script "sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder;" with administrator privileges'""",
    'user_logs': """osascript -e 'do shell script "sudo rm -rf ~/Library/Logs/*" with administrator privileges'""",
    'system_logs': """osascript -e 'do shell script "sudo rm -rf /private/var/log/*" with administrator privileges'""",
    'empty_caches': """osascript -e 'do shell script "sudo rm -rf ~/Library/Caches/*" with administrator privileges'""",
    'brew': "brew cleanup && brew autoremove"
}


class MacleanApp(rumps.App):
    def _exec(self, name: str):
        if name in ACTIONS:
            os.system(ACTIONS[name])

    @rumps.clicked("Purge RAM")
    def purge_ram(self, _):
        rumps.notification("MaClean", "Purging RAM...", "This requires sudo access")
        self._exec('purge')

    @rumps.clicked("Clear DNS")
    def clear_dns(self, _):
        rumps.notification("MaClean", "Clearing DNS records...", "This requires sudo access")
        self._exec('dns')

    @rumps.clicked("Clear user logs")
    def clear_logs(self, _):
        rumps.notification("MaClean", "Clearing user logs...", "This requires sudo access")
        self._exec('user_logs')

    @rumps.clicked("Clear system logs")
    def clear_system_logs(self, _):
        rumps.notification("MaClean", "Clearing system logs...", "This requires sudo access")
        self._exec('system_logs')
    
    @rumps.clicked("Empty Library/Caches")
    def empty_caches(self, _):
        rumps.notification("MaClean", "Emptying Library/Caches...", "This requires sudo access")
        self._exec('empty_caches')

    @rumps.clicked("Brew cleanup")
    def brew_cleanup(self, _):
        rumps.notification("MaClean", "Running brew cleanup and autoremove...", "Hold on...")
        self._exec('brew')


if __name__ == "__main__":
    app = MacleanApp("maclean", icon="icon.png")
    app.run()
