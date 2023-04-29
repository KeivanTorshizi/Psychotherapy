
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from psychotherapy.forms import *

FORMS = [
    ("step_1", WizardStepOneForm),
    ("step_2", WizardStepTwoForm),
    ("step_3", WizardStepThreeForm),
    ("step_4", WizardStepFourForm),
    ("step_5", WizardStepFiveForm),
    ("step_6", WizardStepSixForm),
    ("step_7", WizardStepSevenForm),
    ("step_8", WizardStepEightForm),
    ("step_9", WizardStepNineForm),
    ("step_10", WizardStepTenForm),
    ("step_11", WizardStepElevenForm),
]

TEMPLATES = {
    "step_1": "psychotherapy/profile_step_1.html",
    "step_2": "psychotherapy/profile_step_2.html",
    "step_3": "psychotherapy/profile_step_3.html",
    "step_4": "psychotherapy/profile_step_4.html",
    "step_5": "psychotherapy/therapist_step_1.html",
    "step_6": "psychotherapy/therapist_step_2.html",
    "step_7": "psychotherapy/therapist_step_3.html",
    "step_8": "psychotherapy/therapist_step_4.html",
    "step_9": "psychotherapy/therapist_step_5.html",
    "step_10": "psychotherapy/therapist_step_6.html",
    "step_11": "psychotherapy/therapist_step_7.html",
}


class WizardFormView(SessionWizardView):
    template_name = "psychotherapy/profile_step_1.html"
    form_list = FORMS

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['formset'] = AddLanguageFormSet()
        return context

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_form(self, step=None, data=None, files=None):
        form = super(WizardFormView, self).get_form(step, data, files)
        if step in ('step_11',):
            form.fields['q_t_initial_opinion'].initial = """ 
                    Approximately 82% Among the people who gave answers similar 
                    to yours, they mentioned the following in the pre-counseling 
                    session and initial therapy sessions (psychological consultation):
                    Difficulty in managing emotions, especially anger
                    
                    Increase in anxiety symptoms
                    
                    Challenges in interpersonal communication and partnership
                    
                    So far, by going through this process and participating in the pre-consultation session, 
                    ... clients have been satisfied with more than 98% of their sessions and the suitability 
                    of the therapist for their problem. In the following, after completing the registration process, 
                    in the pre-consultation session, you can discuss all your conditions and needs for effective and
                    targeted therapy sessions (psychological counseling) with ... specialized expert in this
                    field
                 """
        return form

    def render_next_step(self, form, **kwargs):
        # if self.steps.current == 'step_1':
        # data = form.cleaned_data
        # elif self.steps.current == 'step_2':
        #     extra_field_dict = dict()

        return super().render_next_step(form, **kwargs)

    def done(self, form_list, **kwargs):
        data = {'form_data': [form.cleaned_data for form in form_list]}
        all_cleaned_data = self.get_all_cleaned_data()

        # validation forms
        valid_list = list()
        for form in form_list:
            valid_list.append(form.is_valid())

        if "False" not in valid_list:
            customer_obj = CustomerMainInfoModel(
                p_counseling_Individual=all_cleaned_data['p_counseling_Individual'],
                p_counseling_couples_therapy=all_cleaned_data['p_counseling_couples_therapy'],
                p_counseling_child_and_teen=all_cleaned_data['p_counseling_child_and_teen'],

                p_gender_male=all_cleaned_data['p_gender_male'],
                p_gender_female=all_cleaned_data['p_gender_female'],
                p_gender_other=all_cleaned_data['p_gender_other'],

                p_old_26_30=all_cleaned_data['p_old_26_30'],
                p_old_19_25=all_cleaned_data['p_old_19_25'],
                p_old_younger_and_18=all_cleaned_data['p_old_younger_and_18'],
                p_old_31_35=all_cleaned_data['p_old_31_35'],
                p_old_36_45=all_cleaned_data['p_old_36_45'],
                p_old_older_and_45=all_cleaned_data['p_old_older_and_45'],

                p_marital_single=all_cleaned_data['p_marital_single'],
                p_marital_married=all_cleaned_data['p_marital_married'],
                p_marital_in_relationship=all_cleaned_data['p_marital_in_relationship'],
                p_marital_other=all_cleaned_data['p_marital_other'],

                q_t_individual=all_cleaned_data['q_t_individual'],
                q_t_family_and_couple=all_cleaned_data['q_t_family_and_couple'],
                q_t_family=all_cleaned_data['q_t_family'],
                q_t_kids_and_teenagers=all_cleaned_data['q_t_kids_and_teenagers'],
                q_t_sex_therapy=all_cleaned_data['q_t_sex_therapy'],
                q_t_psychiatry=all_cleaned_data['q_t_psychiatry'],

                q_t_chief_complaint=all_cleaned_data['q_t_chief_complaint'],

                q_t_sleep_normal=all_cleaned_data['q_t_sleep_normal'],
                q_t_sleep_less_normal=all_cleaned_data['q_t_sleep_less_normal'],
                q_t_sleep_more_normal=all_cleaned_data['q_t_sleep_more_normal'],

                q_t_sleep_no_impairment=all_cleaned_data['q_t_sleep_no_impairment'],
                q_t_sleep_trouble_falling=all_cleaned_data['q_t_sleep_trouble_falling'],
                q_t_sleep_multiple_waking=all_cleaned_data['q_t_sleep_multiple_waking'],
                q_t_sleep_trouble_waking_up=all_cleaned_data['q_t_sleep_trouble_waking_up'],

                q_t_appetite_normal=all_cleaned_data['q_t_appetite_normal'],
                q_t_appetite_less_normal=all_cleaned_data['q_t_appetite_less_normal'],
                q_t_appetite_more_normal=all_cleaned_data['q_t_appetite_more_normal'],

                q_t_mental_health_services_yes=all_cleaned_data['q_t_mental_health_services_yes'],
                q_t_mental_health_services_no=all_cleaned_data['q_t_mental_health_services_no'],

                q_t_initial_opinion=all_cleaned_data['q_t_initial_opinion'],

            )
            customer_obj.save()

            return render(self.request, 'psychotherapy/done.html', data)
        else:
            return render(self.request, 'psychotherapy/error.html', data)
