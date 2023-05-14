# Fluorite Store
Fluorite Store is a user-friendly Windows app store that utilizes the powerful scoop package manager in the backend. Unlike other app stores that download apps from hosts, Fluorite Store downloads apps directly from either official sources, ensuring safety and reliability.

### Why scoop?

Scoop is a trusted Windows package manager that offers several benefits, such as:
* Safe downloads - Since Scoop downloads apps directly from official sources, there is no chance of downloading a fake app. Fluorite Store also has a built-in virustotal checker to further ensure safety.
* Portable apps - Scoop enables versioning, so you can revert to previous app versions after updates, allowing you to fully uninstall apps, and transfer the entire scoop directory (with installed apps) between Windows installs.

## Features 

- [x] Managing installed scoop apps
- [x] Managing installed buckets
- [x] Searching and installing apps
- [x] List of recommended apps and install buttons
- [x] Faster downloads (optionally) using aria2 multithreaded download manager [experimental]
- [x] uses [scoop-search](https://github.com/shilangyu/scoop-search) instead of the default, as its a lot faster
- [x] Modern design and animations
- [x] Virustotal checking apps - **Work in progress**

### Misc Features
- [x] App descriptions
- [ ] Clicking on description box opens a more info page about the app
- [x] Notifications for status

### TODO
- [ ] GUI virustotal instructions if no api key set using the method below
- [ ] When uninstalling an app check if it's currently open, if so either kill it automatically, or warn the user
- [ ] When searching, place indicator beside apps which are already installed

## Checking apps via virustotal - Work in Progress

Fluorite Store features a virustotal check button next to each install button to scan apps for malware. If any malware is detected, it will open the virustotal URL in a browser. To use this feature, users must first create a free virustotal account and obtain an [api key](https://www.virustotal.com/gui/my-apikey).

Note that virustotal limits free users to four checks per minute.

## Possible Features to be added
- [ ] Chocolately integration
- [ ] Scheduled, auto updates
- [ ] Possibly re-writing the search function to instead scrape https://scoop.sh/#/apps?s=0&d=1&o=true as it also contains unofficial repositories (more apps), would be a bit more complex to implement, however it'd include more apps. (if implemented, place warning beside apps that it comes from an unofficial repo)

## Screenshots
https://user-images.githubusercontent.com/83690012/190864219-1a7856e3-d629-4103-9063-aa05eb71d0ea.mp4

![image](https://user-images.githubusercontent.com/83690012/200650749-71f51ff8-d982-4658-b728-68485564c3df.png)

| Searching for apps | Virustotal  | Notif
| ------- | --- | --- |
![image](https://user-images.githubusercontent.com/83690012/200653746-ddc0ec54-52aa-4b3d-9a68-eebe7913e06f.png) | ![image](https://user-images.githubusercontent.com/83690012/200655668-322f63ad-2d83-449a-8187-53283b016f05.png) | ![image](https://user-images.githubusercontent.com/83690012/200654215-ea58d4c6-027f-4a01-866e-5c5d43b78bf4.png)

| Opens browser with virustotal link if detections found  |
| ------- |
![image](https://user-images.githubusercontent.com/83690012/200657087-5449945b-6862-46c7-b2d4-511cb51ff078.png)

**Also the app shown above is just for the purposes of this example, obviously sharex isn't malware, however one of virustotal's sources has the false positive.** 

If an app comes up with several detections, then you should look into it.

![image](https://user-images.githubusercontent.com/83690012/200662758-51f1ec8b-b3e1-4460-823e-752caa10e3c7.png)
![image](https://user-images.githubusercontent.com/83690012/200663513-3a8319ab-e602-424b-8e39-39035c72d637.png)
![image](https://user-images.githubusercontent.com/83690012/200665690-cbe68828-3136-4ee7-8461-3f5185e47ccd.png)
![image](https://user-images.githubusercontent.com/83690012/200650325-03480b17-6c6a-41ff-b935-08882b6b34d1.png)
![image](https://user-images.githubusercontent.com/83690012/200650515-6b064abb-37db-44fd-99d0-4662b726e91e.png)

## Credits

Main Devs:
- [Thomas Kerby (TXOG)](https://github.com/TXOG)
- [Faraz Ahary (t3dium)](https://github.com/t3dium)
