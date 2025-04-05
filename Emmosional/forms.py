from django import forms
from.models import Emmosionaly

class EmmosionalyForm(forms.ModelForm):
    class Meta:
        model = Emmosionaly
        fields = "__all__"
        widgets={
            'title':forms.TextInput(),
            "video":forms.FileInput(),
            "image":forms.FileInput(),
            "description":forms.Textarea(attrs={'rows':4}),
            "image":forms.FileInput(),
            }
        
      
    def __init__(self, *args, **kwargs):
        super(EmmosionalyForm, self).__init__(*args, **kwargs)    
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'