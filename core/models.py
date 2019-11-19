from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

choice=(('yes','Yes'),('no','No'))
choice1=(('not at all','Not At All'),('Less than once a week','Less than once a week'),('Once a week or more','Once a week or more'))
choice2=(('never have gambled','never have gambled'),('more than $100 up to $1000','more than $100 up to $1000'),('$10 or less','$10 or less'),('more than $1000 up to $10,000','more than $1000 up to $10,000'),('more than $10 up to $100','more than $10 up to $100'),('more than $10,000','more than $10,000'))
choice3=(('both my father and mother gamble (or gambled)','both my father and mother gamble (or gambled)'),('my father gambles (or gambled) too much','my father gambles (or gambled) too much'),('my mother gambles (or gambled) too much','my mother gambles (or gambled) too much'),('neither gambles (or gambled) too much','neither gambles (or gambled) too much'))
choice4=(('never','never'),('some of the time (less than half the time) I lost','some of the time (less than half the time) I lost'),('most of the time I lost','most of the time I lost'),('every time I lost','every time I lost'))
choice5=(('never (or never gamble','never (or never gamble'),('yes, less than half the time I lost','yes, less than half the time I lost'),('yes, most of the time','yes, most of the time'))
choice6=(('no','No'),('yes, in the past, but not now','yes, in the past, but not now'),('Yes','Yes'))
choice7=(('Pre-contemplation','Pre-contemplation'),('Contemplation ','Contemplation'),('Preparation','Preparation'),('Action','Action'),('Maintenance','Maintenance'),('Patient refused family counseling at this time  Patient accepted family counseling','Patient refused family counseling at this time  Patient accepted family counseling '))
choice8=(('Low','Low'),('Moderate','Moderate'),('High','High'))
option1= (('Alcohol use disorder','Alcohol use disorder'),('Cannabis use disorder','Cannabis use disorder'),('Cocaine use disorder','Cocaine use disorder'),('Opioid use disorder','Opioid use disorder'),('other hellucinogen use disorder','other hellucinogen use disorder'),('Phencyclidine use disorder','Phencyclidine use disorder'),('Sedative,hypnotic or anxiolytic use disorder','Sedative,hypnotic or anxiolytic use disorder'))
option2= (('305.00','305.00'),('303.90','303.90'),('291.81','291.81'),('305.20','305.20'),('304.30','304.30'),('292.0','292.0'),('292.89','292.89'),('305.60','305.60'),('304.20','304.20'),('305.50','305.50'),('304.00','304.00'),('305.30','305.30'),('304.60','304.60'),('305.40','305.40'),('304.10','304.10'))
option3= (('F10.10','F10.10'),('F10.20','F10.20'),('F12.10','F12.10'),('F12.288','F12.288'),('F14.10','F14.10'),('F14.20','F14.20'),('F14.23','F14.23'),('F11.10','F11.10'),('F11.20','F11.20'),('F11.23','F11.23'),('F16.10','F16.10'),('F116.20','F116.20'),('F13.10','F13.10'),('F13.20','F13.20'))
option4= (('Alcohol use disorder,Mild','Alcohol use disorder,Mild'),('Alcohol use disorder,Moderate','Alcohol use disorder,Moderate'),('Alcohol use disorder,Severe','Alcohol use disorder,Severe'),('Alcohol withdrawl','Alcohol withdrawl'),('Cannabis use disorder,Mild','Cannabis use disorder,Mild'),('Cannabis use disorder,Moderate','Cannabis use disorder,Moderate'),('Cannabis use disorder,Severe','Cannabis use disorder,Severe'),('Cannabis withdrawl','Cannabis withdrawl'),('Cannabis-induced anxietu disorder','Cannabis-induced anxiety disorder'),('Cocaine use disorder,Mild','Cocaine use disorder,Mild'),('Cocaine use disorder,Moderate','Cocaine use disorder,Moderate'),('Cocaine use disorder,Severe','Cocaine use disorder,Severe'),('Cocaine withdrawl','Cocaine withdrawl'),('Cocaine-induced anxiety disorder','Cocaine-induced anxiety disorder'),('Opioid use disorder,Mild','Opioid use disorder,Mild'),('Opioid use disorder,Moderate','Opioid use disorder,Moderate'),('Opioid use disorder,Severe','Opioid use disorder,Severe'),('Opioid withdrawl','Opioid withdrawl'),('Opioid withdrawl,delirium','Opioid withdrawl,delirium'),('other hellucinogen use disorder,Mild','other hellucinogen use disorder,Mild'),('other hellucinogen use disorder,Moderate','other hellucinogen use disorder,Moderate'),('other hellucinogen use disorder,Severe','other hellucinogen use disorder,Severe'),('other hellucinogen-induced anxiety disorder','other hellucinogen-induced anxiety disorder'),('Phencyclidine use disorder,Mild','Phencyclidine use disorder,Mild'),('Phencyclidine use disorder,Moderate','Phencyclidine use disorder,Moderate'),('Phencyclidine use disorder,Severe','Phencyclidine use disorder,Severe'),('Phencyclidine-induced anxiety disorder','Phencyclidine-induced anxiety disorder'),('Sedative,hypnotic or anxiolytic use disorder,Mild','Sedative,hypnotic or anxiolytic use disorder,Mild'),('Sedative,hypnotic or anxiolytic use disorder,Mpderate','Sedative,hypnotic or anxiolytic use disorder,Moderate'),('Sedative,hypnotic or anxiolytic use disorder,Severe','Sedative,hypnotic or anxiolytic use disorder,Severe'),('Sedative,hypnotic or anxiolytic withdrawl','Sedative,hypnotic or anxiolytic withdrawl'))
referal=(('Inpatient','Inpatient'),('OP','OP'),('IOP','IOP'),('other','other'))

#DSM V code
strength=(('Educated','Educated'),('Intelligent Motivated','Intelligent Motivated'),('family Support','family Support'),('Employed','Employed'),('Hardworking','Hardworking'),('Have Financial Resources','Have Financial Resources'),('Have 12 steps Recovery Support','Have 12 steps Recovery Support'),('Good Health','Good Health'),('Other:','Other:'))
stressor=(('Unemployment','Unemployment'),('Homelessness','Homelessness'),('Substance use in Household','Substance use in Household'),('Family Conflict','Family Conflict'),('Relationship Problem','Relationship Problem'),('Financial Problem','Financial Problem'),('Legal Problem','Legal Problem'),('Health Problem','Health Problem'),('Mental Health Problem','Mental Health Problem'),('Education Problem','Education Problem'),('Medical Problem','Medical Problem'))
barrier=(('Transportation','Transportation'),('Physical Disability','Physical Disability'),('Mental Health','Mental Health'),('Language Problem','Language Problem'),('Religious Restrictions','Religious Restrictions'),('Cultural Restrictions','Cultural Restrictions'))
longterm=(('Maintain A program of recovery,free from impulsive behaviour and addictions','Maintain A program of recovery,free from impulsive behaviour and addictions'),('Reduce the frequency of impuslive behaviour and increase the frequency of behaviour that is carefully thought out','Reduce the frequency of impuslive behaviour and increase the frequency of behaviour that is carefully thought out'))
longterm1=(('Maintain A program of recovery,free of addictions and legal conflicts','Maintain A program of recovery,free of addictions and legal conflicts'),('Accept responsibility for legal problems without blaming others','Accept responsibility for legal problems without blaming others'),('consult with legal authorities(e.g., attorney, probation officer, police, court official) to make plans for adjugating legal conflicts','consult with legal authorities(e.g., attorney, probation officer, police, court official) to make plans for adjugating legal conflicts'),('Understand the need to maintain abstinence to remain free of negative conseqences, which include legal problem','Understand the need to maintain abstinence to remain free of negative conseqences, which include legal problem'),('Decrease antisocial behaviours and increase prosocial behavious','Decrease antisocial behaviours and increase prosocial behavious'))
longterm2 =(('Maintain A program of recovery,free of addictions and negative impact of deficient environment','Maintain A program of recovery,free of addictions and negative impact of deficient environment'),('Improve the social, occupational , financial and living situation sufficiently to increase the probability of a successful recovery from addiction','Improve the social, occupational , financial and living situation sufficiently to increase the probability of a successful recovery from addiction'),('Understand the negative impact of current enviroment on addiction recovery','Understand the negative impact of current enviroment on addiction recovery'),('Develop a peer group that is supportive of revovery','Develop a peer group that is supportive of revovery'),('Family members support the client recovery ','Family members support the client recovery'))
longterm3=(('Maintain A program of recovery,free of addictions and negative impact of medical issues','Maintain A program of recovery,free of addictions and negative impact of medical issues'),('Resolve medical problem and return to a normal level of functioning','Resolve medical problem and return to a normal level of functioning'),('Understand the relationship between medical issues','Understand the relationship between medical issues'))
problem1=(('Exhibits a tendency to act too quickly on imoulses','Exhibits a tendency to act too quickly on imoulses'),('Demonstartes difficulty in patience, particularly while waiting for someone or waiting in line','Demonstartes difficulty in patience, particularly while waiting for someone or waiting in line'),('Impulsively facilitate a self-defeating pattern of addiction behaviour','Impulsively facilitate a self-defeating pattern of addiction behaviour'),('Reports loss of overaggressiveness impulses, resulting in assault , self destructive behaviour, and/or damage to property','Reports loss of overaggressiveness impulses, resulting in assault , self destructive behaviour, and/or damage to property'),('Desires Everything Immediately-demonstrates a deceased ability to delay pleasure or gratification','Desires Everything Immediately-demonstrates a deceased ability to delay pleasure or gratification'),('Has a history of acting out atleast in two areas that are potentially self damaging(e.g., spending money,sexual activity,reckless driving,addiction)','Has a history of acting out atleast in two areas that are potentially self damaging(e.g., spending money,sexual activity,reckless driving,addiction'),('Overreacts to mildly averse or pleasure oriented stimulation','Overreacts to mildly averse or pleasure oriented stimulation'),('Expereince a sense of tension or affective arousal before engaging in the impulsive behaviour (e.g., kleptomania or pyromania)','Expereince a sense of tension or affective arousal before engaging in the impulsive behaviour (e.g., kleptomania or pyromania)'),('Senses pleasure,gratification or release at the time of commiting an antisocial act','Senses pleasure,gratification or release at the time of commiting an antisocial act'))

problem2=(('Presents with legal charges pending adjudication','Presents with legal charges pending adjudication'),('Has  a history of repeated violations of the law, many occuring under the influence of drugs or alcohol','Has  a history of repeated violations of the law, many occuring under the influence of drugs or alcohol'),('Unresolved legal probolems are complicaiting recovery from addiction','Unresolved legal probolems are complicaiting recovery from addiction'),('Express a fear of legal system adjudicating current problems','Express a fear of legal system adjudicating current problems'),('Has  a history of repeated violations of the law related to buying ,selling or using illegal substances','Has  a history of repeated violations of the law related to buying ,selling or using illegal substances'),('Is undera court order to seek treatment for addiction','Is undera court order to seek treatment for addiction'),('Express feelings of anger,resentment and fear of abandonment associated with impending divorce','Express feelings of anger,resentment and fear of abandonment associated with impending divorce'),('Chemical dependancy has resulted in several arrests','Chemical dependancy has resulted in several arrests'),('Fears loss freedom due to current legal charges','Fears loss freedom due to current legal charges'))

problem3=(('lives in an environment which is a high risk for relapse','lives in an environment which is a high risk for relapse'),('Lives with an individual who is a regular user/abuser of alochol/drugs','Lives with an individual who is a regular user/abuser of alochol/drugs'),('Experiencing significant social isolation,withdrawl from social life','Experiencing significant social isolation,withdrawl from social life'),('Lives in an environment in which there is high risk of physical ,sexual or emotional abuse','Lives in an environment in which there is high risk of physical ,sexual or emotional abuse'),('Has many friends who are criminals or addicted','Has many friends who are criminals or addicted'),('Reports that family is angry or negative towards the addict and not supportive of recovery program','Reports that family is angry or negative towards the addict and not supportive of recovery program'),('Present as financial destitute and in need of assistance of adequeste food and shelter','Present as financial destitute and in need of assistance of adequeste food and shelter'),('Associates nith peer group members who are regular user/abuser of alcohol/drugs','Associates nith peer group members who are regular user/abuser of alcohol/drugs'),('Lives ina neighbourhood that has high incidence of alcohol and drugs as well as crimes','Lives ina neighbourhood that has high incidence of alcohol and drugs as well as crime'))
problem4=(('Has been diagnosed with medical problems that complicate the recovery from addiction','Has been diagnosed with medical problems that complicate the recovery from addiction'),('Presents with medical problems that require medical monitoring of medications or assistance with mobility','Presents with medical problems that require medical monitoring of medications or assistance with mobility'),('Has organic brain syndrome that compromises learning as a result of use of mood altering chemicals','Has organic brain syndrome that compromises learning as a result of use of mood altering chemicals'),('Demonstartes inability to  self-administer prescribed medication','Demonstartes inability to  self-administer prescribed medication'),('Suffers from chronic pain syndrome, which places the client for high risk replace','Suffers from chronic pain syndrome, which places the client for high risk relapse'),('Has mediacl problems that require medical/nursing assistance','Has mediacl problems that require medical/nursing assistance'),('Self-medicates medical problems through use of mood altering chemicals','Self-medicates medical problems through use of mood altering chemicals'),('Reports negative emotions concerning medical illness that led to addiction','Reports negative emotions concerning medical illness that led to addiction'),('Demonstrates a compromised ability to concentrate on recovery due to severity of medical problems','Demonstrates a compromised ability to concentrate on recovery due to severity of medical problems'),('Blames substance abuse on medical issues and denies a primary substance abuse disorder','Blames substance abuse on medical issues and denies a primary substance abuse disorder'),('Doctor shops in order to obtain medication necessary to reduce symptoms','Doctor shops in order to obtain medication necessary to reduce symptoms'))


session=(('Individual','Individual'),('Group','Group'),('Case Note','Case Note'))
group=(('Process Group','Process Group'),('Education Group','Education Group'),('Family','Family'),('N/A','N/A'))
topic=(('Relationships','Relationships'),('Work Problems','Work Problems'),('Alcohol/Drug Problems','Alcohol/Drug Problems'),('Parenting','Parenting'),('Abuse','Abuse'),('Childhood/Family of origin','Childhood/Family of origin'),('Sexual','Sexual'),('Homework assignments','Homework assignments'),('Process','Process'),('Logistics/Structure','Logistics/Structure'),('HIV/AIDS','HIV/AIDS'),('Other:','Other:'))
acute=(('Client appears to be making little or no progress','Client appears to be making little or no progress'),('Client appears to be making considerable progress','Client appears to be making considerable progress'),('Resolved','Resolved'),('Not Applicable','Not Applicable'),('Not Assessed','Not Assessed'))
thought=(('Coherent','Coherent'),('Logical','Logical'),('Tangential','Tangential'),('Loose','Loose'),('Circumstantial','Circumstantial'),('Fight of ideas','Fight of ideas'),)
mood=(('Normal','Normal'),('Anxious','Anxious'),('Depressed','Depressed'),('Angry','Angry'),('Euphoric','Euphoric'),('Other:','Other:'))
dx=(('Alcohol use disorder,Mild','Alcohol use disorder,Mild'),('Alcohol use disorder,Moderate','Alcohol use disorder,Moderate'),('Alcohol use disorder,Severe','Alcohol use disorder,Severe'),('Cannabis use disorder,Mild','Cannabis use disorder,Mild'),('Cannabis use disorder,Moderate','Cannabis use disorder,Moderate'),('Cannabis use disorder,Severe','Cannabis use disorder,Severe'),('Cocaine use disorder,Mild','Cocaine use disorder,Mild'),('Cocaine use disorder,Moderate','Cocaine use disorder,Moderate'),('Cocaine use disorder,Severe','Cocaine use disorder,Severe'),('Opioid use disorder,Mild','Opioid use disorder,Mild'),('Opioid use disorder,Moderate','Opioid use disorder,Moderate'),('In Partial remission','In Partial remission'),('In full remission','In full remission'),('Other:','Other:'))
list_objective=(('Abstinenece','Abstinenece'),('Employment','Employment'),('Family Conflict','Family Conflict'),('Housing','Housing'),('Mental Health','Mental Health'),('Education','Education'),('Legal','Legal'),('Support Network','Support Network'),)


class profileModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

