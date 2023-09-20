# epaper/views.py

from django.core.mail import EmailMultiAlternatives
from django.db import connection
from django.utils.translation import get_language
from django.views.generic import FormView, TemplateView
from core.models import Settings

from epaper.models import EPaperEmail
from epaper.forms import EPaperForm

class EPaperView(FormView):
    template_name = "epaper/epaper.html"

    form_class = EPaperForm
    success_url = '/epaper/thanks/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if not EPaperEmail.objects.filter(email=self.object.email):
            self.object.save()
            to = [self.object.email]
            self.send_mail(to)
        return super().form_valid(form)
    
    def send_mail(self, to):
        language =  get_language()
        setting =  Settings.objects.get(id=language)
        subject =f'您已成功訂閱 {setting.sitename} 電子報'
        text_content = f'您已成功訂閱 {setting.sitename} 電子報'
        html_content = f'<p>您已成功訂閱 {setting.sitename} 電子報</p>'
        msg = EmailMultiAlternatives(subject, text_content, None, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    
class EPaperThanksView(TemplateView):
    template_name = "epaper/thanks.html"