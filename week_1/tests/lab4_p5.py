test = {
  'name': '4.5',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you don't have a variable
          >>> # named check_juan_bool. Maybe there's a typo?
          >>> 'check_juan_bool' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value of check_juan_bool is not correct.
          >>> check_juan_bool == 'Juan' in ages_dict
          False
          """
        }
      ]
    }
  ]
}