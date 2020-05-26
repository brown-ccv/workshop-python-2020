test = {
  'name': 'lab3_p2b',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like Willie is not in the list.
          >>> # Please check the spelling too.
          >>> 'Willie' in my_favorite_things_lst
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like Willie's index is not 1.
          >>> my_favorite_things_lst.index('Willie') == 1
          True
          """
        }
      
      ]
    }
  ]
}