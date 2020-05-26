test = {
  'name': 'lab3_p4a',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It seems nested_lst was not created.
          >>> # Maybe a typo?
          >>> 'nested_lst' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # There should be three elements in nested_lst. 
          >>> len(nested_lst) == 3
          True
          """
        },
        {
          'code': r"""
          >>> # The last elements of nested_lst should be a list that contains two strings. 
          >>> (len(nested_lst[2])==2) and (type(nested_lst[2][0]) == str) and (type(nested_lst[2][1]) == str)
          True
          """
        }
      ]
    }
  ]
}