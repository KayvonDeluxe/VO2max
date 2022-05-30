import numpy as np

def get_vo2max(age, sex, weight, height, rhr, phys):
    '''
    age, years
    sex, male or female
    weight, kg
    height, cm
    rhr, resting heart rate per minute 
    phys, what is your exercise activity level:
    0. Avoid walking or exertion, e.g., always use elevator, drive whenever possible instead of walking.
    1. Walk for pleasure, routinely use stairs, or occasionally exercise sufficiently to cause heavy breathing or perspiration.
    2. 10 to 60 minutes per week.
    3. Over one hour per week.
    4. Run about 1 mile per week or walk about 1.3 miles per week or spend about 30 minutes per week in comparable physical activity.
    5. Run 1 to 5 miles per week or walk 1.3 to 6 miles per week or spend 30 to 60 minutes per week in comparable physical activity.
    6. Run 6 to 10 miles per week or walk 7 to 13 miles per week or spend in 1 to 3 hours per week in comparable physical activity.
    7. Run 11 to 15 miles per week or walk 14 to 20 miles per week or spend 4 to 6 hours per week in comparable physical activity.,
    8. Run 16 to 20 miles per week or walk 21 to 26 miles per week or spend 6 to 8 hours per week in comparable physical activity.
    9. Run 21 to 25 miles per week or walk 27 to 33 miles per week or spend 9 to 11 hours per week in comparable physical activity.
    10. Run over 25 miles per week or walk over 34 miles per week or spend over 12 hours per week in comparable physical activity.
    This calculator is intended for illustrative and educational purposes only and is not warranted for any medical use. For more detailed information, please refer to:
    1. Jackson, A S et al. Prediction of functional aerobic capacity without exercise testing. Medicine and science in sports and exercise vol. 22,6 (1990): 863-70.
    2. Ekblom-Bak, Elin et al. Sex- and age-specific associations between cardiorespiratory fitness, CVD morbidity and all-cause mortality in 266.109 adults. Preventive medicine vol. 127 (2019): 105799.
    3. Uth, N., Sorensen, H., Overgaard, K., & Pedersen, P. K. (2004). Estimation of VO2max from the ratio between HRmax and HRrest-the Heart Rate Ratio Method. European journal of applied physiology, 91(1), 111-115.
    4. Farazdaghi, G. R., & Wohlfart, B. (2001). Reference values for the physical work capacity on a bicycle ergometer for women between 20 and 80 years of age. Clinical physiology (Oxford, England), 21(6), 682-687.
    5. Wohlfart, B., & Farazdaghi, G. R. (2003). Reference values for the physical work capacity on a bicycle ergometer for men - a comparison with a previous study on women. Clinical physiology and functional imaging, 23(3), 166-170.
    '''

    bmi = weight/(height/100)**2

    vo2max_1 = 56.363 + 1.921 * phys - 0.754 * bmi - 0.381 * age

    if sex == 'male':

        mhr = 203.7 / (1 + np.exp(0.033 * (age - 104.3)))

        vo2max_1 += 10.987

    elif sex == 'female':

        mhr = 190.2 / (1 + np.exp(0.0453 * (age - 107.5)))

    else:
        
        raise SystemExit('Something went wrong. Check your sex and try again.')

    vo2max_2 = 15.3 * mhr / rhr

    vo2max = 2 * vo2max_1 * vo2max_2 / (vo2max_1 + vo2max_2)
    
    # ""The risk for all-cause mortality and CVD morbidity decreased by 2.3% and 2.6% per increase in 1 ml·min-1·kg-1 
    # with no significant sex-differences..." [2]
    relative_death_risk = (1 - 0.023)**(vo2max - 35)

    years = -10. * np.log(relative_death_risk)
    
    return round(vo2max), round(age - years)
