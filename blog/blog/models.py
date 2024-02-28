from django.db import models

class Category(models.Model):
    # a character field that stores the name of a category for the blog posts.
    name = models.CharField(max_length=30)

    # add correct plural form of the Category class
    class Meta:
        verbose_name_plural = "categories"

    # provide better string representation of objects
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    # short string for the post titile
    title = models.CharField(max_length=255)
    # long-form piece of text
    body = models.TextField()
    # Django DateTimeFields
    # store a datetime object containing the date and time the post 
    #was created and modified
    created_on = models.DateTimeField(auto_now_add=True) # assigns the current date and time
    last_modified = models.DateTimeField(auto_now=True)  # assigns the current date and time
    # relationship between a post and categories
    # link the modles for categories and posts can assign many to many.
    categories = models.ManyToManyField("Category", related_name="posts")
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, blank=True)  # ForeignKey to Author model

    def __str__(self):
        return self.title
    
    def body_as_summernote(self):
        return self.body
    
    body_as_summernote.allow_tags = True
    body_as_summernote.admin_order_field = 'body'

class Comment(models.Model):
    # users to add a name or alias
    author = models.CharField(max_length=60)
    # body of the comment
    body = models.TextField()
    # the date and time
    created_on = models.DateTimeField(auto_now_add=True)
    # many comments correspond to one post
    post = models.ForeignKey("Post", on_delete=models.CASCADE) #ForeignKey defines a many to one relationship
    # on_delet = models.CASCADE: if the post s deleted so are the comments

    def __str__(self):
        return f"{self.author} on '{self.post}'"