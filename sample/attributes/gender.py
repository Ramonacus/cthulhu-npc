from attributes import weighted_attr


gender = weighted_attr.generate(
    ['non-binary', 'trans female', 'trans male', 'female', 'male'],
    [0.2, 0.3, 0.3, 49.6, 49.6])
