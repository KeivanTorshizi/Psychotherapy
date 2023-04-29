
from django import forms
from .models import *


class WizardStepOneForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    p_counseling_Individual = forms.BooleanField(label='Individual', required=False)
    p_counseling_couples_therapy = forms.BooleanField(label='CouplesTherapy', required=False)
    p_counseling_child_and_teen = forms.BooleanField(label='ChildAndTeen', required=False)

    p_counseling_Individual.widget.attrs.update({'class': 'chb'})
    p_counseling_couples_therapy.widget.attrs.update({'class': 'chb'})
    p_counseling_child_and_teen.widget.attrs.update({'class': 'chb'})

    def clean(self):
        super(WizardStepOneForm, self).clean()
        # p_counseling_Individual = self.cleaned_data.get('p_counseling_Individual')
        return self.cleaned_data


class WizardStepTwoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    p_gender_male = forms.BooleanField(label='Male', required=False)
    p_gender_female = forms.BooleanField(label='Female', required=False)
    p_gender_other = forms.BooleanField(label='Other', required=False)

    p_gender_male.widget.attrs.update({'class': 'chb'})
    p_gender_female.widget.attrs.update({'class': 'chb'})
    p_gender_other.widget.attrs.update({'class': 'chb'})


class WizardStepThreeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    p_old_26_30 = forms.BooleanField(label='26_30', required=False)
    p_old_19_25 = forms.BooleanField(label='19_25', required=False)
    p_old_younger_and_18 = forms.BooleanField(label='Younger and 18', required=False)
    p_old_31_35 = forms.BooleanField(label='31_35', required=False)
    p_old_36_45 = forms.BooleanField(label='36_45', required=False)
    p_old_older_and_45 = forms.BooleanField(label='Older and 45', required=False)

    p_old_26_30.widget.attrs.update({'class': 'chb'})
    p_old_19_25.widget.attrs.update({'class': 'chb'})
    p_old_younger_and_18.widget.attrs.update({'class': 'chb'})
    p_old_31_35.widget.attrs.update({'class': 'chb'})
    p_old_36_45.widget.attrs.update({'class': 'chb'})
    p_old_older_and_45.widget.attrs.update({'class': 'chb'})


class WizardStepFourForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    p_marital_single = forms.BooleanField(label='Single', required=False)
    p_marital_married = forms.BooleanField(label='Married', required=False)
    p_marital_in_relationship = forms.BooleanField(label='In_relationship', required=False)
    p_marital_other = forms.BooleanField(label='Other', required=False)

    p_marital_single.widget.attrs.update({'class': 'chb'})
    p_marital_married.widget.attrs.update({'class': 'chb'})
    p_marital_in_relationship.widget.attrs.update({'class': 'chb'})
    p_marital_other.widget.attrs.update({'class': 'chb'})


class WizardStepFiveForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    q_t_individual = forms.BooleanField(label='Individual', required=False)
    q_t_family_and_couple = forms.BooleanField(label='Family and couple', required=False)
    q_t_family = forms.BooleanField(label='Family', required=False)
    q_t_kids_and_teenagers = forms.BooleanField(label='Kids and teenagers', required=False)
    q_t_sex_therapy = forms.BooleanField(label='Sex therapy', required=False)
    q_t_psychiatry = forms.BooleanField(label='Psychiatry', required=False)

    q_t_individual.widget.attrs.update({'class': 'chb'})
    q_t_family_and_couple.widget.attrs.update({'class': 'chb'})
    q_t_family.widget.attrs.update({'class': 'chb'})
    q_t_kids_and_teenagers.widget.attrs.update({'class': 'chb'})
    q_t_sex_therapy.widget.attrs.update({'class': 'chb'})
    q_t_psychiatry.widget.attrs.update({'class': 'chb'})


class WizardStepSixForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    q_t_chief_complaint = forms.ChoiceField(choices=CustomerMainInfoModel.chief_complaint_choices,
                                            widget=forms.RadioSelect, label="", required=False)
    q_t_chief_complaint.widget.attrs.update({'class': 'label'})
    q_t_chief_complaint.widget.attrs.update({'class': 'form-check'})


class WizardStepSevenForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    q_t_sleep_normal = forms.BooleanField(label='Regular/Normal', required=False)
    q_t_sleep_less_normal = forms.BooleanField(label='Irregular/Less than normal', required=False)
    q_t_sleep_more_normal = forms.BooleanField(label='Irregular/More than normal', required=False)
    q_t_sleep_normal.widget.attrs.update({'class': 'chb'})
    q_t_sleep_less_normal.widget.attrs.update({'class': 'chb'})
    q_t_sleep_more_normal.widget.attrs.update({'class': 'chb'})


class WizardStepEightForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    q_t_sleep_no_impairment = forms.BooleanField(label='No impairment (Satisfied with the amount and duration)',
                                                 required=False)
    q_t_sleep_trouble_falling = forms.BooleanField(label='Trouble in falling sleep', required=False)
    q_t_sleep_multiple_waking = forms.BooleanField(label='multiple waking up in midnight', required=False)
    q_t_sleep_trouble_waking_up = forms.BooleanField(label='trouble in waking up', required=False)

    q_t_sleep_no_impairment.widget.attrs.update({'class': 'chb'})
    q_t_sleep_trouble_falling.widget.attrs.update({'class': 'chb'})
    q_t_sleep_multiple_waking.widget.attrs.update({'class': 'chb'})
    q_t_sleep_trouble_waking_up.widget.attrs.update({'class': 'chb'})


class WizardStepNineForm(forms.Form):
    q_t_appetite_normal = forms.BooleanField(label='Regular/ Normal', required=False)
    q_t_appetite_less_normal = forms.BooleanField(label='Irregular/ Less than normal', required=False)
    q_t_appetite_more_normal = forms.BooleanField(label='Irregular/ More than normal', required=False)
    q_t_appetite_normal.widget.attrs.update({'class': 'chb'})
    q_t_appetite_less_normal.widget.attrs.update({'class': 'chb'})
    q_t_appetite_more_normal.widget.attrs.update({'class': 'chb'})


class WizardStepTenForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    q_t_mental_health_services_yes = forms.BooleanField(label='Yes', required=False)
    q_t_mental_health_services_no = forms.BooleanField(label='No', required=False)
    q_t_mental_health_services_yes.widget.attrs.update({'class': 'chb'})
    q_t_mental_health_services_no.widget.attrs.update({'class': 'chb'})


class WizardStepElevenForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q_t_initial_opinion'].widget.attrs.update({'class': 'form-control'})
    q_t_initial_opinion = forms.CharField(widget=forms.Textarea, required=False, label="")
