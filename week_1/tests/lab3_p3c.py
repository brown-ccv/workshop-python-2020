test = {
  'name': 'lab3_p3c',
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
          >>> sub_lst == [3, 7, 11, 15]
          True
          """
        }
      ]
    }
  ]
}