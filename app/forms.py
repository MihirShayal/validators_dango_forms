from django import forms

def valid_for_i(svalue):
    if svalue[0]=='i':
        raise forms.ValidationError('student name can not be start from i')
    

def valid_for_len(name):
    if len(name)<5:
        raise forms.ValidationError('length is Less than 5')
    

class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100,validators=[valid_for_i,valid_for_len])
    sage=forms.IntegerField()
    email=forms.EmailField(validators=[valid_for_i])
    remail=forms.EmailField()
    url=forms.URLField()

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['remail']

        if e != re:
            raise forms.ValidationError('Invalid Data')
        
    def clean_url(self):
        u=self.cleaned_data['url']
        if u[-1].lower() == 'a':
            raise forms.ValidationError('URL shount not be start with a')