from django.http import HttpResponseRedirect # helps redirect the request in the return statement
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm

# will display a list of all your posts
def blog_index(request):
    posts = Post.objects.all().order_by("-created_on") # obtain a Queryset containing all the posts in the database.
    # context dictionary
    context = {
        "posts": posts,
    }
    # a template named index.html
    return render(request, "blog/index.html", context)

# will be similar to blog_index, but the posts shown will only be of a specific category that the user chooses.
def blog_category(request, category):
    posts = Post.objects.filter( #argument of the filter tells Django what conditions need to be true to retrieve an object
        categories__name__contains=category
    ).order_by("-created_on")
    # add these posts and the category to the context dictionary
    context = {
        "category": category,
        "posts": posts,
    }
    # a category.html template.
    return render(request, "blog/category.html", context)

# will display the full post. 
# Later, this view will also show existing comments and a form to allow users to create new comments.
# take a primary key value as an argument
def blog_detail(request, pk):
    # retrieves the object with said key
    post = Post.objects.get(pk=pk)

    # # retrieve the author of the post
    # author = post.author  # Assuming the author field is a ForeignKey to the Author model
    
    form = CommentForm() # an instance of a comment form
    if request.method == "POST": # check for a POST request
        form = CommentForm(request.POST) # update the form with the data from POST request
        if form.is_valid(): # check the user has entered all fields correctly
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post, # connect to an existing post using the pk
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    # getting the comments assigned to the post
    comments = Comment.objects.filter(post=post)
    # adding comments and posts tot the context dictionary
    context = {
        "post": post,
        # "author": author,
        "comments": comments,
        "form": CommentForm(),
    }
    # details.html template
    return render(request, "blog/detail.html", context)
