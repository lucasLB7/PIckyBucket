from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt
# from vote.models import VoteModel

class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    nick_name = models.CharField(max_length = 20, blank = True)
    email = models.EmailField()
    current_country = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 10, blank = True)
    editor_photo = models.ImageField(upload_to = 'editors/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True )
    
    def __str__(self):
        return self.first_name
    
    def save_editor(self):
        self.save()

    def delete_editor(self):
        self.delete()

    class Meta:
        ordering = ['first_name']

    @classmethod
    def view_editor_details(cls):
        results = cls.objects.filter()
        return results


class Category(models.Model):

    categories = (
        ("TRAVEL", "TRAVEL"),
        ("LANDSCAPES", "LANDSCAPES"),
        ("ADVENTURE", "ADVENTURE"),
        ("CARS", "CARS"),
        ("SPORTS", "SPORTS"),
        ("POLITICS", "POLITICS"),
        ("SELFIE", "SELFIE"),
        ("LIFE", "LIFE"),
        ("PEOPLE", "PEOPLE"),
        ("SCENES", "SCENES"),
        ("EXTREME", "EXTREME"),
        ("FIGHT", "FIGHT"),
        ("MUSIC", "MUSIC"),
        ("PERSONAL", "PERSONAL"),
        ("LOVE", "LOVE"),
        ("MAKEUP", "MAKEUP"),
        ("CLOTHES", "CLOTHES"),
        ("WORK", "WORK"),
        ("RELAX", "RELAX"),
        ("ENTERTAIN", "ENTERTAIN"),
        ("SHOCKING", "SHOCKING"),
        ("RANDOM", "RANDOM"),
        
    )

    category_type = models.CharField(max_length = 100, choices=categories, default="RANDOM" )

    def __str__(self):
        return self.category_type
    class Meta:
        verbose_name_plural = "Category"
    
    @classmethod
    def search_by_cat(cls,search_term):
        cat_search = cls.objects.filter(category_type__icontains = search_term)
        return cat_search


class Tag(models.Model):

    tags = models.CharField(max_length = 30)

    @classmethod
    def search_by_tag(cls,search_term):
        tag_search = cls.objects.filter(tags__icontains = search_term)
        return tag_search

    def __str__(self):
        return self.tags


class Location(models.Model):
    continents = (
        ("AFRICA", "AFRICA"),
        ("EUROPE", "EUROPE"),
        ("ASIA", "ASIA"),
        ("NORTH_AMERICA", "NORTH AMERICA"),
        ("SOUTH_AMERICA", "SOUTH AMERICA"),
        ("AUSTRALIA", "AUSTRALIA"),
        ("ANTARCTICA", "ANTARCTICA"),
    )
    continent = models.CharField(max_length = 30, choices=continents, default="AFRICA")
    country = models.CharField(max_length = 30)
    location_descrition = models.CharField(max_length = 30)

    def __str__(self):
        return self.continent
    class Meta:
        verbose_name_plural = "Location"

# class Comment(models.Model):
    
#     body = models.CharField(max_length = 60)

#     def __str__(self):
#         return self.body

    # @classmethod
    # def view_all_comments(cls):
    #     results = cls.objects.filter()
    #     return results
    
    # @classmethod
    # def add_comment(self):
    #     self.save()
    
    # def delete_comment(self):
    #     self.delete()




class Image(models.Model):
    title = models.CharField(max_length = 60)
    description = HTMLField()
    # editor = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='category')
    tag = models.ManyToManyField(Tag, related_name='tag')
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'view_images/')
    location = models.ManyToManyField(Location, related_name='location')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)

    
    # comment = models.ManyToManyField(Comment, related_name='comment')
    # comments = models.ForeignKey(Comment)

    # def votes_count(self):
    #     return self.votes.all().count()


    @classmethod
    def search_by_title(cls,search_term):
        title_search = cls.objects.filter(title__icontains = search_term)
        return title_search
    




    # @classmethod
    # def search_by_category(cls, search_term):
    #     result = cls.objects.filter(category__icontains = search_term)
    #     return results
    # @classmethod
    # def search_by_date(cls, search_term):
    #     result = cls.objects.filter(pub_date__date = search_term)
    #     return results


    @classmethod
    def view_all_pictures(cls):
        results = cls.objects.filter()
        return results
    
    @classmethod
    def pictures_by_date(cls,date):
        results = cls.objects.filter(pub_date__date = date)
        return results

    # class Vote(models.Model):
    #     class Meta:
    #         unique_together = [('post', 'user')]

    #     post = models.ForeignKey(Post, related_name='votes')
    #     user = models.ForeignKey('auth.User')


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return self.name



# class ArticleReview(VoteModel, models.Model):
#     review = ArticleReview.objects.get(pk=1)

#     # Up vote to the object
#     review.votes.up(user_id)

#     # Down vote to the object
#     review.votes.down(user_id)

#     # Removes a vote from the object
#     review.votes.delete(user_id)

#     # Check if the user already voted the object
#     review.votes.exists(user_id)

#     # Returns the number of votes for the object
#     review.votes.count()

#     # Returns a list of users who voted and their voting date
#     review.votes.user_ids()


#     # Returns all instances voted by user
#     Review.votes.all(user_id)




# class Follow_user(models.Model):
#     follower



class Profile(models.Model):
    username = models.CharField(max_length=30,default='New_User')
    profile_photo = models.ImageField(upload_to="pics/",null = True)
    bio = models.TextField(default='welcome..',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True )
    
    
    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


    @classmethod
    def find_profile(cls,name):
        found_profiles = cls.objects.filter(username__icontains = name).all()
        return found_profiles
        

class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null= True )
    comment_body = models.CharField(max_length=100)

    @classmethod
    def get_image_comments(cls, id):
        comment = Comment.objects.filter(image__pk=id)
        return comment