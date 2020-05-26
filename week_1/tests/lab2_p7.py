test = {
  'name': '2.7',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # f_str.  Maybe there's a typo?
          >>> 'f_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to f_str is
          >>> # not correct. 
          >>> f_str == sentence_str.split()
          True
          """
        }
      ]
    }
  ]
}