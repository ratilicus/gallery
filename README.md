# Gallery

### About

A simple program for uploading and manipulating images

### Features

- drag and drop image upload (html5)
- front-end image scaling/thumbing/cropping (using fabricjs library)
- ajax image+thumb upload
- docker deployment

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
# clone this repo
git clone https://github.com/ratilicus/gallery.git

# install docker
https://docs.docker.com/linux/step_one/
```

### Build containers
```
./build.sh
```

### Start containers

```
./start.sh
```

### Stop containers

```
./stop.sh
```

### TODO

- dedicated machine/virtualbox setup (Fabric script?)
- upstart scripts/setup
- planned features
