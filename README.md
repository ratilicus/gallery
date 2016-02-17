# Gallery

### About

A simple program for uploading and manipulating images

### Features

- drag and drop image upload (html5)
- front-end image scaling/thumbing/cropping (using fabricjs library)
- ajax image+thumb upload

### Planned Features

- albums/categories (groups of images)
- comments
- public+private albums
- admins/editors/viewers user classes
- user administration
- album+image/thumb administration

### Stack

- tornado
- mongodb
- nginx

### Install

```
# dev env ubuntu 14.04
git clone https://github.com/ratilicus/gallery.git
cd gallery
./setup.ubuntu14.04.sh

# dedicated machine/virtualbox
TBD - probably fabric script
```

### Run

```
# dev env
cd <path-to-gallery-repo>
source ve/bin/activate
./app.py
```

### TODO

- dedicated machine/virtualbox setup (Fabric script?)
- upstart scripts/setup
- planned features
