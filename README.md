# pyuifaces
=================

###description
This package uses UIfaces.com ( https://www.uifaces.com/ ) to **fake user picture** on your app. You would like to use real user images for your app. This package might be the right one for you. All the images comes from the 'authorized' section from uifaces and all images are real Twitter users images or avatar, these users previously agreeded to share their profile' picture.

## How to install ##

    pip install pyuifaces

##Example:
####FAKING A RANDOM USER IMAGE
```python
user_image = PyUIFaces()
user_image_link = user_image.face()
print(user_image_link)
=> https://s3.amazonaws.com/uifaces/faces/twitter/anton0kurilov/128.jpg
```

####FAKING A SPECIFIC IMAGE SIZE
```python
user_image = PyUIFaces(False, 'random', 'normal')
user_image_link = user_image.face()
print(user_image_link)
=> https://s3.amazonaws.com/uifaces/faces/twitter/karalek/48.jpg

user2_image = PyUIFaces(False, 'random', 'mini')
user2_image_link = user2_image.face()
print(user2_image_link)
=> https://s3.amazonaws.com/uifaces/faces/twitter/ramdreamers/24.jpg

#avalaible image size
#{'epic': '/128.jpg', 'bigger': '/73.jpg', 
#'mini': '/24.jpg', 'normal': '/48.jpg'}
```

####FAKING A USER IMAGE BY GENRE
```python
foo = PyUIFaces()
woman = foo.woman()
man = foo.man()

for user in range(200):
	print(foo.man())
```

####FAKING A SPECIFIC TWITTER USER IMAGE
```python
#the user must be also in the uifaces.com api
foo = PyUIFaces(True, 'guinslym')
guinslym_link = foo.face()
=> https://s3.amazonaws.com/uifaces/faces/twitter/guinslym/128.jpg
```

[![twitter image of user guinslym](https://s3.amazonaws.com/uifaces/faces/twitter/guinslym/128.jpg)](http://uifaces.com/guinslym)

####API
as simple as this
```python
PyUIFaces(network=False, username='random', image_size="epic")
```
***network*** = For efficiency, by default it will not use the internet to retrieve a user picture it will pick one user from the USERNAME list.
***username*** = By default it will choose a random user. If you want to retrieve a specific user picture than ***network*** should be set to True (i.e. ```PyUIFaces(True, 'the_twitter_username')```). Make sure that the user have subscribed to uifaces.com. To verify this http://uifaces.com/the_twitter_username
***image_size*** = Avalaible image size : 'epic', 'bigger', 'mini', 'normal'. The default one is epic


## Contributing

1. Star it :)
2. Fork it ( https://github.com/guinslym/pyuifaces/fork )
3. Create your feature branch (`git checkout -b my-new-feature`)
4. Test it
5. Commit your changes (`git commit -am 'Add some feature'`)
6. Push to the branch (`git push origin my-new-feature`)
7. Create a new Pull Request
