test = {
  'name': '8.1',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like one of your variables is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'lloyd' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like one of your variables is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'alice' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like one of your variables is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'tyler' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like one of your variables is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'students' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your lloyd dictionary is off.
          >>> lloyd == {"name": "Lloyd","homework": [90.0, 97.0, 75.0, 92.0],"quizzes": [88.0, 40.0, 94.0],"tests": [75.0, 90.0]}
          True
          """
        },
        {
          'code': r"""
          >>> # Your alice dictionary is off.
          >>> alice == {"name": "Alice","homework": [100.0, 92.0, 98.0, 100.0],"quizzes": [82.0, 83.0, 91.0],"tests": [89.0, 97.0]}
          True
          """
        },
        {
          'code': r"""
          >>> # Your tyler dictionary is off.
          >>> tyler == {"name": "Tyler","homework": [0.0, 87.0, 75.0, 22.0],"quizzes": [0.0, 75.0, 78.0],"tests": [100.0, 100.0]}
          True
          """
        },
        {
          'code': r"""
          >>> # Your students list is off.
          >>> students == [lloyd, alice, tyler]
          True
          """
        },
      ]
    }
  ]
}