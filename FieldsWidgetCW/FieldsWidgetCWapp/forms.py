from django import forms

from .models import HeroModel

powers = [('F', 'Flight'), ('I', 'Invisibility'), ('T', 'Telekinetic'), ('H', 'Healing'), ('O', 'Other')]

# Flight, Speed, Invisibility, Telekenetic, Healing, Other

affiliation = [('G', 'Good'), ('K', 'Kinda Good'), ('N', 'Neutral'), ('L', 'A Little Evil'), ('E', 'Evil')]
# Good, kinda good, neutral, a little evil, evil

richornot = [('R', 'Rich'), ('P', 'Powers')]


class heroForm(forms.ModelForm):
    class Meta:
        model = HeroModel
        fields = "__all__"
        labels = {
            'where': 'city or origin',
            'richOrwhat': 'Are you rich or have super powers?',
            'powers': 'If you have a super power, which ones?',
            'affiliation': 'Which of the following are you?',
            'ability_examples': 'Give us 3 examples of when you used your super hero abilities',
        }
        widgets = {
            'richOrwhat': forms.RadioSelect(choices=richornot),
            'powers': forms.CheckboxSelectMultiple(choices=powers),
            'affiliation': forms.Select(choices=affiliation),

        }
