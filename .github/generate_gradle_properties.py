#!/usr/bin/env python3
import subprocess

# Run git ls-remote command and extract commit ID
cmd = ['git', 'ls-remote', 'https://github.com/PaperMC/Paper']
result = subprocess.run(cmd, capture_output=True, text=True)
commit_id = result.stdout.split('HEAD')[0].strip()

# Define the original gradle.properties content as a dictionary
gradle_props = {
    'group': 'me.endcrystal.linearpaper',
    'version': '1.19.4-R0.1-SNAPSHOT',
    '\nmcVersion': '1.19.4',
    'paperRef': '29b17a892d11697dce9ee35d8eab593bb4748fb1',
    '\norg.gradle.caching': 'true',
    'org.gradle.parallel': 'true',
    'org.gradle.vfs.watch': 'false'
}

# Update the paperRef value with the commit ID
gradle_props['paperRef'] = commit_id

# Write the updated gradle.properties file
for key, value in gradle_props.items():
    print(f'{key}={value}')
