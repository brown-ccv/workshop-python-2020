test = {
  'name': '2.6',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # e_str.  Maybe there's a typo?
          >>> 'e_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to e_str is
          >>> # not correct. 
          >>> e_str == sentence_str + "sometimes"
          True
          """
        }
      ]
    }
  ]
}