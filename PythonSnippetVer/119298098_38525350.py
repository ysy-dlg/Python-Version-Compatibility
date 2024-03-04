procId = subprocess.Popen('adb shell', stdin = subprocess.PIPE)
procId.communicate('command1\ncommand2\nexit\n')