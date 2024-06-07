from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    Save contact form to database and alerts user of actions outcome.
    """
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for your message! "
                "I will get back to you as soon as possible.",
            )
            return redirect("contact")
        else:
            messages.error(request, "Error sending message")

    else:
        return render(request, "contact/contact.html", {"form": form})
