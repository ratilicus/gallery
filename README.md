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

# install docker + docker compose
https://docs.docker.com/compose/install/
```

### Test
```
docker-compose run web python tests.py
```

### Build + Start containers

```
docker-compose up
```


### TODO

- upstart scripts/setup
- planned features
