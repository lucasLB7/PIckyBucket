from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt
# from vote.models import VoteModel

class Profile(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 20, blank = True)
    profile_picture = models.ImageField(upload_to = 'pictures/',null=True)
    
    def __str__(self):
        return self.username
    
    def save_editor(self):
        self.save()

    def delete_editor(self):
        self.delete()

    class Meta:
        ordering = ['first_name']

    @classmethod
    def search_profile(cls, name):
        results = cls.objects.filter(username__icontains = name)
        return results



# class Category(models.Model):

#     categories = (
#         ("TRAVEL", "TRAVEL"),
#         ("LANDSCAPES", "LANDSCAPES"),
#         ("ADVENTURE", "ADVENTURE"),
#         ("CARS", "CARS"),
#         ("SPORTS", "SPORTS"),
#         ("POLITICS", "POLITICS"),
#         ("SELFIE", "SELFIE"),
#         ("LIFE", "LIFE"),
#         ("PEOPLE", "PEOPLE"),
#         ("SCENES", "SCENES"),
#         ("EXTREME", "EXTREME"),
#         ("FIGHT", "FIGHT"),
#         ("MUSIC", "MUSIC"),
#         ("PERSONAL", "PERSONAL"),
#         ("LOVE", "LOVE"),
#         ("MAKEUP", "MAKEUP"),
#         ("CLOTHES", "CLOTHES"),
#         ("WORK", "WORK"),
#         ("RELAX", "RELAX"),
#         ("ENTERTAIN", "ENTERTAIN"),
#         ("SHOCKING", "SHOCKING"),
#         ("RANDOM", "RANDOM"),
        
#     )

#     category_type = models.CharField(max_length = 100, choices=categories, default="RANDOM" )

#     def __str__(self):
#         return self.category_type
#     class Meta:
#         verbose_name_plural = "Category"
    
#     @classmethod
#     def search_by_cat(cls,search_term):
#         cat_search = cls.objects.filter(category_type__icontains = search_term)
#         return cat_search


# class Tag(models.Model):

#     tags = models.CharField(max_length = 30)

#     @classmethod
#     def search_by_tag(cls,search_term):
#         tag_search = cls.objects.filter(tags__icontains = search_term)
#         return tag_search

#     def __str__(self):
#         return self.tags


# class Location(models.Model):
#     continents = (
#         ("AFRICA", "AFRICA"),
#         ("EUROPE", "EUROPE"),
#         ("ASIA", "ASIA"),
#         ("NORTH_AMERICA", "NORTH AMERICA"),
#         ("SOUTH_AMERICA", "SOUTH AMERICA"),
#         ("AUSTRALIA", "AUSTRALIA"),
#         ("ANTARCTICA", "ANTARCTICA"),
#     )
#     continent = models.CharField(max_length = 30, choices=continents, default="AFRICA")
#     country = models.CharField(max_length = 30)
#     location_descrition = models.CharField(max_length = 30)

#     def __str__(self):
#         return self.continent
#     class Meta:
#         verbose_name_plural = "Location"



class Image(models.Model):

    """
    Image class defines image obj
    """

    media_img = models.ImageField(upload_to = 'pictures/',null=True)
    media_title = models.CharField(max_length=30, null=True)
    media_description = models.TextField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    Profile_key = models.ForeignKey(Profile,on_delete=models.CASCADE, null = True)
    User_key = models.ForeignKey(User,on_delete= models.CASCADE , null = True)

    likes = models.PositiveIntegerField(default=0)
    comments_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.media_title

    def save_images(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    def update_caption(self,new_description):
        self.media_description = new_description
        self.save()

    @classmethod
    def media_by_id(cls,id):
        retrived_image = Image.objects.get(id = id)
        return retrived_image

    
    @classmethod
    def search_by_title(cls,search_term):
        title_search = cls.objects.filter(title__icontains = search_term)
        return title_search
    
    @classmethod
    def media_by_user(cls,id):
        posted_images = Image.objects.filter(user_id=id)
        return posted_images
    

    @classmethod
    def view_all_pictures(cls):
        results = cls.objects.all()
        return results
    
    @classmethod
    def pictures_by_date(cls,date):
        results = cls.objects.filter(pub_date__date = date)
        return results

    @classmethod
    def profile_media(cls):
        results = Image.objects.filter()


class Comment(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null= True)
    image_id = models.ForeignKey(Image,on_delete=models.CASCADE, null= True)
    comment= models.TextField(blank=True)
   

    def __str__(self):
        return self.comment

    def save_comment(self):
        """
        method that saves a comment
        """
        self.save()

    def delete_comment(self):
        """
        methods that deletes a comment
        """
        self.delete()


class Like(models.Model):
    """
    Class defines the structure of a like on a posted Image
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE, null= True)
    image = models.ForeignKey(Image,on_delete=models.CASCADE, null = True)

    def __int__(self):
        return self.user.username


    def save_like(self):
        self.save() 

    def unlike(self):
        self.delete()

    def like(self):
        self.likes_number = 2
        self.save()

    @classmethod
    def get_likes(cls,image_id):
        """
        Function that gets likes belonging to a paticular post
        """
        likes = cls.objects.filter(image = image_id)
        return likes 



class Follow(models.Model):
    """
    Class that defines followers of each user
    """

    
    follower = models.ForeignKey(User,on_delete=models.CASCADE, null= True)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE, null= True)
    
    def __int__(self):
        return self.follower.username 
    
    def save_follower(self):
        self.save()

    @classmethod
    def get_followers(cls,profile_id):
        profile = Profile.objects.filter(id = profile_id)
        followers = cls.objects.filter(user= profile.user.id)
        return len(followers)
    



