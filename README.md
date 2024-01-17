# NI Package Manager Feeds

This repository contains NI Package Manager feeds for the plug-ins contained in [MeasurementLink Plug-Ins Org](https://github.com/NI-MeasurementLink-Plug-Ins). 

# Hosted Feeds
| Feed Name                                                  | NI Package Manger Feed URL                                   |
| ---------------------------------------------------------- | ------------------------------------------------------------ |
| [all](/package-feeds/all/) | https://raw.githubusercontent.com/NISystemsEngineering/package-repo/master/rfmx-signal-creator/Packages |

# Using Feeds in NI Package Manager
Once you subscribe to a feed, you will automatically gets updates as new releases are added to the feed.
1. Copy the NI Package Manager Feed URL from the [Hosted Feeds table](#hosted-feeds). This URL is the feed path.
2. [Add the new feed in NIPM](https://www.ni.com/docs/en-US/bundle/package-manager/page/install-packages-from-feed.html). *Recommendation: Name the feed in NI Package Manager with something you will remember such as "GitHub MeasLink". Keep the name short because NI Package Manager does not keep a lot of visible space to display the name later.*

# Installing Packages from the Feed
Once the feed has been added in NIPM, you can install packages from this feed via the **Packages** tab.

1. Ensure that the *Show available packages and feed management tools* checkbox is **checked** in the NIPM settings. If unchecked, the **Packages** tab used below will not be shown.
![](/_img/example_feed_management.png)
2. Select the **Packages** tab on the far right to show all packages that are available from the currently configured feeds, and search for your package from there.

# Developers: Managing the Feeds
After creating a new release, you can add that release to a feed.

## Adding New Packages to Existing Feed
To add a feed to an existing feed:
1. Download the NI Package that you want to add to the feed to your development system.
2. Clone this repository and create a branch.
3. Use the [Package Feed Updater Utility](/package-feed-updater/package-feed-updater/readme.md) to add new package.
4. Create a PR with the new package feed files (Packages, Packages.gz, and Packages.stamps).

## Adding a New Feed
If you want to create a new feed (maybe to have a feed specific for a subset of packages), create a new folder under [/package-feeds](/package-feeds/) and use the [Package Feed Updater Utility](/package-feed-updater/package-feed-updater/readme.md) to create a new feed.

Recommendation is to add all new releases to the ['all' package feed](/package-feeds/all/).

