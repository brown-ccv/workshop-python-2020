test = {
  'name': '2.6',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # check_pal_bool.  Maybe there's a typo?
          >>> 'check_pal_bool' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to check_pal_bool is
          >>> # not correct. 
          >>> check_pal_bool == (first_str == first_str[::-1])
          True
          """
        }
      ]
    }
  ]
}