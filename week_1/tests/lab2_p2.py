test = {
  'name': '2.2',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # a_str.  Maybe there's a typo?
          >>> 'a_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to a_str is
          >>> # not correct. 
          >>> a_str == sentence_str[-4:]
          True
          """
        }
      ]
    }
  ]
}