# FORMS
class HRRS_INTAKE_SCREEN(models.Model):
    user                           =   models.ForeignKey(User,on_delete=models.CASCADE)    
    date                           =   models.DateField(blank=True,null=True)
    name                           =   models.CharField(max_length=100,blank=True)
    type_of_insurance              =   models.CharField(max_length=100,blank=True)
    medicaid_number                =   models.CharField(max_length=100,blank=True)
    Name_of_Insurance_Holder       =   models.CharField(max_length=100,blank=True)
    DOB                            =   models.DateField(blank=True,null=True)
    ss_number                      =   models.CharField(max_length=100,blank=True)
    race                           =   models.CharField(max_length=100,blank=True)
    address                        =   models.CharField(max_length=100,blank=True) 
    home_tel                       =   models.CharField(max_length=100,blank=True)
    cell_tel                       =   models.CharField(max_length=100,blank=True)
    emergency_contact              =   models.CharField(max_length=100,blank=True)
    relationship_to_ct             =   models.CharField(max_length=100,blank=True)
    telephone_numer                =   models.CharField(max_length=100,blank=True)
    permission_to_contact          =   models.CharField(max_length=100,choices=choice,blank=True)
    referral_source                =   models.CharField(max_length=100,blank=True)
    substance_abuse_history        =   models.CharField(max_length=100,choices=choice,blank=True)
    drug_of_choice                 =   models.CharField(max_length=100,blank=True) 
    date_last_used                 =   models.DateField(blank=True,null=True)
    drug_used                      =   models.CharField(max_length=100,blank=True)
    amt_used                       =   models.CharField(max_length=100,blank=True)
    treatment_history              =   models.CharField(max_length=100,blank=True)
    #A separate card
    Disposition                    =   models.CharField(max_length=100,blank=True)
    Recommendation                 =   models.CharField(max_length=100,blank=True)
    Dx                             =   models.CharField(max_length=100,blank=True)
    client_meets_criteria_for      =   models.CharField(max_length=100,blank=True)
    Option_1                       =   models.CharField(max_length=100,choices=option1,blank=True)
    other_Option_1                 =   models.CharField(max_length=100,blank=True)
    Option_2                       =   models.CharField(max_length=100,choices=option2,blank=True)
    other_Option_2                 =   models.CharField(max_length=100,blank=True)
    Option_3                       =   models.CharField(max_length=100,choices=option3,blank=True)
    other_Option_3                 =   models.CharField(max_length=100,blank=True)
    Option_4                       =   models.CharField(max_length=100,choices=option4,blank=True)
    other_Option_4                 =   models.CharField(max_length=100,blank=True)
    no_further_services_needed     =   models.CharField(max_length=100,choices=choice,blank=True)
    referral_to                    =   models.CharField(max_length=100,choices=referal,blank=True) 
    other_referral                 =   models.CharField(max_length=100,blank=True)  
    recommended_program            =   models.CharField(max_length=100,blank=True)
    Further_Evaluation             =   models.CharField(max_length=100,blank=True)
    Intake_Appointment             =   models.DateTimeField(blank=True,null=True)
    Intake_Appointment_counselor   =   models.CharField(max_length=100,blank=True)
    Intake_Appointment_apt_kept    =   models.CharField(max_length=100,choices=choice,blank=True)
    Rescheduled                    =   models.DateTimeField(blank=True,null=True)
    Rescheduled_counselor          =   models.CharField(max_length=100,blank=True)
    Rescheduled_apt_kept           =   models.CharField(max_length=100,choices=choice,blank=True)
    ########
    Counselor_Name                 =   models.CharField(max_length=100,blank=True)
    Date1                           =   models.DateField(blank=True,null=True)                      
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural= 'HRRS_INTAKE_SCREEN'


class DAST(models.Model):
    user                           =   models.ForeignKey(User,on_delete=models.CASCADE)    
    Have_you_used_drugs_other_than_those_required_for_medical_reasons           =   models.CharField(max_length=100,choices=choice,db_column='Have_you_used_drugs_other_than_those_required_for_medical_reasons',blank=True)
    Have_you_abused_prescription_drugs                                          =   models.CharField(max_length=100,choices=choice,blank=True)
    Do_you_abuse_more_than_one_drug_at_a_time                                   =   models.CharField(max_length=100,choices=choice,blank=True)
    Can_you_get_through_the_week_without_using_drugs                            =   models.CharField(max_length=100,choices=choice,db_column='Can_you_get_through_the_week_without_using_drugs',blank=True)
    Are_you_always_able_to_stop_using_drugs_when_you_want_to                    =   models.CharField(max_length=100,choices=choice,blank=True)
    Do_you_abuse_drugs_on_a_continuous_basis                                    =   models.CharField(max_length=100,choices=choice,blank=True)
    Do_you_try_to_limit_your_drug_use_to_certain_situations                     =   models.CharField(max_length=100,choices=choice,blank=True)
    Have_you_had_blackouts_or_flashbacks_as_a_result_of_drug_use                =   models.CharField(max_length=100,choices=choice,blank=True)
    Do_you_ever_feel_bad_about_your_drug_abuse                                  =   models.CharField(max_length=100,choices=choice,blank=True)
    Does_your_spouse_or_parents_ever_complain_about_your_involvement_with_drugs =   models.CharField(max_length=100,choices=choice,db_column='Does_your_spouse_or_parents_ever_complain_about_your_involvement_with_drugs',blank=True)
    Do_your_friends_or_relatives_know_or_suspect_you_abuse_drugs                =   models.CharField(max_length=100,choices=choice,db_column='Do_your_friends_or_relatives_know_or_suspect_you_abuse_drugs',blank=True)
    Has_drug_abuse_ever_created_problems_between_you_and_your_spouse            =   models.CharField(max_length=100,choices=choice,db_column='Has_drug_abuse_ever_created_problems_between_you_and_your_spouse',blank=True)
    Has_any_family_member_ever_sought_help_for_problems_related_to_your_drug_use=   models.CharField(max_length=100,choices=choice,db_column='Has_any_family_member_ever_sought_help_for_problems_related_to_your_drug_use',blank=True)
    Have_you_ever_lost_friends_because_of_your_use_of_drugs                     =   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_lost_friends_because_of_your_use_of_drugs',blank=True)
    Have_you_ever_neglected_your_family_or_missed_work_because_of_your_use_of_drugs=   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_neglected_your_family_or_missed_work_because_of_your_use_of_drugs',blank=True)
    Have_you_ever_been_in_trouble_at_work_because_of_drug_abuse                 =   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_been_in_trouble_at_work_because_of_drug_abuse',blank=True)
    Have_you_ever_lost_a_job_because_of_drug_abuse                              =   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_lost_a_job_because_of_drug_abuse',blank=True)
    Have_you_gotten_into_fights_when_under_the_influence_of_drugs               =   models.CharField(max_length=100,choices=choice,db_column='Have_you_gotten_into_fights_when_under_the_influence_of_drugs',blank=True)
    Have_you_ever_been_arrested_because_of_unusual_behavior_while_under_the_influence_of_drugs=   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_been_arrested_because_of_unusual_behavior_while_under_the_influence_of_drugs',blank=True)
    Have_you_ever_been_arrested_for_driving_while_under_the_influence_of_drugs  =   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_been_arrested_for_driving_while_under_the_influence_of_drugs',blank=True)
    Have_you_engaged_in_illegal_activities_in_order_to_obtain_drug              =   models.CharField(max_length=100,choices=choice,db_column='Have_you_engaged_in_illegal_activities_in_order_to_obtain_drug',blank=True)
    Have_ou_ever_been_arrested_for_possession_of_illegal_drugs                  =   models.CharField(max_length=100,choices=choice,db_column='Have_ou_ever_been_arrested_for_possession_of_illegal_drugs',blank=True)
    Have_you_ever_experienced_withdrawal_symptoms_as_a_result_of_heavy_drug_intake=   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_experienced_withdrawal_symptoms_as_a_result_of_heavy_drug_intake',blank=True)
    Have_you_had_medical_problems_as_a_result_of_your_drug_use                  =   models.CharField(max_length=100,choices=choice,db_column='Have_you_had_medical_problems_as_a_result_of_your_drug_use',blank=True)
    Have_you_ever_gone_to_anyone_for_help_for_a_drug_problem                    =   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_gone_to_anyone_for_help_for_a_drug_problem',blank=True)
    Have_you_ever_been_in_a_hospital_for_medical_problems_related_to_your_drug_use=   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_been_in_a_hospital_for_medical_problems_related_to_your_drug_use',blank=True)
    Have_you_ever_been_involved_in_a_treatment_program_specifically_related_to_drug_use =   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_been_involved_in_a_treatment_program_specifically_related_to_drug_use',blank=True)
    Have_you_been_treated_as_an_outpatient_for_problems_related_to_drug_abuse   =   models.CharField(max_length=100,choices=choice,db_column='Have_you_been_treated_as_an_outpatient_for_problems_related_to_drug_abuse',blank=True)
    class Meta:
        verbose_name_plural= 'DAST'

class MAST(models.Model):
    user                           =   models.ForeignKey(User,on_delete=models.CASCADE)    
    Do_you_enjoy_drinking_now_and_then   =   models.CharField(max_length=100,choices=choice,blank=True)
    Do_you_feel_you_are_a_normal_drinker  =   models.CharField(max_length=100,choices=choice,blank=True)
    Have_you_ever_awakened_the_morning_after_some_drinking_the_night_before_and_found_that_you_could_not_remember_a_part_of_the_evening =   models.CharField(max_length=100,choices=choice,db_column="Have_you_ever_awakened_the_morning_after_some_drinking_the_night_before_and_found_that_you_could_not_remember_a_part_of_the_evening",blank=True)
    Does_your_wife_husband_a_parent_or_other_near_relative_ever_worry_or_complain_about_your_drinking =   models.CharField(max_length=100,choices=choice,db_column='Does_your_wife_husband_a_parent_or_other_near_relative_ever_worry_or_complain_about_your_drinking',blank=True)
    Can_you_stop_drinking_without_a_struggle_after_one_or_two_drinks =   models.CharField(max_length=100,choices=choice,db_column='Can_you_stop_drinking_without_a_struggle_after_one_or_two_drinks',blank=True)
    Do_you_ever_feel_guilty_about_your_drinking =   models.CharField(max_length=100,choices=choice,db_column='Do_you_ever_feel_guilty_about_your_drinking',blank=True)
    Do_friends_or_relatives_think_you_are_a_normal_drinker =   models.CharField(max_length=100,choices=choice,blank=True)
    Are_you_able_to_stop_drinking_when_you_want_to =   models.CharField(max_length=100,choices=choice,blank=True)
    Have_you_ever_attended_a_meeting_of_Alcoholics_Anonymous_AA =   models.CharField(max_length=100,choices=choice,blank=True)
    Have_you_gotten_into_physical_fights_when_drinking =   models.CharField(max_length=100,choices=choice,blank=True)
    Has_you_drinking_ever_created_problems_between_you_and_your_wife_husband_a_parent_or_other_relative =   models.CharField(max_length=100,choices=choice,db_column='Has_you_drinking_ever_created_problems_between_you_and_your_wife_husband_a_parent_or_other_relative',blank=True)
    Has_your_wife_husband_or_other_family_members_ever_gone_to_anyone_for_help_about_your_drinking =   models.CharField(max_length=100,choices=choice,db_column='Has_your_wife_husband_or_other_family_members_ever_gone_to_anyone_for_help_about_your_drinking',blank=True)
    Have_you_ever_lost_friends_because_of_your_drinking =   models.CharField(max_length=100,choices=choice,blank=True)
    Have_you_ever_gotten_into_trouble_at_work_or_school_because_of_drinking =   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_gotten_into_trouble_at_work_or_school_because_of_drinking',blank=True)
    Have_you_ever_lost_a_job_because_of_drinking =   models.CharField(max_length=100,choices=choice,blank=True)
    Have_you_ever_neglected_your_obligation_your_family_or_your_work_for_two_or_more_days_in_a_row_because_you_were_drinking =   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_neglected_your_obligation_your_family_or_your_work_for_two_or_more_days_in_a_row_because_you_were_drinking',blank=True)
    Do_you_drink_before_noon_fairly_often =   models.CharField(max_length=100,choices=choice,blank=True)
    Have_you_ever_been_told_you_have_liver_troubl_Cirrhosis =   models.CharField(max_length=100,choices=choice,blank=True)
    After_heavy_drinking_have_you_ever_had_Delirium_Tremens_D_T_s_or_severe_shakin_or_heard_voices_or_seen_things_that_are_really_not_there =   models.CharField(max_length=100,choices=choice,db_column='After_heavy_drinking_have_you_ever_had_Delirium_Tremens__D_T_s__or_severe_shakin_or_heard_voices_or_seen_things_that_are_really_not_there',blank=True)
    Have_you_ever_gone_to_anyone_for_help_about_your_drinking =   models.CharField(max_length=100,choices=choice,blank=True)
    Have_you_ever_been_in_a_hospital_because_of_drinking =   models.CharField(max_length=100,choices=choice,blank=True)
    Have_you_ever_been_a_patient_in_a_psychiatric_hospital_or_on_a_psychiatric_ward_of_a_general_hospital_where_drinking_was_part_of_the_problem_that_resulted_in_hospitalization =   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_been_a_patient_in_a_psychiatric_hospital_or_on_a_psychiatric_ward_of_a_general_hospital_where_drinking_was_part_of_the_problem_that_resulted_in_hospitalization',blank=True)
    Have_you_ever_been_seen_at_a_psychiatric_or_mental_health_clinic_orgone_to_any_doctor_social_worker_or_clergyman_for_help_with_anyemotional_problem_where_drinking_was_part_of_the_problem =   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_been_seen_at_a_psychiatric_or_mental_health_clinic_orgone_to_any_doctor_social_worker_or_clergyman_for_help_with_anyemotional_problem_where_drinking_was_part_of_the_problem',blank=True)
    Have_you_ever_been_arrested_for_drunk_driving_driving_whileintoxicated_or_driving_under_the_influence_of_alcoholic_beverages =   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_been_arrested_for_drunk_driving_driving_whileintoxicated_or_driving_under_the_influence_of_alcoholic_beverages',blank=True)
    Have_you_ever_been_arrested_or_taken_into_custody_even_for_a_few_hours_because_of_other_drunk_behavior =   models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_been_arrested_or_taken_into_custody_even_for_a_few_hours_because_of_other_drunk_behavior',blank=True)
    class Meta:
        verbose_name_plural= 'MAST'

class SOGS(models.Model):
    user                           =   models.ForeignKey(User,on_delete=models.CASCADE)    
    played_cards_for_money = models.CharField(max_length=100,choices=choice1,blank=True)
    other_played_cards_for_money                =   models.CharField(max_length=100,blank=True)
    bet_on_horses_dogs_or_other_animals_infftrack_betting_at_the_track_or_with_a_bookie= models.CharField(max_length=100,choices=choice1,db_column='bet_on_horses_dogs_or_other_animals_infftrack_betting_at_the_track_or_with_a_bookie',blank=True)
    other_Option_1                =   models.CharField(max_length=100,blank=True)
    bet_on_sports_parley_cards_with_a_bookie_or_at_jai_alai= models.CharField(max_length=100,choices=choice1,blank=True)
    other_Option_2                =   models.CharField(max_length=100,blank=True)
    played_dice_games_including_craps_over_and_under_or_other_dice_games_for_money= models.CharField(max_length=100,choices=choice1,db_column='played_dice_games_including_craps_over_and_under_or_other_dice_games_for_money',blank=True)
    other_Option_3                =   models.CharField(max_length=100,blank=True)
    went_to_casino_legal_or_otherwise= models.CharField(max_length=100,choices=choice1,blank=True)
    other_Option_4                =   models.CharField(max_length=100,blank=True)
    played_the_numbers_or_bet_on_lotteries= models.CharField(max_length=100,choices=choice1,blank=True)
    other_Option_5                =   models.CharField(max_length=100,blank=True)
    played_bingo= models.CharField(max_length=100,choices=choice1,blank=True)
    other_Option_6                =   models.CharField(max_length=100,blank=True)
    played_the_stock_and_or_commodities_market= models.CharField(max_length=100,choices=choice1,blank=True)
    other_Option_7                =   models.CharField(max_length=100,blank=True)
    played_slot_machines_poker_machines_or_other_gambling_machines= models.CharField(max_length=100,choices=choice1,db_column='played_slot_machines_poker_machines_or_other_gambling_machines',blank=True)
    other_Option_8                =   models.CharField(max_length=100,blank=True)
    bowled_shot_pool_played_golf_or_played_some_other_game_of_skill_for_money= models.CharField(max_length=100,choices=choice1,db_column='_played_golf_or_played_some_other_game_of_skill_for_money',blank=True)
    other_Option_9                =   models.CharField(max_length=100,blank=True)
    What_is_the_largest_amount_of_money_you_have_ever_gambled_with_any_one_day= models.CharField(max_length=100,choices=choice2,db_column='What_is_the_largest_amount_of_money_you_have_ever_gambled_with_any_one_day',blank=True)
    other_Option_10                =   models.CharField(max_length=100,blank=True)
    Do_your_parents_have_a_gambling_problem = models.CharField(max_length=100,choices=choice3,blank=True)
    other_Option_11                =   models.CharField(max_length=100,blank=True)
    When_you_gamble_how_often_do_you_go_back_another_day_to_win_back_money_you_lost = models.CharField(max_length=100,choices=choice4,db_column='When_you_gamble_how_often_do_you_go_back_another_day_to_win_back_money_you_lost',blank=True)
    other_Option_12                =   models.CharField(max_length=100,blank=True)
    Have_you_ever_claimed_to_be_winning_money_gambling_but_werent_really_In_fact_you_lost= models.CharField(max_length=100,choices=choice5,db_column='Have_you_ever_claimed_to_be_winning_money_gambling_but_weren’t_really_In_fact_you_lost',blank=True)
    other_Option_13                =   models.CharField(max_length=100,blank=True)
    Do_you_feel_you_have_ever_had_a_problem_with_gambling= models.CharField(max_length=100,choices=choice6,blank=True)
    other_Option_14                =   models.CharField(max_length=100,blank=True)
    Did_you_ever_gamble_more_than_you_intended= models.CharField(max_length=100,choices=choice,blank=True)
    other_Option_15                =   models.CharField(max_length=100,blank=True)
    Have_people_criticized_your_gambling= models.CharField(max_length=100,choices=choice,blank=True)
    Have_you_ever_felt_guilty_about_the_way_you_gamble_or_what_happens_when_you_gamble=models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_felt_guilty_about_the_way_you_gamble_or_what_happens_when_you_gamble',blank=True)
    Have_you_ever_felt_like_you_would_like_to_stopgambling_but_didnt_think_you_could= models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_felt_like_you_would_like_to_stopgambling_but_didnt_think_you_could',blank=True)
    Have_you_ever_hidden_betting_slips_lottery_tickets_gambling_money_or_other_signs_of_gambling_from_yourspouse_children_or_other_important_people_in_you_life= models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_hidden_betting_slips_lottery_tickets_gambling_money_or_other_signs_of_gambling_from_yourspouse_children_or_other_important_people_in_you_life',blank=True)
    Have_you_ever_argued_with_people_you_like_overhow_you_handle_money= models.CharField(max_length=100,choices=choice,db_column='Have_you_ever_argued_with_people_you_like_overhow_you_handle_money',blank=True)
    Have_money_arguments_ever_centered_on_your_gambling= models.CharField(max_length=100,choices=choice,blank=True)
    Have_you_ever_borrowed_from_someone_and_not_paid_them_back_as_a_result_of_your_gambling= models.CharField(max_length=100,blank=True,choices=choice,db_column='Have_you_ever_borrowed_from_someone_and_not_paid_them_back_as_a_result_of_your_gambling')
    Have_you_ever_lost_time_from_work_or_school_due_to_gambling= models.CharField(max_length=100,choices=choice,blank=True,db_column='Have_you_ever_lost_time_from_work_or_school_due_to_gambling')
    If_you_borrowed_money_to_gamble_or_to_pay_gambling_debts_then_you_borrowed_from_household_money       = models.CharField(max_length=100,blank=True,choices=choice,db_column='If_you_borrowed_money_to_gamble_or_to_pay_gambling_debts_then_you_borrowed_from_household_money')
    you_borrowed_from_your_spouse        = models.CharField(max_length=100,choices=choice,blank=True)
    you_borrowed_from_other_relatives_or_inlaws       = models.CharField(max_length=100,choices=choice,blank=True)
    you_borrowed_from_banks_or_loan_companies_or_credit_unions   = models.CharField(max_length=100,choices=choice,blank=True)
    you_borrowed_from_credit_cards        = models.CharField(max_length=100,choices=choice,blank=True)
    you_borrowed_from_loan_sharks=models.CharField(max_length=100,choices=choice,blank=True)
    you_borrowed_from_your_cashed_in_stocks_bonds_or_other_securities    =models.CharField(max_length=100,choices=choice,db_column='you_borrowed_from_your_cashed_in_stocks_bonds_or_other_securities',blank=True)
    you_borrowed_from_you_sold_personal_or_family_property  =models.CharField(max_length=100,choices=choice,blank=True)
    you_borrowed_from_you_borrowed_on_your_checking_account=models.CharField(max_length=100,choices=choice,blank=True)
    you_borrowed_from_you_have_a_credit_line_with_a_bookie=models.CharField(max_length=100,choices=choice,blank=True)
    you_borrowed_from_you_have_a_credit_line_with_a_casino=models.CharField(max_length=100,choices=choice,blank=True)
    class Meta:
        verbose_name_plural= 'SOGS'

