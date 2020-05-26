test = {
  'name': 'lab5p3',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It seems the face_str variable was not created.
          >>> # Typo?
          >>> 'face_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Something is off with your if statement.
          >>> # Please test your code by trying out all possibilities.
          >>> ((face_str == 'Washington') and (notes_int == 1)) or ((face_str == 'Jefferson') and (notes_int == 2)) or ((face_str == 'Lincoln') and (notes_int == 5)) or ((face_str == 'Hamilton') and (notes_int == 10)) or ((face_str == 'Jackson') and (notes_int == 20)) or ((face_str == 'Grant') and (notes_int == 50)) or ((face_str == 'Franklin') and (notes_int == 100)) or ((face_str == 'not on US banknote') and (notes_int not in [1,2,5,10,20,50,100]))
          True
          """
        }
      ]
    }
  ]
}

    