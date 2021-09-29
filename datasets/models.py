from django.db import models

class Dataset(models.Model):

    title = models.CharField(max_length=80)
    slug_title = models.SlugField

    code = models.TextField(blank=False)
    about = models.TextField(blank=False)
    
    free = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    
    num_downloads = models.IntegerField(default=0)

    #user_id = models.ForeignKey(admin.user, on_delete=models.CASCADE)
