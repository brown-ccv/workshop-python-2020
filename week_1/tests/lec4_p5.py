test = {
  'name': '4.5',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # The value assigned to the key 'ATL' is
          >>> # not correct. 
          >>> cities_dict['ATL'] == 'Atlanta, GA'
          True
          """
        }
      ]
    }
  ]
}