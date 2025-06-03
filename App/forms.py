from django.forms import ModelForm, widgets
from django import forms
from .models import ProjectModel

class ProjectForm(ModelForm):
    class Meta:
        model = ProjectModel
        field = ['title','description','featured','demo_link','source_link','tags']
        # field = '__all__'
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        
        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})
        # self.fields['description'].widget.attrs.update({'class':'input','placeholder':'Add des'})
        # self.fields['featured'].widget.attrs.update({'class':'input'})
        # self.fields['demo_link'].widget.attrs.update({'class':'input'})
        # self.fields['source_link'].widget.attrs.update({'class':'input'})