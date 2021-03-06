Formatting Coordinate Strings
-----------------------------

Getting a string representation of a coordinate is best approached by
treating the components (e.g., RA and Dec) separately.  For example::

  >>> from astropy.coordinates import ICRSCoordinates
  >>> from astropy import units as u
  >>> c = ICRSCoordinates(187.70592, 12.39112, unit=(u.degree, u.degree))
  >>> str(c.ra) + ' ' + str(c.dec)
  '187d42m21.31200s 12d23m28.03200s'

To get better control over the formatting, you can use the angles'
`~astropy.coordinates.angle.Angle.to_string` method (see :doc:`angles`
for more).  For example::

  >>> rahmsstr = c.ra.to_string(u.hour)
  >>> str(rahmsstr)
  '12h30m49.42080s'
  >>> decdmsstr = c.dec.to_string(u.degree, alwayssign=True)
  >>> str(decdmsstr)
  '+12d23m28.03200s'
  >>> rahmsstr + ' ' + decdmsstr
  u'12h30m49.42080s +12d23m28.03200s'
