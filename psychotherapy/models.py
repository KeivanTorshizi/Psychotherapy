from django.db import models


class CustomerMainInfoModel(models.Model):

    chief_complaint_choices = [
        ('1', 'I feel Stress and Anxiety (constant worry).'),
        ('2', 'I have problems due to specific medications, drugs, or alcohol.'),
        ('3', 'I"m hyperactive, and I feel euphoric.'),
        ('4', 'I experience distress due to my education/occupation.'),
        ('5', 'I experience overthinking, obsessive thoughts, and behaviors.'),
        ('6', 'I am in the process of immigrating, or I have been immigrating for many years, '
              'and I need to speak with a Persian-speaking therapist due to Immigration Issues.'),
        ('7', ' I experience sexual impairment and issues.'),
        ('8', 'I intend to get married, and I want to make the right decision.'),
        ('9', 'I have some issues in my relationship/family.'),
        ('10', 'I’m going to be a father or mother for the first time and talk to a therapist about my concerns '
               '(parenting, pregnancy, etc.)'),
        ('11', 'I have experienced hallucinations or delusions.'),
        ('12', 'I feel depressed, exhausted, and unmotivated.'),
        ('13', 'I experience mental distress due to medical conditions such as MS, Cardiovascular Disease, '
               'etc.'),
        ('14', 'I have a traumatic experience or an unfortunate event ' 
               'that has dramatically affected my feelings and life. (Grief, Sexual Abuse, bankruptcy, etc.) '),
    ]

    p_counseling_Individual = models.BooleanField(default=False)
    p_counseling_couples_therapy = models.BooleanField(default=False)
    p_counseling_child_and_teen = models.BooleanField(default=False)

    p_gender_male = models.BooleanField(default=False)
    p_gender_female = models.BooleanField(default=False)
    p_gender_other = models.BooleanField(default=False)

    p_old_26_30 = models.BooleanField(default=False)
    p_old_19_25 = models.BooleanField(default=False)
    p_old_younger_and_18 = models.BooleanField(default=False)
    p_old_31_35 = models.BooleanField(default=False)
    p_old_36_45 = models.BooleanField(default=False)
    p_old_older_and_45 = models.BooleanField(default=False)

    p_marital_single = models.BooleanField(default=False)
    p_marital_married = models.BooleanField(default=False)
    p_marital_in_relationship = models.BooleanField(default=False)
    p_marital_other = models.BooleanField(default=False)

    q_t_individual = models.BooleanField(default=False)
    q_t_family_and_couple = models.BooleanField(default=False)
    q_t_family = models.BooleanField(default=False)
    q_t_kids_and_teenagers = models.BooleanField(default=False)
    q_t_sex_therapy = models.BooleanField(default=False)
    q_t_psychiatry = models.BooleanField(default=False)

    q_t_chief_complaint = models.CharField(max_length=5, null=True, choices=chief_complaint_choices)

    q_t_sleep_normal = models.BooleanField(default=False)
    q_t_sleep_less_normal = models.BooleanField(default=False)
    q_t_sleep_more_normal = models.BooleanField(default=False)

    q_t_sleep_no_impairment = models.BooleanField(default=False)
    q_t_sleep_trouble_falling = models.BooleanField(default=False)
    q_t_sleep_multiple_waking = models.BooleanField(default=False)
    q_t_sleep_trouble_waking_up = models.BooleanField(default=False)

    q_t_appetite_normal = models.BooleanField(default=False)
    q_t_appetite_less_normal = models.BooleanField(default=False)
    q_t_appetite_more_normal = models.BooleanField(default=False)

    q_t_mental_health_services_yes = models.BooleanField(default=False)
    q_t_mental_health_services_no = models.BooleanField(default=False)

    q_t_initial_opinion = models.TextField(max_length=250, default="")

    class Meta:
        ordering = ['-id']
