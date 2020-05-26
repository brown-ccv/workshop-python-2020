test = {
  'name': '2.9',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # lower_str.  Maybe there's a typo?
          >>> 'lower_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to lower_str is
          >>> # not correct. 
          >>> lower_str == sentence_str.lower()
          True
          """
        }
      ]
    }
  ]
}