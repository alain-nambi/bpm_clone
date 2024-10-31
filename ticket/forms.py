from django import forms


class HelpDeskForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(HelpDeskForm, self).__init__(*args, **kwargs)

    title = forms.CharField(
        max_length=150,
        label="Title",
        widget=forms.TextInput(
            attrs={
                "class": "input input-bordered w-full max-w-xs",
                "placeholder": "ex: Need mouse and new keyboard",
            }
        )
    )
    contact = forms.CharField(
        label="N° téléphone",
        widget=forms.TextInput(
            attrs={
                "class": "input input-bordered w-full max-w-xs",
                "placeholder": "ex: +261 32 58 452 12"
            }
        ),
        required=True,
        initial="",
    )
    details = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "input input-bordered w-full max-w-xs",
                "placeholder": "ex: My mouse has broken and some keys in my keyboard don't work anymore"
            }
        ),

        label="Details",
        required=False
    )