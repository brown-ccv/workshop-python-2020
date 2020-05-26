test = {
  'name': '4.4',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like the key 'NYC' doesn't exist.
          >>> # Maybe there's a typo?
          >>> 'NYC' in cities_dict
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to the key 'NYC' is
          >>> # not correct. 
          >>> cities_dict['NYC'] == 'Brooklyn'
          True
          """
        }
      ]
    }
  ]
}