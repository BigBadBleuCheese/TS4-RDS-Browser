TOC
- [Description](#description)
- [How to Use](#how-to-use)
  - [Have PlumbBuddy 1.5 or later](#have-plumbbuddy-15-or-later)
  - [Enable Runtime Mod Integration in PlumbBuddy](#enable-runtime-mod-integration-in-plumbbuddy)
  - [Download and Install this mod](#download-and-install-this-mod)
  - [Use the Cheat Console](#use-the-cheat-console)

# Description

RDS Browser is a PlumbBuddy UI Bridge mod for The Sims 4 which allows you to create, search, and edit Relational Data Storage instances.

<!-- ![GitHub Release Date](https://img.shields.io/github/release-date/BigBadBleuCheese/TS4-Remote-REPL) -->
![GitHub last commit](https://img.shields.io/github/last-commit/BigBadBleuCheese/TS4-Remote-REPL)
![GitHub top language](https://img.shields.io/github/languages/top/BigBadBleuCheese/TS4-Remote-Repl)
![GitHub contributors](https://img.shields.io/github/contributors/BigBadBleuCheese/TS4-Remote-REPL)
![GitHub Issues](https://img.shields.io/github/issues/BigBadBleuCheese/TS4-Remote-REPL)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/BigBadBleuCheese/TS4-Remote-REPL)

# How to Use

## Have PlumbBuddy 1.5 or later
This hasn't become generally available yet, so... I don't know... sweet talk Amethyst and maybe she'll slip you a file which *she really shouldn't*.
Look, just don't tell me about it.

## Enable Runtime Mod Integration in PlumbBuddy
This should be turned on by default, but in case it isn't...
1. open PlumbBuddy's menu
2. select **Settings**
3. on the **General** tab, switch on **Enable runtime mod integration**

## Download and Install this mod
Probably should go with [the latest release](https://github.com/BigBadBleuCheese/TS4-Remote-REPL/releases) for this, but if you're particularly adventurous, you can download a [GitHub Actions workflow artifact](https://github.com/BigBadBleuCheese/TS4-Remote-REPL/actions) for any commit you want.
Each time a commit make it to the `master` branch in this repo, GitHub will build a complete, production-ready version of the `.ts4script` file for use by the game.

## Use the Cheat Console
The Cheat Console command to get the REPL to appear in PlumbBuddy is:
```
rds_browser.launch
```
PlumbBuddy will grab foreground app focus to ask your permission to launch the browser's UI.
Give consent and you're off to the races.

---

That's about it.