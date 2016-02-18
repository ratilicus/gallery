```
Gallery Tornado Server View Handlers
by: Adam Dybczak (RaTilicus)

user: [{
    _id: objectid,
    username: str,
    name: str,
    password: str,
    admin: bool
},]

source_image: [{
    _id: objectid,
    uploader: user._id
    editors: [user._id,],
    approval: {user._id: {status: int, reason: str},},  # approval status: 1:approve, 0:abstain, -1:deny
    alt: str, 
    desc: str, 
    width: int, 
    height: int,
    filename: str,
    catalogs: [
        {image_id: objectid, catalog_id: catalog._id, center: [int, int], scale: float, rotation: int},
    ],
    created: datetime,
},]

catalog: {
    _id: objectid,
    title: str,
    description: str,
    editors: [user._id,],
    viewers: [user._id,],
    approval: {user._id: {status: int, reason: str},},  # approval status: 1:approve, 0:abstain, -1:deny
    public: bool
    images: [
        {_id: objectid, source: source_image._id, filename: str, width: int, height: int, 
         cellx: int, celly: int, cellw:int, cellh: int, approved: bool},
    ]
    created: datetime,
}

comment: [{
    _id: objectid,
    catalog: catalog._id,
    image: catalog.images._id
    owner: 


- upload/delete images
- re-arrange images
- scale/crop/rotate images
- catalogs add/modify/remove    (title: str, desc: str, editors: [], viewers: [], images: [])
- comments 

```
