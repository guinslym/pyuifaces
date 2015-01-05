==========
pyuifaces
==========

description
------------
This package uses UIfaces.com ( https://www.uifaces.com/ ) to **fake user picture** on your app. You would like to use real user images for your app. This package might be the right one for you. All the images comes from the 'authorized' section from uifaces and all images are real Twitter users images or avatar, these users previously agreeded to share their profile' picture.

How to install
---------------

    pip install pyuifaces

Example:
--------
FAKING A RANDOM USER IMAGE
```````````````````````````````
		user_image = PyUIFaces()
		user_image_link = user_image.face()
		print(user_image_link)
		=> https://s3.amazonaws.com/uifaces/faces/twitter/anton0kurilov/128.jpg


FAKING A SPECIFIC IMAGE SIZE
`````````````````````````````````

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


FAKING A USER IMAGE BY GENRE
`````````````````````````````````
		foo = PyUIFaces()
		woman = foo.woman()
		man = foo.man()

		for user in range(200):
			print(foo.man())


view the rest of the Documentation on Github