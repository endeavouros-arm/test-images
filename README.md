# test-images
[![Maintenance](https://img.shields.io/maintenance/yes/2022.svg)]() [![Downloads](https://img.shields.io/github/downloads/endeavouros-arm/images/total)]()

Repository for testing new images for the installation of EndeavourOS on ARM devices <br />
These images contain an EndeavourOS image complete up to including the "Desktop-Base + Common packages". <br />
The only things missing is some personalization and configuration plus a Desktop Environment or Window Manager. <br />
These are provided by a Calamares installer.  

# Installation Instructions

On an operational Arch Linux (or derivative) computer: <br />
Connect a micro SD card or USB SSD enclosure to the computer's USB port or SD slot. <br />
Launch your favorite Terminal and maximize the window or make it at least 120 x 30
```bash 
# (switch to root - enter root's password)
su      
cd /tmp
```
In your tmp directory, make sure a folder named images does not exist
```bash
git clone https://github.com/endeavouros-arm/test-images.git
cd test-images
```
check permissions, should show image-install-calamares.sh as executable.
```bash
./image-install-calamares.sh
```
Follow the instructions.

Post-Install Method 2
After installation,
```bash
cd ..
# (remove the images directory)
rm -rf images  
# (exit root)
exit           
```
Connect the uSD or USB SSD enclosure to a Raspberry Pi 4b/400, Odroid N2/N2+ or Pinebook provided.
Then boot up the device.
Openbox should automatically start up and present the Calamares installer.
Follow the instructions to complete the EndeavourOS install.