class  HRRS_RECORD_RELEASE_AUTHORIZATION(models.Model):
    user    =   models.ForeignKey(User,on_delete=models.CASCADE)    
    Address = models.CharField(max_length=300,blank=True)
    Phone = models.CharField(max_length=300,blank=True)
    Clinet_Name = models.CharField(max_length=300,blank=True)
    Date_of_Birth = models.DateField(blank=True,null=True)
    Precious_name = models.CharField(max_length=300,blank=True)
    SSN_number= models.CharField(max_length=300,blank=True)
    Authorizator_Name= models.CharField(max_length=300,blank=True)
    Patient_Name= models.CharField(max_length=300,blank=True)
    Patient_Address= models.CharField(max_length=300,blank=True)
    Patient_city= models.CharField(max_length=300,blank=True)
    Patient_state= models.CharField(max_length=300,blank=True)
    Patient_zipcode= models.CharField(max_length=300,blank=True)
    This_request_and_authorization_apply_to= models.CharField(max_length=300,blank=True)
    Healthcare_information_relating_to_the_following_treatment_or_condition_or_dates= models.CharField(max_length=300,blank=True,db_column='Healthcare_information_relating_to_the_following_treatment_or_condition_or_dates')
    other= models.CharField(max_length=300,blank=True)
    class Meta:
            verbose_name_plural= 'HRRS_RECORD_RELEASE_AUTHORIZATION'

class Initial_Treatment_Plan(models.Model):
    user   =   models.ForeignKey(User,on_delete=models.CASCADE)    
    Date= models.DateField(blank=True,null=True)
    Review_Date= models.DateField(blank=True,null=True)
    Master_Treatment_Plan= models.CharField(max_length=300,choices=choice7,blank=True)
    Patient_Name= models.CharField(max_length=300,blank=True)
    DSM_V_CODE= models.CharField(max_length=300,choices=option2,blank=True)
    other_DSM_V_CODE= models.CharField(max_length=300,blank=True)
    Diagnosis=  models.CharField(max_length=300,choices=option4,blank=True)
    other_Diagnosis= models.CharField(max_length=300,blank=True)
    # DSM_V_CODE_2= models.CharField(max_length=300)
    # Diagnosis_2=  models.CharField(max_length=300)
    # DSM_V_CODE_3= models.CharField(max_length=300)
    # Diagnosis_3= models.CharField(max_length=300)
    # DSM_V_CODE_4= models.CharField(max_length=300)
    # Diagnosis_4= models.CharField(max_length=300)
    # DSM_V_CODE_5= models.CharField(max_length=300)
    # Diagnosis_5= models.CharField(max_length=300)
    Strengths= models.CharField(max_length=300,choices=strength,blank=True)
    other_strength =   models.CharField(max_length=100,blank=True)  
    Stressors= models.CharField(max_length=300,choices=stressor,blank=True)
    other_Stressors= models.CharField(max_length=300,blank=True)
    Barriers= models.CharField(max_length=300,choices=barrier,blank=True)
    other_Barriers= models.CharField(max_length=300,blank=True)
    Discharge_Date=   models.DateField(blank=True,null=True)
    Discharge_No= models.CharField(max_length=300,blank=True)
    Problems_of_Patient_1= models.CharField(max_length=300,choices=problem1,blank=True)
    other_Option_1= models.CharField(max_length=100,blank=True)
    Problems_of_Patient_2= models.CharField(max_length=300,choices=problem2,blank=True)
    other_Option_2= models.CharField(max_length=100,blank=True)
    Problems_of_Patient_3= models.CharField(max_length=300,choices=problem3,blank=True)
    other_Option_3= models.CharField(max_length=100,blank=True)
    Problems_of_Patient_4= models.CharField(max_length=300,choices=problem4,blank=True)
    other_Option_4= models.CharField(max_length=100,blank=True)
    Longterm_Goals_for_Discharge_1= models.CharField(max_length=300,choices=longterm,blank=True)
    other_Option_5= models.CharField(max_length=100,blank=True)
    Longterm_Goals_for_Discharge_2= models.CharField(max_length=300,choices=longterm1,blank=True)
    other_Option_6= models.CharField(max_length=100,blank=True)
    Longterm_Goals_for_Discharge_3= models.CharField(max_length=300,choices=longterm2,blank=True)
    other_Option_7= models.CharField(max_length=100,blank=True)
    Longterm_Goals_for_Discharge_4= models.CharField(max_length=300,choices=longterm3,blank=True)
    other_Option_8= models.CharField(max_length=100,blank=True)
    Shortterm_Goals_for_Discharge= models.CharField(max_length=300,blank=True)
    Therapeutic_Intervention_for_Discharge= models.CharField(max_length=300,blank=True)
    client= models.CharField(max_length=300,blank=True)
    clinician= models.CharField(max_length=300,blank=True)
    Clinical_Supervisor= models.CharField(max_length=300,blank=True)
    class Meta:
            verbose_name_plural= 'Initial_Treatment_Plan'

class HRRS_PROGRESS_NOTE(models.Model):
    user         =   models.ForeignKey(User,on_delete=models.CASCADE)    
    Clinet_Name  =               models.CharField(max_length=300,blank=True)
    Date    =                    models.DateField(blank=True,null=True)
    Time    =                    models.TimeField(blank=True)
    Session_Type=                models.CharField(max_length=300,choices=session,blank=True)
    other_session =                     models.CharField(max_length=100,blank=True)  
    Type_of_group=               models.CharField(max_length=300,choices=group,blank=True)
    other_group =                     models.CharField(max_length=100,blank=True)  
    Topic_of_Discussion=         models.CharField(max_length=300,choices=topic,blank=True)
    other_topic=                       models.CharField(max_length=100,blank=True)  
    Discussion=                  models.CharField(max_length=300,blank=True)
    Acute     =                  models.CharField(max_length=300,choices=acute,blank=True)
    other_acute =                models.CharField(max_length=100,blank=True)  
    intoxication=                models.CharField(max_length=300,blank=True)
    Biomedical     =             models.CharField(max_length=300,choices=acute,blank=True)
    other_biomedical =                     models.CharField(max_length=100,blank=True)  
    conditions=                  models.CharField(max_length=300,blank=True)
    Emotional_or_Behavioral =    models.CharField(max_length=300,choices=acute,blank=True)
    other_emotional =                     models.CharField(max_length=100,blank=True)  
    conditions_1=                models.CharField(max_length=300,blank=True)
    Resistance=                  models.CharField(max_length=300,choices=acute,blank=True)
    other_resistance =                     models.CharField(max_length=100,blank=True)  
    Relapse_Potential=           models.CharField(max_length=300,choices=acute,blank=True)
    other_relapse_potential =    models.CharField(max_length=100,blank=True)  
    Thought_Process=             models.CharField(max_length=300,choices=thought,blank=True)
    other_thought =                     models.CharField(max_length=100,blank=True)  
    Mood=                        models.CharField(max_length=300,choices=mood,blank=True)
    other_mood=                       models.CharField(max_length=100,blank=True)  
    Oriented_x_3=                models.CharField(max_length=300,choices=choice,blank=True)
    if_no_explain=               models.CharField(max_length=300,blank=True)
    DX=                          models.CharField(max_length=300,choices=dx,blank=True)
    other_DX =                     models.CharField(max_length=100,blank=True)  
    Shared_Feelings=             models.CharField(max_length=300,choices=choice,blank=True)
    Open_to_feedbacks=           models.CharField(max_length=300,choices=choice,blank=True)
    List_Treatment_Plan_Objectives_Discussed= models.CharField(max_length=300,choices=list_objective,blank=True)
    Made_Progress_in_Meeting= models.CharField(max_length=300,choices=choice,blank=True)
    if_no_explain1=               models.CharField(max_length=300,blank=True)
    Treatment_Plan_Objectives= models.CharField(max_length=300,blank=True)
    Appeared_to_Benefit_from_the_Session=models.CharField(max_length=300,choices=choice,blank=True)
    Clinician_Name=  models.CharField(max_length=300,blank=True)
    Clinician_Title=   models.CharField(max_length=300,blank=True)
    class Meta:
        verbose_name_plural= 'HRRS_PROGRESS_NOTE'
                                    
                    

class HRRS_DISCHARGE_PLANNING(models.Model):
    user                                    =   models.ForeignKey(User,on_delete=models.CASCADE)    
    Clinet_Name                             = models.CharField(max_length=300,blank=True)
    Date_of_Birth                           = models.CharField(max_length=300,blank=True)
    Date_of_Admission                       = models.CharField(max_length=300,blank=True)
    Date_of_Projected_Discharge             = models.CharField(max_length=300,blank=True)
    Acute_Intoxication_or_Withdrawal        = models.CharField(max_length=300,choices=choice8,blank=True)
    other_Option_1                          = models.CharField(max_length=300,blank=True)
    Biomedical_Conditions_or_Complications  = models.CharField(max_length=300,choices=choice8,blank=True)
    other_Option_2                          = models.CharField(max_length=300,blank=True)
    Emotional_or_Behavioral                 = models.CharField(max_length=300,choices=choice8,blank=True)
    other_Option_3                          = models.CharField(max_length=300,blank=True)
    Conditions_or_Complications             = models.CharField(max_length=300,choices=choice8,blank=True)
    other_Option_4                          = models.CharField(max_length=300,blank=True)
    Treatment_Acceptance_or_Resistance      = models.CharField(max_length=300,choices=choice8,blank=True)
    other_Option_5                          = models.CharField(max_length=300,blank=True)
    Relapse_Potential                       = models.CharField(max_length=300,choices=choice8,blank=True)
    other_Option_6                          = models.CharField(max_length=300,blank=True)                                                                                                     
    Recovery_Environment                    = models.CharField(max_length=300,choices=choice8,blank=True)
    other_Option_7                          = models.CharField(max_length=300,blank=True)

    History_Physical_or_Sexual_or_Emotional_Abuse   = models.CharField(max_length=300,blank=True)
    Family_issues                                   = models.CharField(max_length=300,blank=True)
    Educational_issues                              = models.CharField(max_length=300,blank=True)
    Financial_issues                                = models.CharField(max_length=300,blank=True)            
    Legal_issues                                    = models.CharField(max_length=300,blank=True)
    Spiritiual_issues                               = models.CharField(max_length=300,blank=True)    
    Medical_isses                                   = models.CharField(max_length=300,blank=True)            
    Psychatric_issues                               = models.CharField(max_length=300,blank=True)    
    Recommendations                                 = models.CharField(max_length=300,blank=True)
    Diagnosis                                       = models.CharField(max_length=300,blank=True)
    DSM_V                                           = models.CharField(max_length=300,blank=True)
    class Meta:
            verbose_name_plural= 'HRRS_DISCHARGE_PLANNING'




Insurance_Type_choices = (
    ('None', 'None'),
    ('MyHealthLA', 'MyHealthLA'),
    ('Medicare', 'Medicare'),
    ('Medi-Cal', 'Medi-Cal'),
    ('Private', 'Private'),
    ('Other', 'Other'),
    ('Unknown', 'Unknown')
)

Living_Arrangement_choices = (
    ('Homeless', 'Homeless'),
    ('Independent living', 'Independent living'),
    ('Other', 'Other'),
    ('Unknown', 'Unknown')
)

SEVERITY_RATING = (
    ('0', 'None'),
    ('1', 'Mild'),
    ('2', "Moderate"),
    ('3', 'Severe'),
    ('4', 'Very Severe'),
    ('5', 'NULL')
)

CHOICES_TYPE_4 = (
    ('0', 'None'),
    ('1', 'Yes'),
    ('2', "No"),
    ('3', 'Not Sure'),
)


CHOICES_TYPE_3 = (
    ('0', 'None'),
    ('1', 'Yes'),
    ('2', "No"),

)

CHOICES_TYPE_2 = (
    ('0', 'None'),
    ('1', 'Slightly'),
    ('2', 'Moderately'),
    ('3', 'Considerably'),
    ('4', 'Extremely'),
    ('5', 'Not at all')

)

CHOICES_TYPE_1 = (
    ('0', 'None'),
    ('1', 'Occasionally'),
    ('2', 'Frequently'),
    ('3', 'Constantly'),
    ('4', 'NULL')
)


CHOICES_TYPE_0 = (
    ('0', 'Unknown'),
    ('1', 'None'),
    ('2', 'Mild'),
    ('3', 'Moderate'),
    ('4', 'Severe')
)


CHOICES_TYPE_0_SEVERITY = (
    ('0', 'Unknown'),
    ('1', 'None'),
    ('2', 'Mild'),
    ('3', 'Moderate'),
    ('4', 'Severe')
)



