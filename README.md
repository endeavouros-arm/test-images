# test-images
[![Maintenance](https://img.shields.io/maintenance/yes/2022.svg)]() [![Downloads](https://img.shields.io/github/downloads/endeavouros-arm/images/total)]()

Repository for testing new images for the installation of EndeavourOS on ARM devices <br />
These images contain an EndeavourOS image complete up to including the "Desktop-Base + Common packages". <br />
The only things missing is some personalization and configuration plus a Desktop Environment or Window Manager. <br />
These are provided by a Calamares installer.  

# Installation Instructions

There are two methods to install the test-image

# Method 1

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
#Method 2

In your favorite browser, go to
https://github.com/endeavouros-arm/test-images/releases

look for the latest ddimg-rpi-20230115 or ddimg-odroid-n2-20230115 image
where 2023 is the year, 01 is the month, 15 is the day.

When you find the desired image, click on it.
Under Assets, click on
enosLinuxARM-rpi-latest.img.xz and enosLinuxARM-rpi-latest.img.xz.sha512sum
If you want Odroid N2 image, subsitute odroid-n2 for rpi.

In a terminal window, cd into the  directory the images were downloaded to.
$ sha512sum -c enosLinuxARM-rpi-latest..img.xz.sha512sum
should show image check is OK

Now use your favorite image burning app to transfer the img.xz file
to a micro SD or USB SSD.  gnome-disk-utility is recommended.

# Finish up

Connect the uSD or USB SSD enclosure to a Raspberry Pi 4b/400, Odroid N2/N2+ or Pinebook provided.
Then boot up the device.
Openbox should automatically start up and present the Calamares installer.
Follow the instructions to complete the EndeavourOS install.
