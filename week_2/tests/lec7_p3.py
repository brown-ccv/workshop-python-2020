test = {
  'name': 'l7p3',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It seems the can_vote_lst list was not created.
          >>> # Typo?
          >>> 'can_vote_lst' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Something is off with your if statement.
          >>> [age >= 18 for fam in ages_lst for age in fam] == [item for fam in can_vote_lst for item in fam]
          True
          """
        }   
      ]
    }
  ]
}