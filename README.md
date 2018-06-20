# Picky-Bucket 



This is a Django clone of the popular app Instagram (lol)

The app uses the ```django``` framework to create a set of backend databases that are then templated in the main application.

As a user you can also search by **category type**, **tags** or **title**.





## Building the app

It is best to use the python `virtualenv` tool to build locally:

```
$ virtualenv venv --python-3.6.2
$ source venv/bin/activate
$ pip install -r requirements.txt
$ DEVELOPMENT=1 python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. 



## requirements.txt


**Once you have run the ```pip installation```, verify that you have all the necessary requirements with the following command:**


 ```
 pip3 freeze
 ```

 We use pip **3** as it mentions the appropriate python version.

![alt text](./media/boom.png "Logo Title Text 1")

The app should now run smoothly on your local server.......

__If it doesn't work or you are experiencing errors__, please report to: 

<plucaslambert@gmail.com>



## Functionality breakdown

__Let's get down and dirty & see how this app code works:__

1. Components:

Our app contains standard django templating conponenets that handle __functionalities__, __routing__, __views__ and __templating__.

```Functionalites``` are handled by our __MODELS__ file, that defines __objects__ and their respective functions.

EXAMPLE:

```models.py```

```python
class Image(models.Model):
    title = models.CharField(max_length = 60)
    description = models.TextField()
    editor = models.ForeignKey(Editor)
    category = models.ManyToManyField(Category, related_name='category')
    tag = models.ManyToManyField(Tag, related_name='tag')
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'view_images/')
    location = models.ManyToManyField(Location, related_name='location')
    

    @classmethod
    def search_by_title(cls,search_term):
        title_search = cls.objects.filter(title__icontains = search_term)
        return title_search
```
We notice the **classmethod** search_by_title. This method defines a function that can be taken in by our **view.py** file.
In the example above the method allows us to perform a search __by title__.
The __icontains filter will **compare** the value of our search-term and the value of the title. 
**regex** searching allows us to search by even a few letters instead of the entire word.

In our **views.py** file we handle what happens with this classmethod:

```views.py```


```python
def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article") 
        searched_images = Image.search_by_title(search_term) or Tag.search_by_tag(search_term) or Category.search_by_cat(search_term)
        message = f"{search_term}"
        date = dt.date.today()

        return render(request, 'all_images/search.html', {"message":message, "images": searched_images, "date":date})
    else:
        message = "You havne't searched for any term"
        date = dt.date.today()
        return render(request, 'all_images/search.html',{"message":message, "date":date})
```
First we define the GET request by saying:
- First we make sure the object "article" really exists in our request.
- The search terms is the gotten from the requested object by passing the __key__ "article"



Django allows us to connect this model to a postgresql db:


```settings.py```

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'zoominphotos',
        'USER': '***...***',
        'PASSWORD': '***...***',
    }
}
```

The __engine__ key defines what kind of database you want to use.



## Get involved!

We are happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[github issue tracker](https://github.com/lucasLB7/Zoomin-Photos-/issues).

Master [git repository](https://github.com/lucasLB7/Zoomin-Photos-):


## Licensing

This library is MIT-licensed.


```The MIT License

Copyright (c) 2010-2018 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.```
