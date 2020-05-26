test = {
  'name': 'lab3_p3a',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It seems sub_lst was not created.
          >>> # Maybe a typo?
          >>> 'sub_lst' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It seems the slicing is not correct.
          >>> sub_lst == [1, 4, 7, 10, 13, 16]
          True
          """
        }
      ]
    }
  ]
}