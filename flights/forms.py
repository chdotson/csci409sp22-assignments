from django import forms

AIRLINE_CHOICES = (
    (1, "MYR"),
    (2, "CLT"),
    (3, "ATL"),
)
class FlightForm(forms.Form):
    from_origin = forms.ChoiceField(label='Origin:', choices=AIRLINE_CHOICES)
    to_destination = forms.ChoiceField(label='Destination:', choices=AIRLINE_CHOICES)


    # to_destination = forms.CharField(label='Destination:', max_length=3)

