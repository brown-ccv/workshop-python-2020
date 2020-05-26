test = {
  'name': '4.2',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you don't have a variable
          >>> # named oldest_int. Maybe there's a typo?
          >>> 'oldest_int' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value of oldest_int is not correct.
          >>> oldest_int == ages_dict['Emily']
          True
          """
        }
      ]
    }
  ]
}