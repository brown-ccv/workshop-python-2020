test = {
  'name': 'lab5p1',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It seems the pay_charge_bool variable was not created.
          >>> # Typo?
          >>> 'pay_charge_bool' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Something is off with your if statement.
          >>> # Please test your code by trying out all possibilities.
          >>> ((weight_flt > 50) and (pay_charge_bool == True)) or ((weight_flt <= 50) and (pay_charge_bool == False))
          True
          """
        }
      ]
    }
  ]
}