class chartReviewTool(models.Model):
    user                           =   models.ForeignKey(User,on_delete=models.CASCADE)    
    clientName = models.CharField(
        max_length=50,  db_column="Client Name")
    level_1 = models.BooleanField(
        blank=True, default=False, db_column="Level 1")
    level_2 = models.BooleanField(
        blank=True, default=False, db_column="Level 2")
    admitDate = models.DateField(
        blank=True, db_column="Admit Date", null=True)
    openChart_1 = models.BooleanField(
        default=False, blank=True, verbose_name="Open Chart 1")
    openChart_2 = models.BooleanField(
        default=False, blank=True, verbose_name="Open Chart 2")
    reviewDate = models.DateField(
        blank=True, verbose_name="Review Date", null=True)
    reviewedBy = models.CharField(
        max_length=50, blank=True, verbose_name="Reviewed By")
    stampDate = models.DateField(blank=True, verbose_name="Date", null=True)

    # Section No.1.............
    screening_or_intake_form_complete = models.BooleanField(
        blank=True,  default=False, db_column="Screening/Intake Form Complete")
    screening_or_intake_form_no_complete = models.BooleanField(
        blank=True,  default=False, db_column="Screening/Intake Form No Complete")
    screening_or_intake_form_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Screening/Intake Form None")
    screening_or_intake_form_comment = models.TextField(
        db_column="Screening/Intake Form Comment", blank=True)
    informed_consent_and_disclosure_complete = models.BooleanField(
        blank=True, default=False, verbose_name="Informed Consent and Disclosure Complete")
    informed_consent_and_disclosure_no_complete = models.BooleanField(
        blank=True, default=False, verbose_name="Informed Consent and Disclosure No Complete")
    informed_consent_and_disclosure_none = models.BooleanField(
        blank=True, default=False, verbose_name="Informed Consent and Disclosure None")
    informed_consent_and_disclosure_comment = models.TextField(
        verbose_name="Informed Consent and Disclosure Comment", blank=True)
    statement_of_confidentiality_complete = models.BooleanField(
        blank=True, default=False,  verbose_name="Statement of Confidentiality Complete")
    statement_of_confidentiality_no_complete = models.BooleanField(
        blank=True, default=False,  verbose_name="Statement of Confidentiality No Complete")
    statement_of_confidentiality_none = models.BooleanField(
        blank=True, default=False,  verbose_name="Statement of Confidentiality None")
    statement_of_confidentiality_comment = models.TextField(
        verbose_name="Statement of Confidentiality Comment", blank=True)
    bill_of_rights_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Bill of Rights Complete")
    bill_of_rights_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Bill of Rights No Complete")
    bill_of_rights_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Bill of Rights None")
    bill_of_rights_comment = models.TextField(
        verbose_name="Bill of Rights Comment", blank=True)
    grievance_procedure_complete = models.BooleanField(
        blank=True, default=False, verbose_name="Grievance Procedure Complete")
    grievance_procedure_no_complete = models.BooleanField(
        blank=True, default=False, verbose_name="Grievance Procedure No Complete")
    grievance_procedure_none = models.BooleanField(
        blank=True, default=False, verbose_name="Grievance Procedure None")
    grievance_procedure_comment = models.TextField(
        verbose_name="Grievance Procedure Comment", blank=True)
    program_rules_complete = models.BooleanField(
        blank=True, default=False, verbose_name="Program Rules Complete")
    program_rules_no_complete = models.BooleanField(
        blank=True, default=False, verbose_name="Program Rules No Complete")
    program_rules_none = models.BooleanField(
        blank=True, default=False, verbose_name="Program Rules None")
    program_rules_comment = models.TextField(
        verbose_name="Program Rules Comment", blank=True)
    release_confidentiality_information_42_cfr_complete = models.BooleanField(
        blank=True, default=False, db_column="Release -Confidential Information    (42 CFR) Complete")
    release_confidentiality_information_42_cfr_no_complete = models.BooleanField(
        blank=True, default=False, verbose_name="Release -Confidential Information    (42 CFR) No Complete")
    release_confidentiality_information_42_cfr_none = models.BooleanField(
        blank=True, default=False, verbose_name="Release -Confidential Information    (42 CFR) None")
    release_confidentiality_information_42_cfr_comment = models.TextField(
        verbose_name="Release -Confidential Information    (42 CFR) Comment", blank=True)
    signature_page_complete = models.BooleanField(
        blank=True, default=False, verbose_name="Signature Page Complete")
    signature_page_no_complete = models.BooleanField(
        blank=True, default=False, verbose_name="Signature Page No Complete")
    signature_page_none = models.BooleanField(
        blank=True, default=False, verbose_name="Signature Page None")
    signature_page_comment = models.TextField(
        verbose_name="Signature Page Comment", blank=True)
    programe_schedule_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Program Schedule (signed copy) Complete")
    programe_schedule_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Program Schedule (signed copy) No Complete")
    programe_schedule_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Program Schedule (signed copy) None")
    programe_schedule_comment = models.TextField(
        verbose_name="Program Schedule (signed copy) Comment", blank=True)

    # Section No.2...................

    bioPsycolosocialAssessment_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Bio-Psychosocial Assessment Complete")
    bioPsycolosocialAssessment_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Bio-Psychosocial Assessment no Complete")
    bioPsycolosocialAssessment_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Bio-Psychosocial Assessment None")
    bioPsycolosocialAssessment_comment = models.TextField(
        verbose_name="Bio-Psychosocial Assessment Comment", blank=True)
    sogs_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="SOGS Complete")
    sogs_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="SOGS No Complete")
    sogs_none = models.BooleanField(
        blank=True,  default=False, verbose_name="SOGS None")
    sogs_commeent = models.TextField(blank=True, verbose_name="SOGS Comment")
    NJSAMS_ASI_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="NJSAMS/ASI Complete")
    NJSAMS_ASI_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="NJSAMS/ASI No Complete")
    NJSAMS_ASI_none = models.BooleanField(
        blank=True,  default=False, verbose_name="NJSAMS/ASI None")
    NJSAMS_ASI_comment = models.TextField(
        blank=True, verbose_name="NJSAMS/ASI Comment")
    dast_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="DAST Complete")
    dast_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="DAST No Complete")
    dast_none = models.BooleanField(
        blank=True,  default=False, verbose_name="DAST None")
    dast_comment = models.TextField(blank=True, verbose_name="DAST Comment")
    MAST_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="MAST Complete")
    MAST_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="MAST No Complete")
    MAST_none = models.BooleanField(
        blank=True,  default=False, verbose_name="MAST None")
    MAST_comment = models.TextField(blank=True, verbose_name="MAST Comment")
    Psychiatric_Evaluation_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Psychiatric Evaluation (if applicable) Complete")
    Psychiatric_Evaluation_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Psychiatric Evaluation (if applicable) No Complete")
    Psychiatric_Evaluation_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Psychiatric Evaluation (if applicable) None")
    Psychiatric_Evaluation_comment = models.TextField(
        blank=True, verbose_name="Psychiatric Evaluation (if applicable) Comment")

    # Section No.3
    Initial_Treatment_Plan_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Initial Treatment Plan Complete")
    Initial_Treatment_Plan_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Initial Treatment Plan No Complete")
    Initial_Treatment_Plan_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Initial Treatment Plan None")
    Initial_Treatment_Plan_comment = models.TextField(
        blank=True, verbose_name="Initial Treatment Plan Comment")
    Updated_Treatment_Plan_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Updated Treatment Plan Complete")
    Updated_Treatment_Plan_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Updated Treatment Plan No Complete")
    Updated_Treatment_Plan_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Updated Treatment Plan None")
    Updated_Treatment_Plan_comment = models.TextField(
        blank=True, verbose_name="Updated Treatment Plan Comment")
    Discharge_Summary_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Discharge Summary Complete")
    Discharge_Summary_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Discharge Summary No Complete")
    Discharge_Summary_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Discharge Summary None")
    Discharge_Summary_comment = models.TextField(
        blank=True, verbose_name="Discharge Summary Comment")
    Individual_Group_Progress_Notes_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Individual/Group Progress Notes Complete")
    Individual_Group_Progress_Notes_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Individual/Group Progress Notes No Complete")
    Individual_Group_Progress_Notes_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Individual/Group Progress Notes None")
    Individual_Group_Progress_Notes_comment = models.TextField(
        blank=True, verbose_name="Individual/Group Progress Notes Comment")
    Individual_Group_Attendance_Sheet_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Individual/Group Attendance Sheet Complete")
    Individual_Group_Attendance_Sheet_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Individual/Group Attendance Sheet No Complete")
    Individual_Group_Attendance_Sheet_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Individual/Group Attendance Sheet None")
    Individual_Group_Attendance_Sheet_comment = models.TextField(
        blank=True, verbose_name="Individual/Group Attendance Sheet Comment")

    # Section No.4
    HIV_Counseling_Form_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="HIV Counseling Form Complete")
    HIV_Counseling_Form_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="HIV Counseling Form No Complete")
    HIV_Counseling_Form_none = models.BooleanField(
        blank=True,  default=False, verbose_name="HIV Counseling Form None")
    HIV_Counseling_Form_comment = models.TextField(
        blank=True, verbose_name="HIV Counseling Form Comment")
    TB_Testing_Form_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="TB Testing Form Complete")
    TB_Testing_Form_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="TB Testing Form No Complete")
    TB_Testing_Form_none = models.BooleanField(
        blank=True,  default=False, verbose_name="TB Testing Form None")
    TB_Testing_Form_comment = models.TextField(
        blank=True, verbose_name="TB Testing Form Comment")
    Medication_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Medication (If applicable) Complete")
    Medication_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Medication (If applicable) No Complete")
    Medication_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Medication (If applicable) None")
    Medication_comment = models.TextField(
        blank=True, verbose_name="Medication (If applicable) Comment")

    # Section No.5
    Urine_Drug_Screening_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Urine Drug Screening Complete")
    Urine_Drug_Screening_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Urine Drug Screening No Complete")
    Urine_Drug_Screening_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Urine Drug Screening None")
    Urine_Drug_Screening_comment = models.TextField(
        blank=True, verbose_name="Urine Drug Screening Comment")
    Other_complete_5 = models.BooleanField(
        blank=True,  default=False, verbose_name="Other Complete")
    Other_no_complete_5 = models.BooleanField(
        blank=True,  default=False, verbose_name="Other No Complete")
    Other_none_5 = models.BooleanField(
        blank=True,  default=False, verbose_name="Otherg None")
    Other_comment_5 = models.TextField(
        blank=True, verbose_name="Other Comment")

    # Section No.6
    Drug_Court_reports_SAI_IDRC_DUII_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Drug Court reports, SAI, IDRC/DUII Complete")
    Drug_Court_reports_SAI_IDRC_DUII_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Drug Court reports, SAI, IDRC/DUII No Complete")
    Drug_Court_reports_SAI_IDRC_DUII_none = models.BooleanField(
        blank=True,  default=False, verbose_name="ODrug Court reports, SAI, IDRC/DUII None")
    Drug_Court_reports_SAI_IDRC_DUII_comment = models.TextField(
        blank=True, verbose_name="Drug Court reports, SAI, IDRC/DUII Comment")
    Probation_Parole_ISP_DFSetc_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Probation, Parole, ISP, DFSetc Complete")
    Probation_Parole_ISP_DFSetc_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Probation, Parole, ISP, DFSetc No Complete")
    Probation_Parole_ISP_DFSetc_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Probation, Parole, ISP, DFSetc None")
    Probation_Parole_ISP_DFSetc_comment = models.TextField(
        blank=True, verbose_name="Probation, Parole, ISP, DFSetc Comment")

    # Section No.7
    Audit_Forms_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Audit Forms Complete")
    Audit_Forms_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Audit Forms No Complete")
    Audit_Forms_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Audit Forms None")
    Audit_Forms_comment = models.TextField(
        blank=True, verbose_name="Audit Forms Comment")
    Supervision_Notes_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Supervision Notes Complete")
    Supervision_Notes_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Supervision Notes No Complete")
    Supervision_Notes_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Supervision Notes None")
    Supervision_Notes_comment = models.TextField(
        blank=True, verbose_name="Supervision Notes Comment")
    Other_complete_7 = models.BooleanField(
        blank=True,  default=False, verbose_name="Other Complete")
    Other_no_complete_7 = models.BooleanField(
        blank=True,  default=False, verbose_name="Other No Complete")
    Other_none_7 = models.BooleanField(
        blank=True,  default=False, verbose_name="Other None")
    Other_comment_7 = models.TextField(
        blank=True, verbose_name="Other Comment")

    # Section No.8
    Client_Survey_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Client Survey (30, 60+90 days) Complete")
    Client_Survey_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="Client Survey (30, 60+90 days) No Complete")
    Client_Survey_none = models.BooleanField(
        blank=True,  default=False, verbose_name="Client Survey (30, 60+90 days) None")
    Client_Survey_comment = models.TextField(
        blank=True, verbose_name="Client Survey (30, 60+90 days) Comment")
    QA_Statistics_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="QA Statistics Complete")
    QA_Statistics_no_complete = models.BooleanField(
        blank=True,  default=False, verbose_name="QA Statistics No Complete")
    QA_Statistics_none = models.BooleanField(
        blank=True,  default=False, verbose_name="QA Statistics None")
    QA_Statistics_comment = models.TextField(
        blank=True, verbose_name="QA Statistics Comment")
    Other_complete_8 = models.BooleanField(
        blank=True,  default=False, verbose_name="Other Complete")
    Other_no_complete_8 = models.BooleanField(
        blank=True,  default=False, verbose_name="Other No Complete")
    Other_none_8 = models.BooleanField(
        blank=True,  default=False, verbose_name="Other None")
    Other_comment_8 = models.TextField(
        blank=True, verbose_name="Other Comment")

    def __str__(self):
        return "Chart Review Tool By {name}".format(name=self.reviewedBy)


class demoGraphicModel(models.Model):
    user                           =   models.ForeignKey(User,on_delete=models.CASCADE)    
# Page 1 ...
    name_page_1 = models.CharField(
        max_length=50, default='',  verbose_name='Name')
    date_page_1 = models.DateField(blank=True, verbose_name='Date', null=True)
    phoneNumber_page_1 = models.IntegerField(
        blank=True, verbose_name="Phone Number", null=True)
    voicemail_page_1 = models.BooleanField(
        blank=True, default=False, verbose_name="Okay to leave voicemail?")
    address_page_1 = models.TextField(
        max_length=100, verbose_name="Address", default='', blank=True)
    dateOfBirth_page_1 = models.DateField(
        blank=True, null=True, verbose_name="Date of Birth")
    age_page_1 = models.IntegerField(verbose_name="Age", blank=True, null=True)
    gender_page_1 = models.CharField(
        max_length=6, verbose_name="Gender", blank=True)
    Race_Ethnicity_page_1 = models.CharField(
        max_length=20, verbose_name="Race/Ethnicity", blank=True)
    Preferred_Language_page_1 = models.CharField(
        max_length=10, verbose_name="Preferred Language", blank=True)
    MediCalID_page_1 = models.CharField(
        max_length=10, verbose_name="Medi-Cal ID #:", blank=True)
    OtherID_page_1 = models.CharField(
        max_length=10, verbose_name="Other ID# (Plan):", blank=True)
    Insurance_Type_page_1 = models.CharField(
        blank=True, default='Unknown', verbose_name="Insurance Type", choices=Insurance_Type_choices, max_length=15)
    # Insurance_Type_MyHealthLA_page_1 = models.BooleanField(blank = True, default=False, verbose_name = "MyHealthLA")
    # Insurance_Type_Medicare_page_1 = models.BooleanField(blank = True, default=False, verbose_name = "Medicare")
    # Insurance_Type_MediCal_page_1 = models.BooleanField(blank = True, default=False, verbose_name = "Medi-Cal")
    # Insurance_Type_Private_page_1 = models.BooleanField(blank = True, default=False, verbose_name = "Private")
    # Insurance_Type_Other_page_1 = models.BooleanField(blank = True, default=False, verbose_name = "Other")
    Insurance_Type_plan_1_page_1 = models.CharField(
        blank=True, default='', verbose_name="(Plan):", max_length=20)
    Insurance_Type_plan_2_page_1 = models.CharField(
        blank=True, default='', verbose_name="(Plan):", max_length=20)
    Insurance_Type_plan_3_page_1 = models.CharField(
        blank=True, default='', verbose_name="(Plan):", max_length=20)
    Insurance_Type_plan_4_page_1 = models.CharField(
        blank=True, default='', verbose_name="(Plan):", max_length=20)
    Living_Arrangement_page_1 = models.CharField(
        blank=True, default='Unknown', verbose_name="Living Arrangement", choices=Living_Arrangement_choices, max_length=20)
    Living_Arrangement_plan_page_1 = models.CharField(
        blank=True, default='', verbose_name="Living Arrangement", max_length=30)
    Explanation_of_why_patient_is_currently_seeking_treatment = models.TextField(
        verbose_name="Explanation of why patient is currently seeking treatment",
        blank=True, max_length=150,
        default='')

    # Dimension No.1 ....
    Amphetamines_dim_1_Recently_Used = models.BooleanField(
        blank=True, default=False, verbose_name="Amphetamines Recently Used")
    Amphetamines_dim_1_Prior_Use = models.BooleanField(
        blank=True, default=False, verbose_name="Amphetamines Prior Use")
    Amphetamines_dim_1_Route = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Amphetamines Route")
    Amphetamines_dim_1_Frequency = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Amphetamines Frequency")
    Amphetamines_dim_1_Duration = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Amphetamines Duration")
    Amphetamines_dim_1_Date_of_Last_Use = models.DateField(
        null=True, blank=True, verbose_name="Amphetamines Date of Last Use")

    Alcohol_dim_1_Recently_Used = models.BooleanField(
        blank=True, default=False, verbose_name="Alcohol Recently Used")
    Alcohol_dim_1_Prior_Use = models.BooleanField(
        blank=True, default=False, verbose_name="Alcohol Prior Use")
    Alcohol_dim_1_Route = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Alcohol Route")
    Alcohol_dim_1_Frequency = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Alcohol Frequency")
    Alcohol_dim_1_Duration = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Alcohol Duration")
    Alcohol_dim_1_Date_of_Last_Use = models.DateField(
        null=True, blank=True, verbose_name="Alcohol Date of Last Use")

    Cocaine_Crack_dim_1_Recently_Used = models.BooleanField(
        blank=True, default=False, verbose_name="Cocaine/Crack Recently Used")
    Cocaine_Crack_dim_1_Prior_Use = models.BooleanField(
        blank=True, default=False, verbose_name="Cocaine/Crack Prior Use")
    Cocaine_Crack_dim_1_Route = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Cocaine/Crack Route")
    Cocaine_Crack_dim_1_Frequency = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Cocaine/Crack Frequency")
    Cocaine_Crack_dim_1_Duration = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Cocaine/Crack Duration")
    Cocaine_Crack_dim_1_Date_of_Last_Use = models.DateField(
        null=True, blank=True, verbose_name="Cocaine/Crack Date of Last Use")

    Heroin_dim_1_Recently_Used = models.BooleanField(
        blank=True, default=False, verbose_name="Heroin Recently Used")
    Heroin_dim_1_Prior_Use = models.BooleanField(
        blank=True, default=False, verbose_name="Amphetamines Heroin Use")
    Heroin_dim_1_Route = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Heroin Route")
    Heroin_dim_1_Frequency = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Heroin Frequency")
    Heroin_dim_1_Duration = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Heroin Duration")
    Heroin_dim_1_Date_of_Last_Use = models.DateField(
        null=True, blank=True, verbose_name="Heroin Date of Last Use")

    Marijuana_dim_1_Recently_Used = models.BooleanField(
        blank=True, default=False, verbose_name="Marijuana Recently Used")
    Marijuana_dim_1_Prior_Use = models.BooleanField(
        blank=True, default=False, verbose_name="Marijuana Prior Use")
    Marijuana_dim_1_Route = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Marijuana Route")
    Marijuana_dim_1_Frequency = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Marijuana Frequency")
    Marijuana_dim_1_Duration = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Marijuana Duration")
    Marijuana_dim_1_Date_of_Last_Use = models.DateField(
        null=True, blank=True, verbose_name="Marijuana Date of Last Use")

    Opioid_Pain_Medications_dim_1_Recently_Used = models.BooleanField(
        blank=True, default=False, verbose_name="Opioid Pain Medications Recently Used")
    Opioid_Pain_Medications_dim_1_Prior_Use = models.BooleanField(
        blank=True, default=False, verbose_name="Opioid Pain Medications Prior Use")
    Opioid_Pain_Medications_dim_1_Route = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Opioid Pain Medications Route")
    Opioid_Pain_Medications_dim_1_Frequency = models.CharField(
        max_length=500, default='', blank=True, verbose_name="Opioid Pain Medications Frequency")
    Opioid_Pain_Medications_dim_1_Duration = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Opioid Pain Medications Duration")
    Opioid_Pain_Medications_dim_1_Date_of_Last_Use = models.DateField(
        null=True, blank=True, verbose_name="Opioid Pain Medications Date of Last Use")

    Sedatives_dim_1_Recently_Used = models.BooleanField(
        blank=True, default=False, verbose_name="Sedatives Recently Used")
    Sedatives_dim_1_Prior_Use = models.BooleanField(
        blank=True, default=False, verbose_name="Sedatives Prior Use")
    Sedatives_dim_1_Route = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Sedatives Route")
    Sedatives_dim_1_Frequency = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Sedatives Frequency")
    Sedatives_dim_1_Duration = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Sedatives Duration")
    Sedatives_dim_1_Date_of_Last_Use = models.DateField(
        null=True, blank=True, verbose_name="Sedatives Date of Last Use")

    Hallucinogens_dim_1_Recently_Used = models.BooleanField(
        blank=True, default=False, verbose_name="Hallucinogens Recently Used")
    Hallucinogens_dim_1_Prior_Use = models.BooleanField(
        blank=True, default=False, verbose_name="Hallucinogens Prior Use")
    Hallucinogens_dim_1_Route = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Hallucinogens Route")
    Hallucinogens_dim_1_Frequency = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Hallucinogens Frequency")
    Hallucinogens_dim_1_Duration = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Hallucinogens Duration")
    Hallucinogens_dim_1_Date_of_Last_Use = models.DateField(
        null=True, blank=True, verbose_name="Hallucinogens Date of Last Use")

    Inhalants_dim_1_Recently_Used = models.BooleanField(
        blank=True, default=False, verbose_name="Inhalants Recently Used")
    Inhalants_dim_1_Prior_Use = models.BooleanField(
        blank=True, default=False, verbose_name="Inhalants Prior Use")
    Inhalants_dim_1_Route = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Inhalants Route")
    Inhalants_dim_1_Frequency = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Inhalants Frequency")
    Inhalants_dim_1_Duration = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Inhalants Duration")
    Inhalants_dim_1_Date_of_Last_Use = models.DateField(
        null=True, blank=True, verbose_name="Inhalants Date of Last Use")

    Over_the_Counter_Medications_dim_1_Recently_Used = models.BooleanField(
        blank=True, default=False, verbose_name="Over-the-Counter Medications Recently Used")
    Over_the_Counter_Medications_dim_1_Prior_Use = models.BooleanField(
        blank=True, default=False, verbose_name="Over-the-Counter Medications Prior Use")
    Over_the_Counter_Medications_dim_1_Route = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Over-the-Counter Medications Route")
    Over_the_Counter_Medications_dim_1_Frequency = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Over-the-Counter Medications Frequency")
    Over_the_Counter_Medications_dim_1_Duration = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Over-the-Counter Medications Duration")
    Over_the_Counter_Medications_dim_1_Date_of_Last_Use = models.DateField(
        null=True, blank=True, verbose_name="Over-the-Counter Medications Date of Last Use")

    Nicotine_dim_1_Recently_Used = models.BooleanField(
        blank=True, default=False, verbose_name="Nicotine Recently Used")
    Nicotine_dim_1_Prior_Use = models.BooleanField(
        blank=True, default=False, verbose_name="Nicotine Prior Use")
    Nicotine_dim_1_Route = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Nicotine Route")
    Nicotine_dim_1_Frequency = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Nicotine Frequency")
    Nicotine_dim_1_Duration = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Nicotine Duration")
    Nicotine_dim_1_Date_of_Last_Use = models.DateField(
        null=True, blank=True, verbose_name="Nicotine Date of Last Use")

    Other_dim_1_Recently_Used = models.BooleanField(
        blank=True, default=False, verbose_name="Other: Recently Used")
    Other_dim_1_Prior_Use = models.BooleanField(
        blank=True, default=False, verbose_name="Other: Prior Use")
    Other_dim_1_Route = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Other: Route")
    Other_dim_1_Frequency = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Other: Frequency")
    Other_dim_1_Duration = models.CharField(
        max_length=50, default='', blank=True, verbose_name="Other: Duration")
    Other_dim_1_Date_of_Last_Use = models.DateField(
        null=True, blank=True, verbose_name="Other: Date of Last Use")
    Other_Explanation_dim_1_page_1 = models.CharField(
        max_length=20, default='', blank=True, verbose_name="Other (Specify):")

