test = {
  'name': 'lab3_p2c',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like chocolate is not in the list.
          >>> # Please check the spelling too.
          >>> 'chocolate' in my_favorite_things_lst
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like chocolate is not the third element of the list.
          >>> my_favorite_things_lst.index('chocolate') == 2
          True
          """
        }
      
      ]
    }
  ]
}