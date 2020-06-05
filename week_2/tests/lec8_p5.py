test = {
  'name': '8.5',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'res_list' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your function is off for input.
          >>> res_list == 'The Anatolian Shepherd dog was developed to be independent and forceful'.split()
          True
          """
        }
      ]
    }
  ]
}