# ---------------------------------------------------------------------------------------------------
    Client_Name_Dim_1_Page_1 = models.CharField(
        max_length=20, default='', blank=True, verbose_name="Client Name")
    Medi_Cal_ID_Dim_1_Page_1 = models.CharField(
        max_length=20, default='', blank=True, verbose_name="Medi-Cal ID")
    Treatment_Agency_Dim_1_Page_1 = models.CharField(
        max_length=20, default='', blank=True, verbose_name="Treatment Agency")

# ---------------------------------------------------------------------------------------------------

    # --------------------------------------------
    # Addtional Comments............
    Dimenion_1_Addtional_Information = models.TextField(
        max_length=200, default='', verbose_name="Additional Information", blank=True)

    # -------------------------------------------------

    Do_you_find_yourself_using_more_alcohol_and_or_drugs_than_you_intend_to = models.TextField(
        blank=True, default='', db_column="Do you find yourself using more alcohol and/or drugs than you intend to", max_length=200)
    Do_you_find_yourself_using_more_alcohol_and_or_drugs_than_you_intend_to_options = models.BooleanField(
        blank=True, default=False, db_column="Do_you_find_yourself_using_more_alcohol_and_or_drugs_you_intend_to_option: (Yes or No)")

    Do_you_get_physically_ill_when_you_stop_using_alcohol_and_or_drugs = models.TextField(
        blank=True, default='', db_column="Do you get physically ill when you stop using alcohol and/or drugs?", max_length=200)
    Do_you_get_physically_ill_when_you_stop_using_alcohol_and_or_drugs_to_option = models.BooleanField(
        blank=True, default=False, db_column="options: (Yes or No)")

    Are_you_currently_experiencing_withdrawal_symptoms_such_as_tremors_excessive_sweating_rapid_heart_rate_blackouts_anxiety_vomiting_etc = models.TextField(
        blank=True, default='', db_column="Are you currently experiencing withdrawal symptoms, such as tremors, excessive sweating, rapid heart rate,blackouts, anxiety, vomiting, etc", max_length=200)
    Are_you_currently_experiencing_withdrawal_symptoms_such_as_tremors_excessive_sweating_rapid_heart_rate_blackouts_anxiety_vomiting_etc_to_option = models.BooleanField(
        blank=True, default=False, db_column="experiencing_options: (Yes or No)")

    Do_you_have_a_history_of_serious_withdrawal_seizures_or_life_threatening_symptoms_during_withdrawal = models.TextField(
        blank=True, default='', db_column="Do you have a history of serious withdrawal, seizures, or life-threatening symptoms during withdrawal?", max_length=200)
    Do_you_have_a_history_of_serious_withdrawal_seizures_or_life_threatening_symptoms_during_withdrawal_to_option = models.BooleanField(
        blank=True, default=False, db_column="health_options: (Yes or No)")

    Do_you_find_yourself_using_more_alcohol_and_or_drugs_in_order_to_get_the_same_high = models.TextField(
        blank=True, default='', db_column="Do you find yourself using more alcohol and/or drugs in order to get the same high?", max_length=200)
    Do_you_find_yourself_using_more_alcohol_and_or_drugs_in_order_to_get_the_same_high_to_option = models.BooleanField(
        blank=True, default=False, db_column="Do you find yourself using more alcohol and/or  to get the same high?: (Yes or No)")

    Has_your_alcohol_and_or_drug_use_changed_recently_increase_decreased_changed_route_of_use = models.TextField(
        blank=True, default='', db_column="Has your alcohol and/or drug use changed recently (increase/ decreased, changed route of use)?", max_length=200)
    Has_your_alcohol_and_or_drug_use_changed_recently_increase_decreased_changed_route_of_use_to_option = models.BooleanField(
        blank=True, default=False, db_column="Has your alcohol and/or drug use changed recently ?: (Yes or No)")

    Please_describe_family_history_of_alcohol_and_or_drug_use = models.TextField(
        blank=True, default='', db_column="Please describe family history of alcohol and/or drug use:", max_length=200)


# --------------------------------------------------------------------------------------------------------
# Level of Severity ...
    severity_rating_dim_1 = models.CharField(max_length=15, choices=SEVERITY_RATING, default='5',
                                             db_column="Severity Rating- Dimension 1 (Substance Use, Acute Intoxication and/or Withdrawal Potential)",
                                             blank=True)
# --------------------------------------------------------------------------------------------------------

    Dimenion_2_Addtional_Information = models.TextField(
        max_length=200, default='', db_column="Additional Information", blank=True)


# -----------------------------------------------------------------------
# Dimension 2 Start Here ....
    dim_2_person_name_1 = models.TextField(
        max_length=40, verbose_name="Person 1 Name", blank=True, default='')
    dim_2_person_speciality_1 = models.TextField(
        max_length=100, verbose_name="Person 1 Specialty", blank=True, default='')
    dim_2_person_contact_1 = models.TextField(
        max_length=40, verbose_name="Person 1 Contact Number", blank=True, default='')
    dim_2_person_name_2 = models.TextField(
        max_length=40, verbose_name="Person 2 Name", blank=True, default='')
    dim_2_person_speciality_2 = models.TextField(
        max_length=100, verbose_name="Person 2 Specialty", blank=True, default='')
    dim_2_person_contact_2 = models.TextField(
        max_length=40, verbose_name="Person 2 Contact Number", blank=True, default='')
    dim_2_person_name_3 = models.TextField(
        max_length=40, verbose_name="Person 3 Name", blank=True, default='')
    dim_2_person_speciality_3 = models.TextField(
        max_length=100, verbose_name="Person 3 Specialty", blank=True, default='')
    dim_2_person_contact_3 = models.TextField(
        max_length=40, verbose_name="Person 3 Contact Number", blank=True, default='')
    dim_2_person_name_4 = models.TextField(
        max_length=40, verbose_name="Person 4 Name", blank=True, default='')
    dim_2_person_speciality_4 = models.TextField(
        max_length=100, verbose_name="Person 4 Specialty", blank=True, default='')
    dim_2_person_contact_4 = models.TextField(
        max_length=40, verbose_name="Person 4 Contact Number", blank=True, default='')
    dim_2_person_name_5 = models.TextField(
        max_length=40, verbose_name="Person 5 Name", blank=True, default='')
    dim_2_person_speciality_5 = models.TextField(
        max_length=100, verbose_name="Person 5 Specialty", blank=True, default='')
    dim_2_person_contact_5 = models.TextField(
        max_length=40, verbose_name="Person 5 Contact Number", blank=True, default='')


# -----------------------------------------------------------------------


