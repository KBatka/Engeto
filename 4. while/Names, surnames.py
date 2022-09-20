students = ['Adam, Baker','Chelsea, Archer',
            'Marcus, Archer','Oliver, Cook',
            'Alex, Dyer', 'Sandra, Turner',
            'Ann, Fisher', 'Glenn, Hawkins',
            'Samuel, Baker','Clara, Slater',
            'Tyler, Hunt', 'Alex, Smith',
            'Clara, Woodman','Abraham, Mason',
            'Marcus, Sawyer','Alex, Glover',
            'Glenn, Cook','Clara, Fisher',
            'Alfred, Dyer', 'Curt, Head',
            'Oliver, Slater','Alex, Mason',
            'Tyler, Fisher','Ann, Parker',
            'Samuel, Hawkins', 'Ann, Woodman',
            'Sandra, Slater', 'Curt, Dyer']

seznam = str(students)
rozdel = seznam.split(',')
jmena = rozdel[::2]
prijmeni = rozdel[::1]
print(jmena, prijmeni)