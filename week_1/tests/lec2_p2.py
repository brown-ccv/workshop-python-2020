test = {
  'name': '2.2',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # comb_str.  Maybe there's a typo?
          >>> 'comb_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to comb_str is
          >>> # not correct. 
          >>> comb_str == another_uppercase_str + a_symbol_str + an_uppercase_str
          True
          """
        }
      ]
    }
  ]
}