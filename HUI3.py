

# HUI3 APPLY
Coefficient = 1.371
perfecthealth = 0.371
#dictionary
dictCoefficients = {'vision':             [1,0.98,0.89,0.84,0.75,0.61],
                    'hearing':            [1,0.95,0.89,0.8,0.74,0.61],
                    'speech':               [1,0.94,0.89,0.81,0.68],
                    'dexterity':      [1,0.95,0.88,0.76,0.65,0.56],
                    'emotion':      [1,0.95,0.85,0.64,0.46],
                    'cognition':      [1,0.92,0.95,0.83,0.6,0.42],
                    'pain':   [1,0.96,0.9,0.77,0.55],
                    };

#two quote and click return to get the param

def get_score(vision,hearing,speech,dexterity,emotion,cognition,pain):
    """

    :param vision:
    :param hearing:
    :param speech:CARDIOMETABOLIC
    :param dexterity:
    :param emotion:
    :param cognition:
    :param pain:
    :return:
    """

    if not(vision in [1,2,3,4,5,6]):
        raise ValueError("vision level can take only 1,2,3,4,5,6")
    if not(hearing in [1,2,3,4,5,6]):
        raise ValueError("hearing level can take only 1,2,3,4,5,6")
    if not(speech in [1,2,3,4,5]):
        raise ValueError("speech level can take only 1,2,3,4,5")
    if not(dexterity in [1,2,3,4,5,6]):
            raise ValueError("dexterity level can take only 1,2,3,4,5,6")
    if not(emotion in [1,2,3,4,5]):
            raise ValueError("emotion level can take only 1,2,3,4,5")
    if not(cognition in [1,2,3,4,5,6]):
            raise ValueError("cognition level can take only 1,2,3,4,5,6")
    if not(pain in [1,2,3,4,5]):
            raise ValueError("pain level can take only 1,2,3,4,5")




    score = 0

    score = Coefficient*dictCoefficients['vision'][vision - 1] * dictCoefficients['hearing'][hearing - 1] \
                * dictCoefficients['speech'][speech - 1]*dictCoefficients['dexterity'][dexterity - 1]\
                *dictCoefficients['emotion'][emotion - 1]*dictCoefficients['cognition'][cognition - 1]\
                *dictCoefficients['pain'][pain - 1] - perfecthealth


    return score

#use function
print(get_score(1,2,5,1,1,1,1))
