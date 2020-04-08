from django import forms

class SearchedSummonerNameForm(forms.Form):
     summoner_name = forms.CharField(min_length=3, max_length=16, strip=True, required=True)

     def clean_summoner_name(self):
          data = self.cleaned_data['summoner_name']
          return data