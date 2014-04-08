"""This very fancy doc string shows how this file works."""


if __name__ == '__main__':
    
    from django.shortcuts import render, render_to_response, RequestContext

    from .forms import SignUpForm
    # Create your views here.
    def home(request):
        """Defines the home page."""
        form = SignUpForm(request.POST or None)
        
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
            
        return render_to_response("signup.html",
                                  locals(),
                                  context_instance=RequestContext(request))
