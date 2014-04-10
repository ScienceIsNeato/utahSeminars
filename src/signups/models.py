"""
This module houses the forms used to...
    - Sign up users
    - Add events to the database
    - Query the databsae
"""

if __name__ == '__main__':

    from django.db import models
    from django.utils.encoding import smart_unicode
    
    # Create your models here.
    class SignUp(models.Model):
        first_name = models.CharField(max_length=120, null=True, blank=True)
        last_name = models.CharField(max_length=120, null=True, blank=True)
        email = models.EmailField(null=False)
        timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
        updated = models.DateTimeField(auto_now_add=False, auto_now=True)
        
        def __unicode__(self):
            return smart_unicode(self.email)
    
