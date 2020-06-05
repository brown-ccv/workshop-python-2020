test = {
  'name': 'l7p2',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It seems the oldies_lst list was not created.
          >>> # Typo?
          >>> 'oldies_lst' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Something is off with your if statement.
          >>> # Ashley is not older than 30.
          >>> 'Ashley' not in oldies_lst
          True
          """
        },
        {
          'code': r"""
          >>> # Something is off with your if statement.
          >>> oldies_lst == ['Andras', 'Madonna']
          True
          """
        }    
      ]
    }
  ]
}