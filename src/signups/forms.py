if __name__ == '__main__':
   
   from django import forms

   from .models import SignUp
   
   class SignUpForm(forms.ModelForm):
      class Meta:
       model = SignUp
   
