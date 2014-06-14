from django import forms
from models import UploadFile
 
 
class UploadFileForm(forms.ModelForm):
     
    class Meta:
        model = UploadFile







  {% extends "base1.html" %}
{% load i18n %}

{% block title %}{% trans "Password reset" %}{% endblock %}

{% block content %}

<h1>{% trans "Password reset" %}</h1>

<p>{% trans "Forgotten your password? Enter your email address below, and we'll email instructions for setting a new one." %}</p>

<form action="" method="post">{% csrf_token %}
{{ form.email.errors }}
<p><label for="id_email">{% trans 'Email address:' %}</label> {{ form.email }} <input type="submit" value="{% trans 'Reset my password' %}" /></p>
</form>

{% endblock %}