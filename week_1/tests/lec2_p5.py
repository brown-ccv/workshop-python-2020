test = {
  'name': '2.5',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # name_age_str.  Maybe there's a typo?
          >>> 'name_age_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to name_age_str is
          >>> # not correct. 
          >>> name_age_str == '{} {}'.format('Ashley', 30)
          True
          """
        }
      ]
    }
  ]
}