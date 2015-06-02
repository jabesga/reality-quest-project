from django import forms
from models import Mission, NPC


class NPCForm(forms.Form):
    name = forms.CharField(max_length=128)
    portrait_style = forms.IntegerField(max_value=10, widget=forms.Select(choices=[
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]))
    lat = forms.FloatField()
    lng = forms.FloatField()
    quote_1 = forms.CharField(max_length=128)
    quote_2 = forms.CharField(max_length=128)
    quote_3 = forms.CharField(max_length=128)
    quote_4 = forms.CharField(max_length=128)


class MissionForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    mission_briefing = forms.CharField(max_length=128)

    start_with = forms.ModelChoiceField(queryset=NPC.objects.all(), empty_label=None)
    start_quote = forms.CharField(max_length=128)

    end_with = forms.ModelChoiceField(queryset=NPC.objects.all(), empty_label=None)
    end_quote = forms.CharField(max_length=128)

    class Meta:
        model = Mission
        fields = ('name', 'mission_briefing', 'start_with', 'start_quote', 'end_with', 'end_quote')



