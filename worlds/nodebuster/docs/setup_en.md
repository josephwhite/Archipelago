# Nodebuster for Archipelago Setup Guide

## Required Software
* A legal copy of Nodebuster.
    * Steam.
    * Windows.
* Download the Godot Mod Loader from this [Github](https://github.com/GodotModding/godot-mod-loader/pull/533)
    * We use this version due to the main branch not working with Nodebuster.
* Download the [Archipelago Mod](https://github.com/Emerald836/Emerlads-Nodebuster_AP_Mod/releases)

## Recommended Software
* QOL Mods.
    * I would highly recommend using a QOL mod just to make your life easier. As this while normally not long. Does have over 500 checks on the standard settings. And with progression being so broken up due to randomization it can easily make the game a lot longer.
    * If you can not find a mod for Nodebuster you can find one [Here](https://github.com/Emerald836/Emerlad-Nodebuster-QOL-Mod/releases)

## Setting up Mod Loader and Installing the Archipelago Mod
1. After downloading the Mod Loader from [Here](https://github.com/GodotModding/godot-mod-loader/pull/533). Extract the addons folder from the zip and put it in your Nodebuster files right next to the Executable.
 * This can be found by right clicking on your Nodebuster game in steam and clicking browse local files.
2. Go back to steam and go to the properties window by right clicking your Nodebuster game and clicking properties.
3. After the window opens find launch options and put "--script addons/mod_loader/mod_loader_setup.gd"(remove quotes) in the launch options field. Then open Nodebuster once.
3. After you opened the game go back to the properties window and remove what we put in the launch options field.
4. Go back to the Nodebuster local files. and create a folder named "mods".
5. Insert the ZIP file of the archipelago mod found [here](https://github.com/Emerald836/Emerlads-Nodebuster_AP_Mod/releases) into the mods folder.
 * Do not unzip the mod file as the mod loader requires for it to be zipped.
6. Open up Nodebuster once more and the game should ask you to restart the game. Click yes. After restarting the game the mod will be installed.

### What to do if the Mod Loader doesn't install correctly
* This can happen due to either the wrong version of the Mod loader was installed or the launch options field wasn't filled correctly.

1. Check the launch options field in the properties window of the game. If you still have what we put back in step 3 of setup. Remove it and try starting the game again.

2. Make sure you downloaded the Mod Loader from [Here](https://github.com/GodotModding/godot-mod-loader/pull/533). This is the version that I was able to get working. any other version I was unable to get working.
 * More information on the Godot Mod Loader can be found on the [Wiki](https://wiki.godotmodding.com)


## Configuring your YAML File
### What is a YAML and why do I need one?
An YAML file is the way that you provide your player options to Archipelago.
See the [basic multiworld setup guide](/tutorial/Archipelago/setup/en) here on the Archipelago website to learn more.

### Where do I get a YAML?
You can either download it from the [mod release page](https://github.com/Emerald836/Emerlads-Nodebuster_AP_Mod/releases). Or you can generate a template with the Archipelago Launcher after installing the APWorld.

### Joining an Archipelago Game in Nodebuster
1. Start the game after installing all necessary mods.
2. In the main menu you should see a Connect button instead of a new game, and cotinue game button.
3. Click said Connect button.
4. Input the correct information in the correct fields. (ie. "archipelago:12993" in the address slot.).
5. Click Connect and wait a tiny bit.
 * If it takes more then a min to connect then check your input fields to make sure everything is correct.
6. After the game connects to archipelago. It will either take you straight to the upgrade tree scene. Or if you have a save file that was already connected to the server address you are using. It will instead ask if you want to use the aforementioned save file or no.
7. Enjoy!


## Hints and other commands
While playing in a multiworld, you can interact with the server using various commands listed in the 
[commands guide](/tutorial/Archipelago/commands/en). You can use the Archipelago Text Client to do this,
which is included in the latest release of the [Archipelago software](https://github.com/ArchipelagoMW/Archipelago/releases/latest).