# Dimension No.2 Medical Conditions ...
    Dim_2_medicalConditoins_Heart_Problems = models.BooleanField(
        blank=True, default=False, verbose_name="Heart Problems")
    Dim_2_medicalConditoins_Seizure_Neurological = models.BooleanField(
        blank=True, default=False, verbose_name="Seizure/Neurological")
    Dim_2_medicalConditoins_Muscle_Joint_Problems = models.BooleanField(
        blank=True, default=False, verbose_name="Muscle/Joint Problems")
    Dim_2_medicalConditoins_Diabetes = models.BooleanField(
        blank=True, default=False, verbose_name="Diabetes")
    Dim_2_medicalConditoins_High_Blood_Pressure = models.BooleanField(
        blank=True, default=False, verbose_name="High Blood Pressure")
    Dim_2_medicalConditoins_Thyroid_Problems = models.BooleanField(
        blank=True, default=False, verbose_name="Thyroid Problems")
    Dim_2_medicalConditoins_Vision_Problems = models.BooleanField(
        blank=True, default=False, verbose_name="Vision Problems")
    Dim_2_medicalConditoins_Sleep_Problems = models.BooleanField(
        blank=True, default=False, verbose_name="Sleep Problems")
    Dim_2_medicalConditoins_High_Cholesterol = models.BooleanField(
        blank=True, default=False, verbose_name="High Cholesterol")
    Dim_2_medicalConditoins_Kidney_Problems = models.BooleanField(
        blank=True, default=False, verbose_name="Kidney Problems")
    Dim_2_medicalConditoins_Hearing_Problems = models.BooleanField(
        blank=True, default=False, verbose_name="Hearing Problems")
    Dim_2_medicalConditoins_Chronic_Pain = models.BooleanField(
        blank=True, default=False, verbose_name="Chronic Pain")
    Dim_2_medicalConditoins_Blood_Disorder = models.BooleanField(
        blank=True, default=False, verbose_name="Blood Disorder")
    Dim_2_medicalConditoins_Liver_Problems = models.BooleanField(
        blank=True, default=False, verbose_name="Liver Problems")
    Dim_2_medicalConditoins_Dental_Problems = models.BooleanField(
        blank=True, default=False, verbose_name="Dental Problems")
    Dim_2_medicalConditoins_Pregnant = models.BooleanField(
        blank=True, default=False, verbose_name="Pregnant")
    Dim_2_medicalConditoins_Stomach_Intestinal_Problems = models.BooleanField(
        blank=True, default=False, verbose_name="Stomach/Intestinal Problems")
    Dim_2_medicalConditoins_Asthma_Lung_Problems = models.BooleanField(
        blank=True, default=False, verbose_name="Asthma/Lung Problems")
    Dim_2_medicalConditoins_Sexually_Transmitted_Disease = models.BooleanField(
        blank=True, default=False, verbose_name="Sexually Transmitted Disease(s)")
    Dim_2_medicalConditoins_Sexually_Transmitted_Disease_Explanation = models.CharField(
        max_length=50, blank=True, default='', db_column="Dim_2_medicalConditoins_Sexually_Transmitted_Disease_Explanation")

    Dim_2_medicalConditoins_Cancer_Disease = models.BooleanField(
        blank=True, default=False, db_column="Dim_2_medicalConditoins_Cancer_Disease")
    Dim_2_medicalConditoins_Cancer_Explanation = models.CharField(
        max_length=50, blank=True, default='', db_column="Dim_2_medicalConditoins_Cancer_Explanation")

    Dim_2_medicalConditoins_Infection_Disease = models.BooleanField(
        blank=True, default=False, db_column="Dim_2_medicalConditoins_Infection_Disease")
    Dim_2_medicalConditoins_Infection_Disease_Explanation = models.CharField(
        max_length=50, blank=True, default='', db_column="Dim_2_medicalConditoins_Infection_Disease_Explanation")

    Dim_2_medicalConditoins_Allergies_Disease = models.BooleanField(
        blank=True, default=False, verbose_name="Allergies Disease(s)")
    Dim_2_medicalConditoins_Allergies_Explanation = models.CharField(
        max_length=50, blank=True, default='', verbose_name="Allergies Explanation")

    Dim_2_medicalConditoins_Other_Disease = models.BooleanField(
        blank=True, default=False, verbose_name="Other Disease(s)")
    Dim_2_medicalConditoins_Other_Disease_Explanation = models.CharField(
        max_length=50, blank=True, default='', verbose_name="Other Explanation")

    Dim_2_Do_any_of_these_conditions_significantly_interfere_with_your_life_to_option = models.BooleanField(
        blank=True,
        default=False,
        db_column="Do any of these conditions significantly interfere with your life? (Yes or No):"
    )
    Dim_2_Do_any_of_these_conditions_significantly_interfere_with_your_life = models.TextField(
        blank=True,
        default='',
        db_column="Do any of these conditions significantly interfere in life?",
        max_length=200
    )

    Dim_2_Provide_additional_comments_on_medical_conditions_prior_hospitalizations_include_dates_and_reasons = models.TextField(
        blank=True,
        default='',
        db_column="Provide additional comments on medical conditions, prior hospitalizations (include dates and reasons)",
        max_length=200
    )

    Dim_2_Does_the_patient_report_medical_symptoms_that_would_be_considered_life_threatening_or_require_immediate_medical_attention_to_option = models.BooleanField(
        blank=True,
        default=False,
        db_column="Does the patient report medical symptoms that would be considered life-threatening or require immediate medical attention? (Yes or No):"
    )
    Dim_2_Does_the_patient_report_medical_symptoms_that_would_be_considered_life_threatening_or_require_immediate_medical_attention = models.TextField(
        blank=True,
        default='',
        db_column="Does the patient report medical symptoms  considered life-threatening or require immediate medical attention?",
        max_length=200
    )

    # Queastion No.14 Table ....
    Dim_2_current_medication_for_medical_condition_Medication_1 = models.TextField(
        max_length=40, db_column="Medication 1", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Dose_Frequency_1 = models.TextField(
        max_length=100, db_column="Dose/Frequency 1", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Reason_1 = models.TextField(
        max_length=40, db_column="Reason 1", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Effectiveness_Side_Effects_1 = models.TextField(
        max_length=40, db_column="Effectiveness/Side Effects 1", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Medication_2 = models.TextField(
        max_length=100, db_column="Medication 2", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Dose_Frequency_2 = models.TextField(
        max_length=40, db_column="Dose/Frequency 2  ", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Reason_2 = models.TextField(
        max_length=40, db_column="Reason 2", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Effectiveness_Side_Effects_2 = models.TextField(
        max_length=100, db_column="Effectiveness/Side Effects 2", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Medication_3 = models.TextField(
        max_length=40, db_column="Medication 3  ", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Dose_Frequency_3 = models.TextField(
        max_length=40, db_column="Dose/Frequency 3", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Reason_3 = models.TextField(
        max_length=100, db_column="Reason 3", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Effectiveness_Side_Effects_3 = models.TextField(
        max_length=40, db_column="Effectiveness/Side Effects 3", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Medication_4 = models.TextField(
        max_length=40, db_column="Medication 4", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Dose_Frequency_4 = models.TextField(
        max_length=100, db_column="Dose/Frequency 4", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Reason_4 = models.TextField(
        max_length=40, db_column="Reason 4", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Effectiveness_Side_Effects_4 = models.TextField(
        max_length=40, db_column="Effectiveness/Side Effects 4", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Medication_5 = models.TextField(
        max_length=40, db_column="Medication 5", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Dose_Frequency_5 = models.TextField(
        max_length=40, db_column="Dose/Frequency 5", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Reason_5 = models.TextField(
        max_length=40, db_column="Reason 5", blank=True, default='')
    Dim_2_current_medication_for_medical_condition_Effectiveness_Side_Effects_5 = models.TextField(
        max_length=40, db_column="Effectiveness/Side Effects 5", blank=True, default='')

    # Dimension No.2 Level of Severity ...
    severity_rating_dim_2 = models.CharField(max_length=15, choices=SEVERITY_RATING, default='5',
                                             verbose_name="Severity Rating- Dimension 2 (Biomedical Conditions and Complications)",
                                             blank=True)

    # Dimension 2 Ending Addtional Comments ...
    Dimenion_2_Addtional_Information_Ending = models.TextField(
        max_length=200, default='', verbose_name="Additional Comments", blank=True)

    # Dimension 3 Starts ...
    dim_3_problematic_Depression_sadness = models.BooleanField(
        blank=True, default=False, verbose_name="Depression/sadness")
    dim_3_problematic_Loss_of_Pleasure_Interest = models.BooleanField(
        blank=True, default=False, verbose_name="Loss of Pleasure/Interest")
    dim_3_problematic_Hopelessness = models.BooleanField(
        blank=True, default=False, verbose_name="Hopelessness")
    dim_3_problematic_Irritability_Anger = models.BooleanField(
        blank=True, default=False, verbose_name="Irritability/Anger")
    dim_3_problematic_Impulsivity = models.BooleanField(
        blank=True, default=False, verbose_name="Impulsivity")
    dim_3_problematic_Pressured_Speech = models.BooleanField(
        blank=True, default=False, verbose_name="Pressured Speech")
    dim_3_problematic_Grandiosity = models.BooleanField(
        blank=True, default=False, verbose_name="Grandiosity")
    dim_3_problematic_Racing_Thoughts = models.BooleanField(
        blank=True, default=False, verbose_name="Racing Thoughts")
    dim_3_problematic_Anxiety_Excessive_Worry = models.BooleanField(
        blank=True, default=False, verbose_name="Anxiety/Excessive Worry")
    dim_3_problematic_Obsessive_Thoughts = models.BooleanField(
        blank=True, default=False, verbose_name="Obsessive Thoughts")
    dim_3_problematic_Compulsive_Behaviors = models.BooleanField(
        blank=True, default=False, verbose_name="Compulsive Behaviors")
    dim_3_problematic_Flashbacks = models.BooleanField(
        blank=True, default=False, verbose_name="Flashbacks")
    dim_3_problematic_Paranoia = models.BooleanField(
        blank=True, default=False, verbose_name="Paranoia")
    dim_3_problematic_Delusions = models.BooleanField(
        blank=True, default=False, verbose_name="Delusions")
    dim_3_problematic_Delusions_Explanation = models.CharField(
        max_length=30, blank=True, default='', verbose_name="Delusions Explanation")
    dim_3_problematic_Hallucinations = models.BooleanField(
        blank=True, default=False, verbose_name="Hallucinations")
    dim_3_problematic_Hallucinations_Explanation = models.CharField(
        max_length=30, blank=True, default='', verbose_name="Hallucinations Explanation")
    dim_3_problematic_Sleep_Problems = models.BooleanField(
        blank=True, default=False, verbose_name="Sleep Problems")
    dim_3_problematic_Memory_Concentration = models.BooleanField(
        blank=True, default=False, verbose_name="Memory/Concentration")
    dim_3_problematic_Gambling = models.BooleanField(
        blank=True, default=False, verbose_name="Gambling")
    dim_3_problematic_Risky_Sex_Behaviors = models.BooleanField(
        blank=True, default=False, verbose_name="Risky Sex Behaviors")

    dim_3_problematic_Suicidal_Thoughts = models.BooleanField(
        blank=True, default=False, verbose_name="Suicidal Thoughts")
    dim_3_problematic_Suicidal_Thoughts_Explanation = models.TextField(
        max_length=200, blank=True, default='', verbose_name="Suicidal Thoughts Explanation")

    dim_3_problematic_Thoughts_of_Harming_Others = models.BooleanField(
        blank=True, default=False, verbose_name="Thoughts of Harming Others Thoughts")
    dim_3_problematic_Thoughts_of_Harming_Others_Explanation = models.TextField(
        max_length=30, blank=True, default='', verbose_name="Thoughts of Harming Others Explanation")

    dim_3_problematic_Abuse_physical_emotional_sexual = models.BooleanField(
        blank=True, default=False, verbose_name="Abuse (physical, emotional, sexual)")
    dim_3_problematic_Abuse_physical_emotional_sexual_Explanation = models.TextField(
        max_length=300, blank=True, default='', verbose_name="Abuse (physical, emotional, sexual) Explanation")

    dim_3_problematic_Traumatic_Event = models.BooleanField(
        blank=True, default=False, verbose_name="Traumatic Event")
    dim_3_problematic_Traumatic_Event_Explanation = models.TextField(
        max_length=300, blank=True, default='', verbose_name="Traumatic Event Explanation")

    dim_3_problematic_Other = models.BooleanField(
        blank=True, default=False, verbose_name="Other")
    dim_3_problematic_Other_Explanation = models.TextField(
        max_length=300, blank=True, default='', verbose_name="Other Explanation")

    dim_3_problematic_Have_you_ever_been_diagnosed_with_a_mental_illness = models.CharField(
        max_length=8, blank=True, default='0', db_column="Have you ever been diagnosed with a mental illness? (Yes or No or Not Sure)", choices=CHOICES_TYPE_4)
    dim_3_problematic_Have_you_ever_been_diagnosed_with_a_mental_illness_Explanation = models.TextField(
        max_length=300, blank=True, default='', db_column="Have you ever been diagnosed with a mental illness? Explanation")

    dim_3_problematic_17 = models.BooleanField(
        blank=True, default=False, verbose_name="Are you currently or have you previously received treatment for psychiatric or emotional problems? (Yes or No)", null=True)
    dim_3_problematic_17_Explanation = models.TextField(
        max_length=300, blank=True, default='', db_column="Are you currently or have you previously received treatment for psychiatric or emotional problems? Explanation")

    dim_3_problematic_Do_you_ever_see_or_hear_things_that_other_people_say_they_do_not_see_or_hear = models.BooleanField(
        blank=True, default=False, db_column="Do you ever see or hear things that other people say they do not see or hear? (Yes or No)", null=True)
    dim_3_problematic_Do_you_ever_see_or_hear_things_that_other_people_say_they_do_not_see_or_hear_Explanation = models.TextField(
        max_length=300, blank=True, default='', db_column="Do you ever see or hear  people say they do not see or hear? Explanation")

    dim_3_problem_19_option = models.CharField(
        max_length=4,  default='0', verbose_name="Based on previous questions, is further assessment of mental health needed? (Yes or No) ", choices=CHOICES_TYPE_3, blank=True)
    dim_3_problem_19 = models.TextField(max_length=200, blank=True, default='',
                                        verbose_name="Based on previous questions, is further assessment of mental health needed?")

    # Question No.20 Table ...

    # Queastion No.14 Table ....
    Dim_2_current_medication_for_psychiatric_condition_Medication_1 = models.TextField(
        max_length=40, db_column="Dim_2_current_medication_for_psychiatric_condition_Medication_1", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_condition_Dose_Frequency_1 = models.TextField(
        max_length=100, db_column="Dim_2_current_medication_for__1", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_condition_Reason_1 = models.TextField(
        max_length=40, db_column="Dim_2_current_medication_for_psychiatric_condition_Reason_1", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_condition_Effectiveness_Side_Effects_1 = models.TextField(
        max_length=40, db_column="Dim_2_current_medication_for_psychiatric__Effectiveness_Side_Effects_1", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_condition_Medication_2 = models.TextField(
        max_length=100, db_column="Dim_2_current_medication_for_psychiatric_condition_Medication_2", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_conditions_Dose_Frequency_2 = models.TextField(
        max_length=40, db_column="Dim_2_current_medication_for_psychiatricy_2", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_condition_Reason_2 = models.TextField(
        max_length=40, db_column="Dim_2_current_medication_for_psychiatric_condition_Reason_2", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_condition_Effective_Side_Effects_2 = models.TextField(
        max_length=100, db_column="Dim_2_current_medication_for__condition_Effectiveness_Side_Effects_2", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_condition_Medication_3 = models.TextField(
        max_length=40, db_column="Dim_2_current_medication_for_psychiatric_condition_Medication_3", blank=True, default='')
    Dim_2_current_medication_psychiatric_condition_Dose_Frequency_3 = models.TextField(
        max_length=40, db_column="Dim_2_current_medication_for__3", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_condition_Reason_3 = models.TextField(
        max_length=100, db_column="Dim_2_current_medication_for_psychiatric_condition_Reason_3", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_conditions_Effectiveness_Side_Effects_3 = models.TextField(
        max_length=40, db_column="Dim_2_current_for_psychiatric_condition_Effectiveness_Side_Effects_3", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_condition_Medication_4 = models.TextField(
        max_length=40, db_column="Dim_2_current_medication_for_psychiatric_condition_Medication_4", blank=True, default='')
    Dim_2_current_medication_for_psychiatrics_condition_Dose_Frequency_4 = models.TextField(
        max_length=100, db_column="Dim_2_current_medication_for_psychiatric_condition_Dose_4", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_condition_Reason_4 = models.TextField(
        max_length=40, db_column="Dim_2_current_medication_for_psychiatric_condition_Reason_4", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_condition_Effectivss_Side_Effects_4 = models.TextField(
        max_length=40, db_column="Dim_2_current__psychiatric_condition_Effectiveness_Side_Effects_4", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_condition_Medication_5 = models.TextField(
        max_length=40, db_column="Dim_2_current_medication_for_psychiatric_condition_Medication_5", blank=True, default='')
    Dim_2_current_medications_for_psychiatric_condition_Dose_Frequency_5 = models.TextField(
        max_length=40, db_column="Dim_2_current_medication_for_psychiatric__Frequency_5", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_condition_Reason_5 = models.TextField(
        max_length=40, db_column="Dim_2_current_medication_for_psychiatric_condition_Reason_5", blank=True, default='')
    Dim_2_current_medication_for_psychiatric_condition_Effects_Side_Effects_5 = models.TextField(
        max_length=40, db_column="Dim_current_medication_for_psychiatric_condition_Effectiveness_Side_Effects_5", blank=True, default='')


# Question No.21 Table Start Here ....
    dim_2_person_name_1_21 = models.TextField(
        max_length=40, verbose_name="Person 1 Name", blank=True, default='')
    dim_2_person_contact_1_21 = models.TextField(
        max_length=40, verbose_name="Person 1 Contact Number", blank=True, default='')
    dim_2_person_name_2_21 = models.TextField(
        max_length=40, verbose_name="Person 2 Name", blank=True, default='')
    dim_2_person_contact_2_21 = models.TextField(
        max_length=40, verbose_name="Person 2 Contact Number", blank=True, default='')
    dim_2_person_name_3_21 = models.TextField(
        max_length=40, verbose_name="Person 3 Name", blank=True, default='')
    dim_2_person_contact_3_21 = models.TextField(
        max_length=40, verbose_name="Person 3 Contact Number", blank=True, default='')
    dim_2_person_name_4_21 = models.TextField(
        max_length=40, verbose_name="Person 4 Name", blank=True, default='')
    dim_2_person_contact_4_21 = models.TextField(
        max_length=40, verbose_name="Person 4 Contact Number", blank=True, default='')

    severity_rating_dim_3 = models.CharField(max_length=15, choices=SEVERITY_RATING, default='5',
                                             verbose_name="Severity Rating- Dimension 3 (Emotional, Behavioral, or Cognitive Conditions and Complications)",
                                             blank=True)

    # Dimension 3 Addtional Comments Ending ..
    # Addtional Comments............
    Dimenion_3_Addtional_Information = models.TextField(
        max_length=200, default='', verbose_name="Additional Information", blank=True)


# Dimension 4 Start here...
# Question no.22

    dim_4_problem_22_0 = models.CharField(
        max_length=1, verbose_name="Is your alcohol and/or drug use affecting any of the following?", editable=True, default='', blank=True)
    dim_4_problem_22_1 = models.BooleanField(
        blank=True, default=False, verbose_name="Work")
    dim_4_problem_22_2 = models.BooleanField(
        blank=True, default=False, verbose_name="Mental Health")
    dim_4_problem_22_3 = models.BooleanField(
        blank=True, default=False, verbose_name="Physical Health")
    dim_4_problem_22_4 = models.BooleanField(
        blank=True, default=False, verbose_name="Finances")
    dim_4_problem_22_5 = models.BooleanField(
        blank=True, default=False, verbose_name="School")
    dim_4_problem_22_6 = models.BooleanField(
        blank=True, default=False, verbose_name="Relationships")
    dim_4_problem_22_7 = models.BooleanField(
        blank=True, default=False, verbose_name="Sexual Activity")
    dim_4_problem_22_8 = models.BooleanField(
        blank=True, default=False, verbose_name="Legal Matters")
    dim_4_problem_22_9 = models.BooleanField(
        blank=True, default=False, verbose_name="Handling Everyday Tasks")
    dim_4_problem_22_10 = models.BooleanField(
        blank=True, default=False, verbose_name="Self-esteem")
    dim_4_problem_22_11 = models.BooleanField(
        blank=True, default=False, verbose_name="Hygiene")
    dim_4_problem_22_12 = models.BooleanField(
        blank=True, default=False, verbose_name="Recreational Activities")
    dim_4_problem_22_13 = models.BooleanField(
        blank=True, default=False, verbose_name="Other:")
    dim_4_problem_22_13_explanation = models.TextField(
        max_length=150, blank=True, default='', verbose_name="Other Explanation")

    # Question No.23

    dim_4_problem_23 = models.CharField(
        max_length=4, blank=True, default="0",
        verbose_name="Do you continue to use alcohol or drugs despite having it affect theareas listed above? (Yes or no)", choices=CHOICES_TYPE_3)

    dim_4_problem_23_Exaplanation = models.TextField(
        max_length=150, blank=True, default="",
        verbose_name="Do you continue to use alcohol or drugs despite having it affect theareas listed above?")

    # Question no.24

    dim_4_problem_24 = models.CharField(
        max_length=4, blank=True, default="0",
        verbose_name="Have you received help for alcohol and/or drug problems in the past? (Yes or no)", choices=CHOICES_TYPE_3)

    dim_4_problem_24_Exaplanation = models.TextField(
        max_length=150, blank=True, default="",
        verbose_name="Have you received help for alcohol and/or drug problems in the past?")

    # Question No.24 Please list treatment provider(s) ....
    dim_4_person_name_1_21 = models.TextField(
        max_length=40, verbose_name="Person 1 Name", blank=True, default='')
    dim_4_person_contact_1_21 = models.TextField(
        max_length=40, verbose_name="Person 1 Contact Number", blank=True, default='')
    dim_4_person_name_2_21 = models.TextField(
        max_length=40, verbose_name="Person 2 Name", blank=True, default='')
    dim_4_person_contact_2_21 = models.TextField(
        max_length=40, verbose_name="Person 2 Contact Number", blank=True, default='')
    dim_4_person_name_3_21 = models.TextField(
        max_length=40, verbose_name="Person 3 Name", blank=True, default='')
    dim_4_person_contact_3_21 = models.TextField(
        max_length=40, verbose_name="Person 3 Contact Number", blank=True, default='')
    dim_4_person_name_4_21 = models.TextField(
        max_length=40, verbose_name="Person 4 Name", blank=True, default='')
    dim_4_person_contact_4_21 = models.TextField(
        max_length=40, verbose_name="Person 4 Contact Number", blank=True, default='')

    # Question No.25
    dim_4_problem_25_Exaplanation = models.TextField(
        max_length=150, blank=True, default="",
        verbose_name="Have you received help for alcohol and/or drug problems in the past?")

    # Question No.26
    dim_4_problem_26_Exaplanation = models.TextField(
        max_length=150, blank=True, default="",
        verbose_name=" What are potential barriers to your recovery (e.g., financial, transportation,relationships, etc.)?")

    # Questions No.27
    dim_4_problem_27 = models.CharField(
        max_length=1, blank=True, default="",
        verbose_name="How important is it for you to receive treatment for?")

    dim_4_problem_27_11 = models.CharField(
        max_length=15, blank=True, default="0",
        verbose_name="Alcohol Problems", choices=CHOICES_TYPE_2)

    dim_4_problem_27_22 = models.CharField(
        max_length=15, blank=True, default="0",
        verbose_name="Drug Problems", choices=CHOICES_TYPE_2)

    dim_4_problem_27_explanation = models.TextField(
        max_length=150, blank=True, default="",
        verbose_name="How important is it for you to receive treatment for? Please Describe")


# Level of Severity ...
    severity_rating_dim_4 = models.CharField(max_length=15, choices=SEVERITY_RATING, default='5',
                                             verbose_name="Severity Rating- Dimension 4 (Readiness to Change)",
                                             blank=True)

    # Addtional Comments............
    Dimenion_2_Addtional_Information = models.TextField(
        max_length=200, default='', verbose_name="Additional Information", blank=True)


# Dimension No.5

# Question No.28
    dim_5_problem_28 = models.CharField(
        max_length=1, blank=True, default="",
        verbose_name="In the last 30 days, how often have you experienced cravings, withdrawal symptoms, disturbing effects of use?")

    dim_5_problem_28_1 = models.CharField(
        max_length=15, blank=True, default="4",
        verbose_name="Alcohol", choices=CHOICES_TYPE_1)

    dim_5_problem_28_2 = models.CharField(
        max_length=15, blank=True, default="4",
        verbose_name="Drug", choices=CHOICES_TYPE_1)

    dim_5_problem_28_explanation = models.TextField(
        max_length=150, blank=True, default="",
        verbose_name="In the last 30 days, how often have you experienced cravings, withdrawal symptoms, disturbing effects of use? Please Describe")

    # Question No. 29
    dim_5_problem_29 = models.CharField(
        max_length=4, blank=True, default="0",
        verbose_name="Do you find yourself spending time searching for alcohol and/or drugs, or trying to recover from its effects? (Yes or No)", choices=CHOICES_TYPE_3)

    dim_5_problem_29_explanation = models.TextField(
        max_length=150, blank=True, default="",
        verbose_name="Do you find yourself spending time searching for alcohol and/or drugs, or trying to recover from its effects?")

    # Question No. 30
    dim_5_problem_30 = models.CharField(
        max_length=4, blank=True, default="0",
        verbose_name="Do you feel that you will either relapse or continue to use without treatment or additional support? (Yes or No)", choices=CHOICES_TYPE_3)

    dim_5_problem_30_explanation = models.TextField(
        max_length=150, blank=True, default="",
        verbose_name="Do you feel that you will either relapse or continue to use without treatment or additional support?")

    # Question No. 31
    dim_5_problem_31 = models.CharField(
        max_length=4, blank=True, default="0",
        verbose_name="Are you aware of your triggers to use alcohol and/or drugs? (Yes or No)", choices=CHOICES_TYPE_3)

    # Question no. 31 choices ...
    dim_5_problem_311 = models.BooleanField(
        default=False, verbose_name="Strong Cravings")
    dim_5_problem_312 = models.BooleanField(
        default=False, verbose_name="Work Pressure")
    dim_5_problem_313 = models.BooleanField(
        default=False, verbose_name="Mental Health")
    dim_5_problem_314 = models.BooleanField(
        default=False, verbose_name="Relationship Problems")
    dim_5_problem_315 = models.BooleanField(
        default=False, verbose_name="Difficulty Dealing with Feelings")
    dim_5_problem_316 = models.BooleanField(
        default=False, verbose_name="Financial Stressors")
    dim_5_problem_317 = models.BooleanField(
        default=False, verbose_name="Physical Health")
    dim_5_problem_318 = models.BooleanField(
        default=False, verbose_name="School Pressure")
    dim_5_problem_319 = models.BooleanField(
        default=False, verbose_name="Environment")
    dim_5_problem_3101 = models.BooleanField(
        default=False, verbose_name="Unemployment")
    dim_5_problem_3102 = models.BooleanField(
        default=False, verbose_name="Chronic Pain")
    dim_5_problem_3103 = models.BooleanField(
        default=False, verbose_name="Peer Pressure")
    dim_5_problem_3104 = models.BooleanField(
        default=False, verbose_name="Other")

    dim_5_problem_3104_explanation = models.TextField(
        max_length=150, blank=True, default="",
        verbose_name="Other Exaplanation")

    # Question No.32
    dim_5_problem_32 = models.TextField(
        max_length=200, blank=True, default="",
        verbose_name="What do you do if you are triggered?")

    # Question No.33
    dim_5_problem_33 = models.TextField(
        max_length=200, blank=True, default="",
        verbose_name="Can you please describe any attempts you have made to either control or cut down on your alcohol and/or drug use?")

    # Question No.34
    dim_5_problem_34 = models.TextField(
        max_length=200, blank=True, default="",
        verbose_name="What is the longest period of time that you have gone without using alcohol and/or drugs?")

    # Question No.35
    dim_5_problem_35 = models.TextField(
        max_length=200, blank=True, default="",
        verbose_name="What helped and didn’t help?")

# Level of Severity ...
    severity_rating_dim_5 = models.CharField(max_length=15, choices=SEVERITY_RATING, default='5',
                                             verbose_name="Severity Rating- Dimension 5 (Relapse, continued Use, or Continued Problem Potential)",
                                             blank=True)

    dim_5_problem_Additional_comments = models.TextField(
        max_length=200, blank=True, default="", verbose_name="Additional Comments")


# Dimesion 6 start here...

# Question No.36
    dim_6_problem_36 = models.TextField(
        max_length=200, blank=True, default="",
        verbose_name="Do you have any relationships that are supportive of your recovery? (e.g., family, friends)")

# Question No.37
    dim_6_problem_37 = models.TextField(
        max_length=200, blank=True, default="",
        verbose_name="What is your current living situation (e.g., homeless, living with family/alone)?")

# Question No.38
    dim_6_problem_38_option = models.CharField(
        max_length=4,  default='None', blank=True, verbose_name="Do you currently live in an environment where others are using drugs? (Yes or No) ", choices=CHOICES_TYPE_3)
    dim_6_problem_38 = models.TextField(
        max_length=200, blank=True, default="",
        verbose_name="Do you currently live in an environment where others are using drugs? Please Describe")


# Question No.39
    dim_6_problem_39_option = models.CharField(
        max_length=4,  default='None', blank=True, verbose_name="Are you currently involved in relationships or situations that pose a threat to your safety? (Yes or No) ", choices=CHOICES_TYPE_3)
    dim_6_problem_39 = models.TextField(
        max_length=200, blank=True, default="",
        verbose_name="Are you currently involved in relationships or situations that pose a threat to your safety? Please Describe")

# Question No.40
    dim_6_problem_40_option = models.CharField(
        max_length=4,  default='None',blank=True, verbose_name="Are you currently involved in relationships or situations that would negatively impact your recovery? (Yes or No) ", choices=CHOICES_TYPE_3)
    dim_6_problem_40 = models.TextField(
        max_length=200, blank=True, default="",
        verbose_name="Are you currently involved in relationships or situations that would negatively impact your recovery? Please Describe")

    # Question No.41
    dim_6_problem_41_option = models.CharField(
        max_length=4,  default='None', blank=True, verbose_name="Are you currently employed or enrolled in school? (Yes or No) ", choices=CHOICES_TYPE_3)
    dim_6_problem_41 = models.TextField(
        max_length=200, blank=True, default="",
        verbose_name="Are you currently employed or enrolled in school? Please Describe")

    # Question No.42
    dim_6_problem_42_option = models.CharField(
        max_length=4,  default='None',blank=True, verbose_name="Are you currently involved with social services or the legal system (e.g., DCFS, court mandated, probation, parole)? (Yes or No) ", choices=CHOICES_TYPE_3)
    dim_6_problem_42 = models.TextField(
        max_length=200, blank=True, default="",
        verbose_name="Are you currently involved with social services or the legal system (e.g., DCFS, court mandated, probation, parole)? Please Describe")

    # Question no 42 table ....
    dim_6_person_name_1 = models.TextField(
        max_length=40, verbose_name="Name of Probation/Parole Officer 1 (If on parole/probation)", blank=True, default='')
    dim_6_person_contact_1 = models.TextField(
        max_length=40, verbose_name="Contact Number of Probation/Parole Officer 1 (If on parole/probation)", blank=True, default='')

    dim_6_person_name_2 = models.TextField(
        max_length=40, verbose_name="Name of Probation/Parole Officer 2 (If on parole/probation)", blank=True, default='')
    dim_6_person_contact_2 = models.TextField(
        max_length=40, verbose_name="Contact Number of Probation/Parole Officer 2 (If on parole/probation)", blank=True, default='')


# --------------------------------------------------------------------------------------------------------
# Level of Severity ...
    severity_rating_dim_6 = models.CharField(max_length=15, choices=SEVERITY_RATING, default='5',
                                             verbose_name="Severity Rating- Dimension 6 Recovery/Living Environment",
                                             blank=True)
# --------------------------------------------------------------------------------------------------------

    dim_6_problem_Additional_comments = models.TextField(
        max_length=200, blank=True, default="", verbose_name="Additional Comments")


# Summary of Multidimensional Assessment Table
    severity_rating_dim_1_Rationale_option = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Dimension No.1 Rationale Severity Rating Rationale", choices=CHOICES_TYPE_0)

    severity_rating_dim_1_Rationale = models.TextField(
        max_length=100, verbose_name="Dimension No.1 Rationale", blank=True, default='')

    severity_rating_dim_2_Rationale_option = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Dimension No.2 Rationale Severity Rating Rationale", choices=CHOICES_TYPE_0)
    severity_rating_dim_2_Rationale = models.TextField(
        max_length=100, verbose_name="Dimension No.2 Rationale", blank=True, default='')

    
    severity_rating_dim_3_Rationale_option = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Dimension No.3 Rationale Severity Rating Rationale", choices=CHOICES_TYPE_0)
    
    severity_rating_dim_3_Rationale = models.TextField(
        max_length=100, verbose_name="Dimension No.3 Rationale", blank=True, default='')


    severity_rating_dim_4_Rationale_option = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Dimension No.4 Rationale Severity Rating Rationale", choices=CHOICES_TYPE_0)

    severity_rating_dim_4_Rationale = models.TextField(
        max_length=100, verbose_name="Dimension No.4 Rationale", blank=True, default='')

    
    severity_rating_dim_5_Rationale_option = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Dimension No.5 Rationale Severity Rating Rationale", choices=CHOICES_TYPE_0)
    


    severity_rating_dim_5_Rationale = models.TextField(
        max_length=100, verbose_name="Dimension No.5 Rationale", blank=True, default='')

    
    severity_rating_dim_6_Rationale_option = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Dimension No.6 Rationale Severity Rating Rationale", choices=CHOICES_TYPE_0)

    
    severity_rating_dim_6_Rationale = models.TextField(
        max_length=100, verbose_name="Dimension No.6 Rationale", blank=True, default='')


# Diagnosis: Diagnostic Statistical Manual, 5th Edition (DSM-5) Criteria For Substance Use Disorder
    # Substance Use Disorder Criteria (DSM-5)
    Name_of_Substance_1 = models.CharField(
        max_length=15, blank=True, default='', verbose_name="Name of Substance No.1")
    Name_of_Substance_2 = models.CharField(
        max_length=15, blank=True, default='', verbose_name="Name of Substance No.2")
    Name_of_Substance_3 = models.CharField(
        max_length=15, blank=True, default='', verbose_name="Name of Substance No.3")

    substance_1_1 = models.BooleanField(
        default=False, verbose_name="Substance often taken in larger amounts or over a longer period than was intended : Subtance_1")
    substance_1_2 = models.BooleanField(
        default=False, verbose_name="Substance often taken in larger amounts or over a longer period than was intended : Subtance_2")
    substance_1_3 = models.BooleanField(
        default=False, verbose_name="Substance often taken in larger amounts or over a longer period than was intended : Subtance_3")
    substance_2_1 = models.BooleanField(
        default=False, verbose_name="There is a persistent desire or unsuccessful efforts to cut down or control substance use : Subtance_1")
    substance_2_2 = models.BooleanField(
        default=False, verbose_name="There is a persistent desire or unsuccessful efforts to cut down or control substance use : Subtance_2")
    substance_2_3 = models.BooleanField(
        default=False, verbose_name="There is a persistent desire or unsuccessful efforts to cut down or control substance use : Subtance_3")
    substance_3_1 = models.BooleanField(
        default=False, verbose_name="A great deal of time is spent in activities necessary to obtain the substance, use the substance, or recover from its effects : Subtance_1")
    substance_3_2 = models.BooleanField(
        default=False, verbose_name="A great deal of time is spent in activities necessary to obtain the substance, use the substance, or recover from its effects : Subtance_2")
    substance_3_3 = models.BooleanField(
        default=False, verbose_name="A great deal of time is spent in activities necessary to obtain the substance, use the substance, or recover from its effects : Subtance_3")
    substance_4_1 = models.BooleanField(
        default=False, verbose_name="Craving, or a strong desire or urge to use the substance : Subtance_1")
    substance_4_2 = models.BooleanField(
        default=False, verbose_name="Craving, or a strong desire or urge to use the substance : Subtance_2")
    substance_4_3 = models.BooleanField(
        default=False, verbose_name="Craving, or a strong desire or urge to use the substance : Subtance_3")
    substance_5_1 = models.BooleanField(
        default=False, verbose_name="Recurrent substance use resulting in a failure to fulfill major role obligations at work, school, or home : Subtance_1")
    substance_5_2 = models.BooleanField(
        default=False, verbose_name="Recurrent substance use resulting in a failure to fulfill major role obligations at work, school, or home : Subtance_2")
    substance_5_3 = models.BooleanField(
        default=False, verbose_name="Recurrent substance use resulting in a failure to fulfill major role obligations at work, school, or home : Subtance_3")
    substance_6_1 = models.BooleanField(
        default=False, verbose_name="Continued substance use despite having persistent or recurrent social or interpersonal problems caused or exacerbated by the effects of the substance : Subtance_1")
    substance_6_2 = models.BooleanField(
        default=False, verbose_name="Continued substance use despite having persistent or recurrent social or interpersonal problems caused or exacerbated by the effects of the substance : Subtance_2")
    substance_6_3 = models.BooleanField(
        default=False, verbose_name="Continued substance use despite having persistent or recurrent social or interpersonal problems caused or exacerbated by the effects of the substance : Subtance_3")
    substance_7_1 = models.BooleanField(
        default=False, verbose_name="Important social, occupational, or recreational activities are given up or reduced because of substance use : Subtance_1")
    substance_7_2 = models.BooleanField(
        default=False, verbose_name="Important social, occupational, or recreational activities are given up or reduced because of substance use : Subtance_2")
    substance_7_3 = models.BooleanField(
        default=False, verbose_name="Important social, occupational, or recreational activities are given up or reduced because of substance use : Subtance_3")
    substance_8_1 = models.BooleanField(
        default=False, verbose_name="Recurrent substance use in situations in which it is physically hazardous : Subtance_1")
    substance_8_2 = models.BooleanField(
        default=False, verbose_name="Recurrent substance use in situations in which it is physically hazardous : Subtance_2")
    substance_8_3 = models.BooleanField(
        default=False, verbose_name="Recurrent substance use in situations in which it is physically hazardous : Subtance_3")
    substance_9_1 = models.BooleanField(
        default=False, verbose_name="Continued substance use despite knowledge of having a persistent or recurrent physical or psychological problem that is likely to have been caused or exacerbated by the substance : Subtance_1")
    substance_9_2 = models.BooleanField(
        default=False, verbose_name="Continued substance use despite knowledge of having a persistent or recurrent physical or psychological problem that is likely to have been caused or exacerbated by the substance : Subtance_2")
    substance_9_3 = models.BooleanField(
        default=False, verbose_name="Continued substance use despite knowledge of having a persistent or recurrent physical or psychological problem that is likely to have been caused or exacerbated by the substance : Subtance_3")
    substance_10_1 = models.BooleanField(
        default=False, verbose_name="Tolerance : Subtance_1")
    substance_10_2 = models.BooleanField(
        default=False, verbose_name="Tolerance : Subtance_2")
    substance_10_3 = models.BooleanField(
        default=False, verbose_name="Tolerance : Subtance_3")
    substance_11_1 = models.BooleanField(
        default=False, verbose_name="Withdrawal : Subtance_1")
    substance_11_2 = models.BooleanField(
        default=False, verbose_name="Withdrawal : Subtance_2")
    substance_11_3 = models.BooleanField(
        default=False, verbose_name="Withdrawal : Subtance_3")

    Total_Number_of_Criteria_1 = models.CharField(
        max_length=6, verbose_name="Total Number of Criteria : Substance 1 : ", default='', blank=True)
    Total_Number_of_Criteria_2 = models.CharField(
        max_length=6, verbose_name="Total Number of Criteria : Substance 2 : ", default='', blank=True)
    Total_Number_of_Criteria_3 = models.CharField(
        max_length=6, verbose_name="Total Number of Criteria : Substance 3 : ", default='', blank=True)

    list_of_substance = models.TextField(max_length=300, default="", blank=True,
                                         verbose_name="List of Substance Use Disorder(s) that Meet DSM-5 Criteria and Date of DSM-5 Diagnosis (specify severity level)")

# Page Number 14

    # ASAM LEVEL OF CARE DETERMINATION TOOL

    asme_1_dimension_1 = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Ambulatory Withdrawal Management without Extended On-Site Monitoring (1-WM)", choices=CHOICES_TYPE_0)
    asme_2_dimension_1 = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Ambulatory Withdrawal Management with Extended On-Site Monitoring (2-WM)", choices=CHOICES_TYPE_0)
    asme_3_dimension_1 = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Clinically Managed Residential Withdrawal Management (3.2-WM)", choices=(
                                              ('0', 'Unkown'),
                                              ('1', 'Moderate'),
                                              ('2', 'Severe')
                                          ))
    asme_4_dimension_1 = models.BooleanField(default=False, blank=True,
                                             verbose_name="Medically Monitored Inpatient Withdrawal Management (3.7-WM)")

    asme_5_dimension_1 = models.BooleanField(default=False, blank=True,
                                             verbose_name="Medically Managed Intensive Inpatient Withdrawal Management (4-WM)")

    asme_6_dimension_1 = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Early Intervention (0.5) Dimension No.1", choices=(
                                              ('0', 'Unknown'),
                                              ('1', 'None'),
                                              ('2', 'Mild')))

    asme_6_dimension_2 = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Early Intervention (0.5) Dimension No.2", choices=(
                                              ('0', 'Unknown'),
                                              ('1', 'None'),
                                              ('2', 'Mild')))

    asme_6_dimension_3 = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Early Intervention (0.5) Dimension No.3", choices=(
                                              ('0', 'Unknown'),
                                              ('1', 'None'),
                                              ('2', 'Mild')))
    asme_6_dimension_4 = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Early Intervention (0.5) Dimension No.4", choices=(
                                              ('0', 'Unknown'),
                                              ('1', 'None'),
                                              ('2', 'Mild')))
    asme_6_dimension_5 = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Early Intervention (0.5) Dimension No.5", choices=(
                                              ('0', 'Unknown'),
                                              ('1', 'None'),
                                              ('2', 'Mild')))
    asme_6_dimension_6 = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Early Intervention (0.5) Dimension No.6", choices=(
                                              ('0', 'Unknown'),
                                              ('1', 'None'),
                                              ('2', 'Mild')))

    asme_7_dimension_1 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Outpatient Services Dimension 1 (1)", choices=CHOICES_TYPE_0)

    asme_7_dimension_2 = models.CharField(max_length=10, default='0', blank=True, verbose_name="Outpatient Services Dimension 2 (1)", choices=(('0', 'Unknown'),
                                                                                                                                                ('1', 'None'),
                                                                                                                                                ('2', 'Mild'),
                                                                                                                                                ('3', 'Moderate')
                                                                                                                                                ))
    asme_7_dimension_3 = models.CharField(max_length=10, default='0', blank=True, verbose_name="Outpatient Services Dimension 3 (1)", choices=(('0', 'Unknown'),
                                                                                                                                                ('1', 'None'),
                                                                                                                                                ('2', 'Mild'),
                                                                                                                                                ('3', 'Moderate')
                                                                                                                                                ))
    asme_7_dimension_4 = models.CharField(max_length=10, default='0', blank=True, verbose_name="Outpatient Services Dimension 4 (1)", choices=(('0', 'Unknown'),
                                                                                                                                                ('1', 'None'),
                                                                                                                                                ('2', 'Mild'),
                                                                                                                                                ('3', 'Moderate')
                                                                                                                                                ))
    asme_7_dimension_5 = models.CharField(max_length=10, default='0', blank=True, verbose_name="Outpatient Services Dimension 5 (1)", choices=(('0', 'Unknown'),
                                                                                                                                                ('1', 'None'),
                                                                                                                                                ('2', 'Mild'),
                                                                                                                                                ('3', 'Moderate')
                                                                                                                                                ))
    asme_7_dimension_6 = models.CharField(max_length=10, default='0', blank=True, verbose_name="Outpatient Services Dimension 6 (1)", choices=(('0', 'Unknown'),
                                                                                                                                                ('1', 'None'),
                                                                                                                                                ('2', 'Mild'),
                                                                                                                                                ('3', 'Moderate')
                                                                                                                                                ))

    asme_8_dimension_1 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Intensive Outpatient Services Dimension 1 (2.1)", choices=CHOICES_TYPE_0)

    asme_8_dimension_2 = models.CharField(max_length=10, default='0', blank=True, verbose_name="Intensive Outpatient Services Dimension 2 (2.1)", choices=(('0', 'Unknown'),
                                                                                                                                                            ('1', 'None'),
                                                                                                                                                            ('2', 'Mild'),
                                                                                                                                                            ('3', 'Moderate')
                                                                                                                                                            ))

    asme_8_dimension_3 = models.CharField(max_length=10, default='0', blank=True, verbose_name="Intensive Outpatient Services Dimension 3 (2.1)", choices=(('0', 'Unknown'),
                                                                                                                                                            ('1', 'None'),
                                                                                                                                                            ('2', 'Mild'),
                                                                                                                                                            ('3', 'Moderate')
                                                                                                                                                            ))

    asme_8_dimension_4 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Intensive Outpatient Services Dimension 4 (2.1)", choices=CHOICES_TYPE_0)

    asme_8_dimension_5 = models.CharField(max_length=10, default='0', blank=True, verbose_name="Intensive Outpatient Services Dimension 5 (2.1)", choices=(('0', 'Unknown'),
                                                                                                                                                            ('1', 'None'),
                                                                                                                                                            ('2', 'Mild'),
                                                                                                                                                            ('3', 'Moderate')
                                                                                                                                                            ))

    asme_8_dimension_6 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Intensive Outpatient Services Dimension 6 (2.1)", choices=CHOICES_TYPE_0)

    asme_9_dimension_1 = models.CharField(max_length=10,  default='0', blank=True,
                                          verbose_name="Clinically Managed Low-Intensity Residential Servicest Dimension 1 (3.1)", choices=(
                                              ('0', 'Unkown'),
                                              ('1', 'Moderate'),
                                              ('2', 'Severe')
                                          ))

    asme_9_dimension_2 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Clinically Managed Low-Intensity Residential Servicest Dimension 2 (3.1)", choices=CHOICES_TYPE_0)

    asme_9_dimension_3 = models.CharField(max_length=10, default='0', blank=True, verbose_name="Clinically Managed Low-Intensity Residential Servicest Dimension 3 (3.1)", choices=(('0', 'Unknown'),
                                                                                                                                                                                     ('1', 'None'),
                                                                                                                                                                                     ('2', 'Mild'),
                                                                                                                                                                                     ('3', 'Moderate')
                                                                                                                                                                                     ))

    asme_9_dimension_4 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Clinically Managed Low-Intensity Residential Servicest Dimension 4 (3.1)", choices=CHOICES_TYPE_0)

    asme_9_dimension_5 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Clinically Managed Low-Intensity Residential Servicest Dimension 5 (3.1)", choices=CHOICES_TYPE_0)

    asme_9_dimension_6 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Clinically Managed Low-Intensity Residential Servicest Dimension 6 (3.1)", choices=CHOICES_TYPE_0)

    # ------------------------

    asme_10_dimension_1 = models.CharField(max_length=10,  default='0', blank=True,
                                           verbose_name="Clinically Managed Population-Specific High-Intensity Residential Services Dimension 1 (3.3)", choices=(
                                               ('0', 'Unkown'),
                                               ('1', 'Moderate'),
                                               ('2', 'Severe')
                                           ))

    asme_10_dimension_2 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Clinically Managed Population-Specific High-Intensity Residential Services Dimension 2 (3.3)", choices=CHOICES_TYPE_0)

    asme_10_dimension_3 = models.CharField(max_length=10, default='0', blank=True, verbose_name="Clinically Managed Population-Specific High-Intensity Residential Services Dimension 3 (3.3)", choices=(('0', 'Unknown'),
                                                                                                                                                                                                          ('1', 'None'),
                                                                                                                                                                                                          ('2', 'Mild'),
                                                                                                                                                                                                          ('3', 'Moderate')
                                                                                                                                                                                                          ))

    asme_10_dimension_4 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Clinically Managed Population-Specific High-Intensity Residential Services Dimension 4 (3.3)", choices=CHOICES_TYPE_0)

    asme_10_dimension_5 = models.CharField(max_length=10,  default='0', blank=True,
                                           verbose_name="Clinically Managed Population-Specific High-Intensity Residential Services Dimension 5 (3.3)", choices=(
                                               ('0', 'Unkown'),
                                               ('1', 'Moderate'),
                                               ('2', 'Severe')
                                           ))

    asme_10_dimension_6 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Clinically Managed Population-Specific High-Intensity Residential Services Dimension 6 (3.3)", choices=(
            ('0', 'Unkown'),
            ('1', 'Moderate'),
            ('2', 'Severe')
        ))

    # --------------------------------

    asme_11_dimension_1 = models.BooleanField(default=False, blank=True,
                                              verbose_name="Clinically Managed High-Intensity Residential Services Dimension 1 (3.5)")

    asme_11_dimension_2 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Clinically Managed High-Intensity Residential Services Dimension 2 (3.5)", choices=CHOICES_TYPE_0)

    asme_11_dimension_3 = models.CharField(max_length=10, default='0', blank=True, verbose_name="Clinically Managed High-Intensity Residential Services Dimension 3 (3.5)", choices=(('0', 'Unknown'),
                                                                                                                                                                                      ('1', 'None'),
                                                                                                                                                                                      ('2', 'Mild'),
                                                                                                                                                                                      ('3', 'Moderate')
                                                                                                                                                                                      ))

    asme_11_dimension_4 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Clinically Managed High-Intensity Residential Services Dimension 4 (3.5)", choices=CHOICES_TYPE_0)

    asme_11_dimension_5 = models.CharField(max_length=10,  default='0', blank=True,
                                           verbose_name="Clinically Managed High-Intensity Residential Services Dimension 5 (3.5)", choices=(
                                               ('0', 'Unkown'),
                                               ('1', 'Moderate'),
                                               ('2', 'Severe')
                                           ))

    asme_11_dimension_6 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Clinically Managed High-Intensity Residential Services Dimension 6 (3.5)", choices=(
            ('0', 'Unkown'),
            ('1', 'Moderate'),
            ('2', 'Severe')
        ))


        # --------------------
    asme_12_dimension_1 = models.BooleanField(default=False, blank=True,
                                              verbose_name="Medically Monitored Intensive Inpatient Services Dimension 1 (3.7)")
   


    asme_12_dimension_2 = models.CharField(max_length=10,  default='0', blank=True,
                                           verbose_name="Medically Monitored Intensive Inpatient Services Dimension 2 (3.7)", choices=(
                                               ('0', 'Unkown'),
                                               ('1', 'Moderate'),
                                               ('2', 'Severe')
                                           ))



    asme_12_dimension_3 = models.BooleanField(default=False, blank=True,
                                              verbose_name="Medically Monitored Intensive Inpatient Services Dimension 3 (3.7)")


    asme_12_dimension_4 = models.CharField(max_length=10,  default='0', blank=True,
                                           verbose_name="Medically Monitored Intensive Inpatient Services Dimension 4 (3.7)", choices=(
                                               ('0', 'Unkown'),
                                               ('1', 'Moderate'),
                                               ('2', 'Severe')
                                           ))

    asme_12_dimension_5 = models.CharField(max_length=10,  default='0', blank=True,
                                           verbose_name="Medically Monitored Intensive Inpatient Services Dimension 5 (3.7)", choices=(
                                               ('0', 'Unkown'),
                                               ('1', 'Moderate'),
                                               ('2', 'Severe')
                                           ))


    asme_12_dimension_6 = models.BooleanField(default=False, blank=True,
                                              verbose_name="Medically Monitored Intensive Inpatient Services Dimension 6 (3.7)")



        # --------------------
    asme_13_dimension_1 = models.BooleanField(default=False, blank=True,
                                              verbose_name="Medically Managed Intensive Inpatient Services Dimension 1 (4)")
   


    asme_13_dimension_2 = models.CharField(max_length=10,  default='0', blank=True,
                                           verbose_name="Medically Managed Intensive Inpatient Services Dimension 2 (4)", choices=(
                                               ('0', 'Unkown'),
                                               ('1', 'Moderate'),
                                               ('2', 'Severe')
                                           ))



    asme_13_dimension_3 = models.BooleanField(default=False, blank=True,
                                              verbose_name="Medically Managed Intensive Inpatient Services Dimension 3 (4)")


    asme_13_dimension_4 = models.CharField(max_length=10,  default='0', blank=True,
                                           verbose_name="Medically Managed Intensive Inpatient Services Dimension 4 (4)", choices=(
                                               ('0', 'Unkown'),
                                               ('1', 'Moderate'),
                                               ('2', 'Severe')
                                           ))

    asme_13_dimension_5 = models.CharField(max_length=10,  default='0', blank=True,
                                           verbose_name="Medically Managed Intensive Inpatient Services Dimension 5 (4)", choices=(
                                               ('0', 'Unkown'),
                                               ('1', 'Moderate'),
                                               ('2', 'Severe')
                                           ))


    asme_13_dimension_6 = models.BooleanField(default=False, blank=True,
                                              verbose_name="Medically Managed Intensive Inpatient Services Dimension 6 (4)")

    
    asme_14_dimension_1 = models.CharField(
        max_length=10, default='0', blank=True, verbose_name="Opioid Treatment Program Dimension 1 (OTP)", choices=CHOICES_TYPE_0)

    asme_14_dimension_2 = models.CharField(
    max_length=10, default='0', blank=True, verbose_name="Opioid Treatment Program Dimension 2 (OTP)", choices=CHOICES_TYPE_0)

    asme_14_dimension_3 = models.CharField(
    max_length=10, default='0', blank=True, verbose_name="Opioid Treatment Program Dimension 3 (OTP)", choices=CHOICES_TYPE_0)

    asme_14_dimension_4 = models.CharField(
    max_length=10, default='0', blank=True, verbose_name="Opioid Treatment Program Dimension 4 (OTP)", choices=CHOICES_TYPE_0)

    asme_14_dimension_5 = models.CharField(
    max_length=10, default='0', blank=True, verbose_name="Opioid Treatment Program Dimension 5 (OTP)", choices=CHOICES_TYPE_0)

    asme_14_dimension_6 = models.CharField(
    max_length=10, default='0', blank=True, verbose_name="Opioid Treatment Program Dimension 6 (OTP)", choices=CHOICES_TYPE_0)


    mat_problem_to_option = models.CharField(blank=True, default='0', choices=CHOICES_TYPE_3, verbose_name="Would the patient with alcohol or opioid use disorders benefit from and be interested in Medication-Assisted Treatment (MAT)?(Yes or No)", max_length=4)

    mat_problem_explanation = models.TextField(max_length=100, default='', blank=True, verbose_name="Would the patient with alcohol or opioid use disorders benefit from and be interested in Medication-Assisted Treatment (MAT)? Describe")

    # Placement Summary
    summary_1 = models.TextField(max_length=100, default='', blank=True, verbose_name="Enter the ASAM Level of Care (e.g., 3.1, 2.1, 3.2, W.M) number that offers the most appropriate treatment setting given the patient’s current severity and functioning")
    summary_2 = models.TextField(max_length=100, default='', blank=True, verbose_name="If the most appropriate Level of Care is not utilized, then enter the next appropriate Level of Care and check off the reason for this discrepancy (below)")

    # Reason for Discrepancy:
    Reason_for_Discrepancy_1 = models.BooleanField(default=False, blank=True, verbose_name="Reason for Discrepancy Not Applicable (Yes or No) :")
    Reason_for_Discrepancy_2 = models.BooleanField(default=False, blank=True, verbose_name="Reason for Discrepancy Service Not Available (Yes or No) :")
    Reason_for_Discrepancy_3 = models.BooleanField(default=False, blank=True, verbose_name="Reason for Discrepancy Provider Judgment (Yes or No) :")
    Reason_for_Discrepancy_4 = models.BooleanField(default=False, blank=True, verbose_name="Reason for Discrepancy Patient Preference (Yes or No) :")
    Reason_for_Discrepancy_5 = models.BooleanField(default=False, blank=True, verbose_name="Reason for Discrepancy Transportation (Yes or No) :")
    Reason_for_Discrepancy_6 = models.BooleanField(default=False, blank=True, verbose_name="Reason for Discrepancy Accessibility (Yes or No) :")
    Reason_for_Discrepancy_7 = models.BooleanField(default=False, blank=True, verbose_name="Reason for Discrepancy Financial (Yes or No) :")
    Reason_for_Discrepancy_8 = models.BooleanField(default=False, blank=True, verbose_name="Reason for Discrepancy Preferred to Wait (Yes or No) :")
    Reason_for_Discrepancy_9 = models.BooleanField(default=False, blank=True, verbose_name="Reason for Discrepancy Language/ Cultural Considerations (Yes or No) :")
    Reason_for_Discrepancy_10 = models.BooleanField(default=False, blank=True, verbose_name="Reason for Discrepancy Environment (Yes or No) :")
    Reason_for_Discrepancy_11 = models.BooleanField(default=False, blank=True, verbose_name="Reason for Discrepancy Mental Health (Yes or No) :")
    Reason_for_Discrepancy_12 = models.BooleanField(default=False, blank=True, verbose_name="Reason for Discrepancy Physical Health (Yes or No) :")
    Reason_for_Discrepancy_13 = models.BooleanField(default=False, blank=True, verbose_name="Reason for Discrepancy Other (Yes or No) :")
    Reason_for_Discrepancy_13_Title = models.CharField(max_length=50 ,default='', blank=True, verbose_name="Reason for Discrepancy Other Title :")
    Reason_for_Discrepancy_13_Explanation = models.TextField(max_length=150 ,default='', blank=True, verbose_name="Reason for Discrepancy Other Explanation :")
    summary_3 = models.TextField(max_length=150 ,default='', blank=True, verbose_name="Designated Treatment Location and Provider Name :")
    
    summary_4 = models.CharField(max_length=50 ,default='', blank=True, verbose_name="Counselor Name (if applicable)")
    summary_4_date = models.DateField(blank=True, null=True, verbose_name="Counselor Name (if applicable) Date")

    summary_5 = models.CharField(max_length=50 ,default='', blank=True, verbose_name="Licensed-eligible LPHA Name (if applicable)")
    summary_5_date = models.DateField(blank=True, null=True, verbose_name="Licensed-eligible LPHA Name (if applicable) Date")
    summary_6 = models.CharField(max_length=50 ,default='', blank=True, verbose_name="Licensed LPHA Name")
    summary_6_date = models.DateField(blank=True, null = True, verbose_name="Licensed LPHA Name Date")

    def __str__(self):
        return "Demographic Information by {name}".format(name=self.name_page_1)

class Grievance_Procedure(models.Model):
    user   =   models.ForeignKey(User,on_delete=models.CASCADE)    
    grievance= models.CharField(max_length=100)
    recognizes= models.CharField(max_length=100)
    class Meta:
        verbose_name_plural= 'Grievance Procedure'

class Rights_of_Each_Client_or_Bill_of_Rights(models.Model):
    user   =   models.ForeignKey(User,on_delete=models.CASCADE)    
    policy= models.CharField(max_length=100)
    procedure= models.CharField(max_length=100)
    client= models.CharField(max_length=100)
    class Meta:
        verbose_name_plural= 'Rights of Each Client/Bill of Rights'


class case_note(models.Model):
    user   =   models.ForeignKey(User,on_delete=models.CASCADE)    
    case_note= models.CharField(max_length=10000)
    class Meta:
        verbose_name_plural= 'Case Note'


class consent(models.Model):
    user   =   models.ForeignKey(User,on_delete=models.CASCADE)    
    note1= models.CharField(max_length=10000)
    note2= models.CharField(max_length=10000)
    class Meta:
        verbose_name_plural= 'Informed Consent and Disclosure'
class program(models.Model):
    user   =   models.ForeignKey(User,on_delete=models.CASCADE)    
    date1= models.CharField(max_length=10000)
    date2= models.CharField(max_length=10000)
    class Meta:
        verbose_name_plural= 'Program Schedule'

class program_rules(models.Model):
    user   =   models.ForeignKey(User,on_delete=models.CASCADE)    
    program_rules= models.CharField(max_length=10000)
    class Meta:
        verbose_name_plural= 'Program Rules'
    