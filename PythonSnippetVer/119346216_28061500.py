print '\n'.join(line.replace(',', '') if not line.startswith('#') else line
                for line in data.splitlines())