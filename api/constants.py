def enum(*sequential, **named):
  enums = dict(zip(sequential, range(len(sequential))), **named)
  return type('Enum', (), enums);

Link_Types = enum(
  none = 0,
  facebook = 1,
  twitter  = 2,
  linkedin = 3,
  medium   = 4,
  github   = 5,
  heroku   = 6,
  site     = 7,
)

LINK_TYPES = (
  (Link_Types.none, ''),
  (Link_Types.facebook, 'FACEBOOK'),
  (Link_Types.twitter, 'TWITTER'),
  (Link_Types.linkedin, 'LINKEDIN'),
  (Link_Types.medium, 'MEDIUM'),
  (Link_Types.github, 'GITHUB'),
  (Link_Types.heroku, 'HEROKU'),
  (Link_Types.site, 'SITE'),
)