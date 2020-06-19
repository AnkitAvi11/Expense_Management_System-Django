from django.db import models
from django.contrib.auth.models import User

#   model for admin profile
class UserProfile(models.Model) : 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200)
    user_bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to = 'images/%Y/%m', default='default.png', blank=True, null=True)
    
    def __str__(self) : 
        return self.user_name

    #   overriding save method
    def save(self, *args, **kwargs) : 
        try : 
            prev = UserProfile.objects.get(id=self.id)
            if prev.profile_pic != self.profile_pic :
                prev.profile_pic.delete()
        except : 
            pass
        super().save(*args, **kwargs)

    #   overriding delete function
    def delete(self, *args, **kwargs) : 
        self.profile_pic.delete()
        super().delete(*args, **kwargs)
    

