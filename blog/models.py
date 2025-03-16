from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def delete(self, *args, **kwargs):
        self.images.all().delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug or self._state.adding:
            original_slug = slugify(self.title)
            slug = original_slug
            count = 1

            while BlogPost.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{count}"
                count += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class BlogPostImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return f"Image for {self.blog_post.title}"
