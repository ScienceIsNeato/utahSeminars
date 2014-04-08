if __name__ == '__main__':
    from django.contrib import admin
    
    # Register your models here.
    from .models import SignUp
    
    
    
    class SignUpAdmin(admin.ModelAdmin):
        """Class Def for administration signups.
    
        Args:
            admin.ModelAdmin: loads the controller for the model of
            an administrator data object
    
        Returns:
            None
        """
        class Meta:
            model = SignUp
            
            
    admin.site.register(SignUp, SignUpAdmin)
