# pyuifaces

###description
This package uses UIfaces.com ( https://www.uifaces.com/ ) to **fake user pictures** on your app. You would like to use real user images for your app. This package might be the right one for you. All the images comes from the 'authorized' section from uifaces and all images are real Twitter users images or avatar, these users previously agreeded to share their images.

## How to install ##

    pip install pyuifaces


#Example:
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
```

####FAKING A USER IMAGE BY GENRE
```python
foo = PyUIFaces()
woman = foo.woman()
man = foo.man()
```

####FAKING A SPECIFIC TWITTER USER IMAGE
```python
#the user be also in the uifaces.com api
foo = PyUIFaces(True, 'guinslym')
guinslym_link = foo.face()
```

[![guinslym](https://s3.amazonaws.com/uifaces/faces/twitter/guinslym/128.jpg)](http://uifaces.com/guinslym)


## Contributing

1. Star it :)
2. Fork it ( https://github.com/guinslym/pyuifaces/fork )
3. Create your feature branch (`git checkout -b my-new-feature`)
4. Test it
5. Commit your changes (`git commit -am 'Add some feature'`)
6. Push to the branch (`git push origin my-new-feature`)
7. Create a new Pull Request
