test = {
  'name': '6.9',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'my_list' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your loop is off.
          >>> my_list == [(k.lower(), v+10) for k, v in ages_dict.items()]
          True
          """
        },
      ]
    }
  ]
}