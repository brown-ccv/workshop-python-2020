test = {
  'name': '2.5',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # d_str.  Maybe there's a typo?
          >>> 'd_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to d_str is
          >>> # not correct. 
          >>> d_str == sentence_str * 3
          True
          """
        }
      ]
    }
  ]
}