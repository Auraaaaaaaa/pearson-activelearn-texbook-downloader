### Pearson activelearn downloader
FAQ:
##### what is this?
it downloads a textbook from Pearson's activelearn website as a series of images and (optionally) turns it into a pdf
##### does it work?
yes, as of 29/09/24

##### how do i use it
i'm lazy, so you'll have to change the amount of pages in the book to yours that you want to download, an example is in the script and change the images url (you can find by opening the network tab in firefox's developer tools and flicking through the pages, the images are simply downloaded as jpgs lmfao)
alter the downloader.py to suit your needs, wait, then if you want a pdf run makepdf.py 

##### will you ever update this again
probably not, i only needed it for one thing

### requirements:
python 3
pillow
requests
internet connection

### why does this work?
some work experience kid at pearson wrote the activelearn system and didn't include proper drm, and made it in the most lazy way possible. took a random 16 year old 5 minutes to download a politics textbook 
fix ur shit pearson
