# Overview
This utility will add a NI Package linked to a URL to a new or existing NI Package Feed. The primary use case is adding NI Packages that are published in GitHub releases to a feed.

# Usage
The easiest way to use the utility is with the compiled exe stored in teh repo releases. Download the exe. The feed path and NI Package for adding to the feed must be local to the system. Invoke the utility from the command line. Here's an example:
```console
.\package_feed_updater.exe --feed-path C:\builds\feed_automation --pkg-local-path C:\Users\SEBUADV\Downloads\jack-audiotest_1.0.0.0_windows_x64.nipkg --pkg-url https://github.com/JacksSandboxOrg/packages/blob/main/jacks-audio-test/jack-audiotest_1.0.0.0_windows_x64.nipkg
```
In this case, the feed package located in C:\builds\feed_automation will be updated.

To get the URL for a release hosted on GitHub, open a browser, go to the release asset and right-click to copy the link.

![](/_img/copy_release_link.png)

# Code
Use Poetry to setup the development environment. If you do not want to use Poetry, check out the dependencies in pyproject.toml.

# Build
To build, use pyinstaller.
```console
pyinstaller .\package_feed_updater.py
```